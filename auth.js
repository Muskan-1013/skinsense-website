const SUPABASE_URL =
    "https://ezztfywicvrajevxngjc.supabase.co";

const SUPABASE_KEY =
    "sb_publishable_EZ-ZHcOnSEWQVyEmKAMeXg_TyjygF1j";

const supabaseClient = window.supabase.createClient(
    SUPABASE_URL,
    SUPABASE_KEY
);


function getSiteUrl() {
    return window.location.origin;
}


async function signUpUser() {
    const email = document.getElementById("signup-email").value;
    const password = document.getElementById("signup-password").value;
    const message = document.getElementById("signup-message");

    const result = await supabaseClient.auth.signUp({
        email: email,
        password: password,
        options: {
            emailRedirectTo: getSiteUrl() + "/account.html"
        }
    });

    if (result.error) {
        message.innerHTML = result.error.message;
        return;
    }

    message.innerHTML =
        "Account created. Check your email to verify your account.";
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
        message.innerHTML = result.error.message;
        return;
    }

    window.location.href = "account.html";
}


async function loginWithGoogle() {
    const result = await supabaseClient.auth.signInWithOAuth({
        provider: "google",
        options: {
            redirectTo: getSiteUrl() + "/account.html"
        }
    });

    if (result.error) {
        alert(result.error.message);
    }
}


async function sendPasswordReset() {
    const email = document.getElementById("reset-email").value;
    const message = document.getElementById("reset-message");

    const result =
        await supabaseClient.auth.resetPasswordForEmail(
            email,
            {
                redirectTo: getSiteUrl() + "/reset-password.html"
            }
        );

    if (result.error) {
        message.innerHTML = result.error.message;
        return;
    }

    message.innerHTML =
        "If this email exists, a password reset link has been sent.";
}


async function updatePassword() {
    const password =
        document.getElementById("new-password").value;

    const message =
        document.getElementById("update-password-message");

    const result =
        await supabaseClient.auth.updateUser({
            password: password
        });

    if (result.error) {
        message.innerHTML = result.error.message;
        return;
    }

    message.innerHTML =
        "Your password has been updated successfully.";
}


async function loadAccount() {
    const result =
        await supabaseClient.auth.getUser();

    if (
        result.error ||
        result.data.user === null
    ) {
        window.location.href = "login.html";
        return;
    }

    const emailElement =
        document.getElementById("account-email");

    if (emailElement) {
        emailElement.innerHTML =
            result.data.user.email;
    }
}


async function logoutUser() {
    await supabaseClient.auth.signOut();

    window.location.href = "login.html";
}