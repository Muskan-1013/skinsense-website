const SUPABASE_URL =
    "https://ezztfywicvrajevxngjc.supabase.co";
const SUPABASE_KEY =
    "sb_publishable_EZ-ZHcOnSEWQVyEmKAMeXg_TyjygF1j";
const supabaseClient = window.supabase.createClient(
    SUPABASE_URL,
    SUPABASE_KEY,
    {
        auth: {
            persistSession: true,
            autoRefreshToken: true,
            detectSessionInUrl: true
        }
    }
);
function makeUsername(email) {
    const localPart = (email || "skin")
        .split("@")[0]
        .toLowerCase()
        .replace(/[^a-z0-9]/g, "");
    const prefix = localPart.slice(0, 6) || "skin";
    const randomNumber = Math.floor(1000 + Math.random() * 9000);
    return prefix + "_" + randomNumber;
}
function getOrCreateUsername(user) {
    const metadata = user.user_metadata || {};
    const storageKey = "skinsense_username_" + user.id;
    let username = metadata.username || "";
    if (!username) {
        try {
            username = localStorage.getItem(storageKey) || "";
        } catch (error) {
            username = "";
        }
    }
    if (!username) {
        username = makeUsername(user.email);
    }
    try {
        localStorage.setItem(storageKey, username);
    } catch (error) {
        // Supabase user metadata is the persistent fallback.
    }
    return username;
}
async function ensureUsername(user) {
    if (!user) {
        return "skin_user";
    }
    const username = getOrCreateUsername(user);
    const metadata = user.user_metadata || {};
    if (!metadata.username) {
        try {
            const updateResult = await supabaseClient.auth.updateUser({
                data: {
                    username: username
                }
            });
            if (updateResult.error) {
                console.error(
                    "Could not save username to Supabase Auth:",
                    updateResult.error.message
                );
            }
        } catch (error) {
            console.error("Could not update username:", error);
        }
    }
    /*
     * This requires a public.profiles table with user_id and username columns,
     * plus RLS policies that allow each signed-in user to write only their row.
     * If you have not created that table, remove this upsert block.
     */
    try {
        const profileResult = await supabaseClient
            .from("profiles")
            .upsert(
                {
                    user_id: user.id,
                    username: username
                },
                {
                    onConflict: "user_id"
                }
            );
        if (profileResult.error) {
            console.error(
                "Could not save profile row:",
                profileResult.error.message
            );
        }
    } catch (error) {
        console.error("Could not save profile row:", error);
    }
    return username;
}
function showHomeProfile(username) {
    const label = document.getElementById("profile-label");
    const profileLink = document.getElementById("profile-link");
    const logoutButton = document.getElementById("logout-button");
    if (label) {
        label.textContent = username;
        label.hidden = false;
    }
    if (profileLink) {
        profileLink.hidden = false;
    }
    if (logoutButton) {
        logoutButton.hidden = false;
    }
}
function finishHomeStartup() {
    const splash = document.getElementById("splash-screen");
    if (splash) {
        splash.classList.add("splash-hidden");
    }
    document.body.classList.remove("auth-checking");
}
async function startHomePage() {
    const sessionTimeout = window.setTimeout(function () {
        window.location.replace("login.html");
    }, 12000);
    try {
        const result = await supabaseClient.auth.getSession();
        window.clearTimeout(sessionTimeout);
        if (result.error) {
            throw result.error;
        }
        if (!result.data.session) {
            window.location.replace("signup.html");
            return;
        }
        const user = result.data.session.user;
        const username = getOrCreateUsername(user);
        showHomeProfile(username);
        window.setTimeout(finishHomeStartup, 1600);
        /*
         * Save the username in the background. Do not make the splash screen
         * wait for the profile-table request to finish.
         */
        ensureUsername(user)
            .then(function (savedUsername) {
                showHomeProfile(savedUsername);
            })
            .catch(function (error) {
                console.error("Could not finish saving the username:", error);
            });
        supabaseClient.auth.onAuthStateChange(function (event, session) {
            if (event === "SIGNED_OUT") {
                window.location.replace("signup.html");
                return;
            }
            if (session && session.user) {
                const sessionUsername = getOrCreateUsername(session.user);
                showHomeProfile(sessionUsername);
            }
        });
    } catch (error) {
        window.clearTimeout(sessionTimeout);
        console.error("Could not check the sign-in session:", error);
        window.location.replace("login.html");
    }
}
async function redirectIfLoggedIn() {
    try {
        const result = await supabaseClient.auth.getSession();
        if (!result.error && result.data.session) {
            window.location.replace("index.html");
        }
    } catch (error) {
        console.error("Could not check the sign-in session:", error);
    }
}
async function signUpUser() {
    const email = document.getElementById("signup-email").value.trim();
    const password = document.getElementById("signup-password").value;
    const message = document.getElementById("signup-message");
    const username = makeUsername(email);
    const result = await supabaseClient.auth.signUp({
        email: email,
        password: password,
        options: {
            data: {
                username: username
            },
            emailRedirectTo: window.location.origin + "/index.html"
        }
    });
    if (result.error) {
        if (message) {
            message.textContent = result.error.message;
        }
        return;
    }
    if (result.data.session) {
        window.location.replace("index.html");
        return;
    }
    if (message) {
        message.textContent =
            "Account created. Check your email to verify it, then return to SkinSense.";
    }
}
async function loginUser() {
    const email = document.getElementById("login-email").value.trim();
    const password = document.getElementById("login-password").value;
    const message = document.getElementById("login-message");
    const result = await supabaseClient.auth.signInWithPassword({
        email: email,
        password: password
    });
    if (result.error) {
        if (message) {
            message.textContent = result.error.message;
        }
        return;
    }
    window.location.replace("index.html");
}
async function loginWithGoogle() {
    const result = await supabaseClient.auth.signInWithOAuth({
        provider: "google",
        options: {
            redirectTo: window.location.origin + "/index.html"
        }
    });
    if (result.error) {
        console.error("Google sign-in failed:", result.error.message);
        alert(result.error.message);
    }
}
async function sendPasswordReset() {
    const emailElement = document.getElementById("reset-email");
    const message = document.getElementById("reset-message");
    if (!emailElement) {
        return;
    }
    const result = await supabaseClient.auth.resetPasswordForEmail(
        emailElement.value.trim(),
        {
            redirectTo: window.location.origin + "/reset-password.html"
        }
    );
    if (result.error) {
        if (message) {
            message.textContent = result.error.message;
        }
        return;
    }
    if (message) {
        message.textContent =
            "If the email is registered, a password reset link has been sent.";
    }
}
async function updatePassword() {
    const passwordElement = document.getElementById("new-password");
    const message = document.getElementById("update-password-message");
    if (!passwordElement) {
        return;
    }
    const result = await supabaseClient.auth.updateUser({
        password: passwordElement.value
    });
    if (result.error) {
        if (message) {
            message.textContent = result.error.message;
        }
        return;
    }
    if (message) {
        message.textContent = "Your password has been updated.";
    }
}
async function loadAccount() {
    const nameElement = document.getElementById("account-username");
    try {
        const result = await supabaseClient.auth.getUser();
        if (result.error || !result.data.user) {
            window.location.replace("signup.html");
            return;
        }
        const user = result.data.user;
        const username = getOrCreateUsername(user);
        if (nameElement) {
            nameElement.textContent = username;
        }
        ensureUsername(user)
            .then(function (savedUsername) {
                if (nameElement) {
                    nameElement.textContent = savedUsername;
                }
            })
            .catch(function (error) {
                console.error("Could not save the profile username:", error);
            });
    } catch (error) {
        console.error("Could not load the profile:", error);
        window.location.replace("login.html");
    }
}
async function logoutUser() {
    try {
        await supabaseClient.auth.signOut();
    } catch (error) {
        console.error("Could not sign out:", error);
    }
    window.location.replace("signup.html");
}