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
    const number = Math.floor(1000 + Math.random() * 9000);

    return prefix + "_" + number;
}

async function ensureUsername(user) {
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

    if (!metadata.username) {
        const result = await supabaseClient.auth.updateUser({
            data: { username: username }
        });

        if (
            !result.error &&
            result.data.user &&
            result.data.user.user_metadata.username
        ) {
            username = result.data.user.user_metadata.username;
        }
    }

    try {
        localStorage.setItem(storageKey, username);
    } catch (error) {
        // Supabase user metadata remains the saved username when available.
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

async function startHomePage() {
    const result = await supabaseClient.auth.getSession();

    if (result.error || !result.data.session) {
        window.location.replace("signup.html");
        return;
    }

    const username = await ensureUsername(result.data.session.user);
    showHomeProfile(username);

    const splash = document.getElementById("splash-screen");

    window.setTimeout(function () {
        if (splash) {
            splash.classList.add("splash-hidden");
        }

        document.body.classList.remove("auth-checking");
    }, 1600);

    supabaseClient.auth.onAuthStateChange(function (event, session) {
        if (event === "SIGNED_OUT") {
            window.location.replace("signup.html");
            return;
        }

        if (session && session.user.user_metadata.username) {
            showHomeProfile(session.user.user_metadata.username);
        }
    });
}

async function redirectIfLoggedIn() {
    const result = await supabaseClient.auth.getSession();

    if (!result.error && result.data.session) {
        window.location.replace("index.html");
    }
}

async function signUpUser() {
    const email = document.getElementById("signup-email").value;
    const password = document.getElementById("signup-password").value;
    const message = document.getElementById("signup-message");
    const username = makeUsername(email);

    const result = await supabaseClient.auth.signUp({
        email: email,
        password: password,
        options: {
            data: { username: username },
            emailRedirectTo: window.location.origin + "/index.html"
        }
    });

    if (result.error) {
        message.textContent = result.error.message;
        return;
    }

    if (result.data.session && result.data.user) {
        await ensureUsername(result.data.user);
        window.location.replace("index.html");
        return;
    }

    message.textContent =
        "Account created. Check your email to verify it, then return to SkinSense.";
}

async function loginUser() {
    const email = document.getElementById("login-email").value;
    const password = document.getElementById("login-password").value;
    const message = document.getElementById("login-message");

    const result = await supabaseClient.auth.signInWithPassword({
        email: email,
        password: password
    });

    if (result.error) {
        message.textContent = result.error.message;
        return;
    }

    await ensureUsername(result.data.user);
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
        alert(result.error.message);
    }
}

async function sendPasswordReset() {
    const email = document.getElementById("reset-email").value;
    const message = document.getElementById("reset-message");

    const result = await supabaseClient.auth.resetPasswordForEmail(
        email,
        {
            redirectTo: window.location.origin + "/reset-password.html"
        }
    );

    if (result.error) {
        message.textContent = result.error.message;
        return;
    }

    message.textContent =
        "If the email is registered, a password reset link has been sent.";
}

async function updatePassword() {
    const password = document.getElementById("new-password").value;
    const message = document.getElementById("update-password-message");

    const result = await supabaseClient.auth.updateUser({
        password: password
    });

    if (result.error) {
        message.textContent = result.error.message;
        return;
    }

    message.textContent = "Your password has been updated.";
}

async function loadAccount() {
    const result = await supabaseClient.auth.getUser();

    if (result.error || !result.data.user) {
        window.location.replace("signup.html");
        return;
    }

    const username = await ensureUsername(result.data.user);
    const nameElement = document.getElementById("account-username");

    if (nameElement) {
        nameElement.textContent = username;
    }
}

async function logoutUser() {
    await supabaseClient.auth.signOut();
    window.location.replace("signup.html");
}