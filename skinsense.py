# SkinSense website generator
# Keep logo.png and device.png in the same folder as this file.
# This script creates index.html and style.css.

def make_image_tag(filename, class_name, alt_text):
    return (
        "<img class=\""
        + class_name
        + "\" src=\""
        + filename
        + "\" alt=\""
        + alt_text
        + "\">"
    )


def create_html():
    logo_tag = make_image_tag(
        "logo.png",
        "brand-logo",
        "SkinSense logo"
    )

    device_tag = make_image_tag(
        "device.png",
        "device-photo",
        "DermaSense skincare analysis device"
    )

    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SkinSense | Know Your Skin, Care Better</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="splash-screen" id="splash-screen">
    <div class="splash-content">
        <div class="splash-logo">
""" + logo_tag + """
        </div>
        <p class="eyebrow">SKINSENSE</p>
        <h1>Know Your Skin.</h1>
        <p>Care better with clearer insight.</p>
        <div class="loading-line"><span></span></div>
    </div>
</div>

<header class="site-header">
    <a class="brand" href="#home">
""" + logo_tag + """
    </a>

    <nav class="navigation">
        <a href="#home">Home</a>
        <a href="#product">Product</a>
        <a href="#how-it-works">How It Works</a>
        <a href="#science">Science</a>
        <a href="#insights">Insights</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
    </nav>

    <div class="account-links">
        <a href="login.html">Log In</a>
        <a class="signup-link" href="signup.html">Sign Up</a>
    </div>
</header>

<main>

<section class="hero-section" id="home">
    <div class="hero-copy">
        <p class="eyebrow">Affordable skincare technology</p>
        <h1>Know Your Skin,<br>Care Better.</h1>
        <p class="hero-tagline">We don't guess your skin. We measure it.</p>
        <p class="hero-description">
            DermaSense is a low-cost, IoT-enabled device that measures
            moisture, pH, and oiliness, then helps you understand which
            skincare ingredients may suit your skin.
        </p>

        <div class="hero-buttons">
            <a class="primary-button" href="#how-it-works">See How It Works</a>
            <a class="secondary-button" href="#waitlist">Join the Waitlist</a>
        </div>
    </div>

    <div class="hero-art">
        <p class="art-label">DERMASENSE / 01</p>
""" + device_tag + """
        <p class="art-caption">Measure. Understand. Care.</p>
        <span class="decorative-dot dot-one"></span>
        <span class="decorative-dot dot-two"></span>
        <span class="decorative-dot dot-three"></span>
    </div>
</section>

<section class="intro-strip">
    <div class="intro-number">01</div>
    <div>
        <p class="eyebrow">A clearer starting point</p>
        <h2>Skin insights without the guesswork.</h2>
    </div>
    <p>
        SkinSense is on a mission to make practical, science-backed skin
        analysis more affordable and understandable.
    </p>
</section>

<section class="section" id="product">
    <div class="section-heading">
        <p class="eyebrow">What DermaSense measures</p>
        <h2>Three readings. A more informed routine.</h2>
    </div>

    <div class="feature-grid">
        <article class="feature-card blue-card">
            <div class="feature-icon">◌</div>
            <p class="card-number">01 / MEASURE</p>
            <h3>Moisture</h3>
            <p>
                Capacitive sensing helps estimate hydration and gives you
                a starting point for understanding skin moisture.
            </p>
        </article>

        <article class="feature-card cream-card">
            <div class="feature-icon">✧</div>
            <p class="card-number">02 / MEASURE</p>
            <h3>pH Balance</h3>
            <p>
                A liquid probe reads an acid-alkaline value. The result is
                educational and is not a medical diagnosis.
            </p>
        </article>

        <article class="feature-card sage-card">
            <div class="feature-icon">☼</div>
            <p class="card-number">03 / MEASURE</p>
            <h3>Oiliness</h3>
            <p>
                Blotting paper and a light sensor estimate surface oil by
                comparing clean paper with a skin sample.
            </p>
        </article>
    </div>
</section>

<section class="product-panel">
    <div class="product-copy">
        <p class="eyebrow">Meet the device</p>
        <h2>Small device.<br>Clearer skin insights.</h2>
        <p>
            DermaSense brings together simple sensors, a compact display,
            and ingredient education to make skin analysis more approachable.
        </p>
        <a class="dark-button" href="#waitlist">Join the Waitlist</a>
    </div>

    <div class="spec-card">
        <div class="spec-top">
            <span>DERMASENSE</span>
            <span>TECHNICAL NOTES</span>
        </div>

        <div class="spec-list">
            <div><span>Controller</span><strong>ESP32</strong></div>
            <div><span>Moisture sensor</span><strong>YL-69</strong></div>
            <div><span>pH sensor</span><strong>PH-4502C</strong></div>
            <div><span>Light sensor</span><strong>BH1750</strong></div>
            <div><span>Display</span><strong>16x2 LCD</strong></div>
            <div><span>Estimated project cost</span><strong>About Rs. 2,500</strong></div>
        </div>

        <div class="box-note">
            <h3>What's in the box?</h3>
            <p>
                Planned contents include the DermaSense device, sensors,
                display, and a calibration guide. Final contents may change
                as the prototype develops.
            </p>
        </div>
    </div>
</section>

<section class="section" id="how-it-works">
    <div class="section-heading centered">
        <p class="eyebrow">The process</p>
        <h2>From measurement to meaning.</h2>
        <p>Four steps help you understand the readings and their limits.</p>
    </div>

    <div class="process-grid">
        <article class="process-card">
            <span>01</span>
            <div class="process-symbol">⌁</div>
            <h3>Calibrate</h3>
            <p>
                Prepare the sensors against known reference samples before
                taking measurements.
            </p>
        </article>

        <article class="process-card">
            <span>02</span>
            <div class="process-symbol">◉</div>
            <h3>Measure</h3>
            <p>
                Take moisture and pH readings, then use the paper-and-light
                method to estimate surface oil.
            </p>
        </article>

        <article class="process-card">
            <span>03</span>
            <div class="process-symbol">✦</div>
            <h3>See Results</h3>
            <p>
                Review each reading in plain language. One reading alone
                cannot identify or diagnose a skin condition.
            </p>
        </article>

        <article class="process-card">
            <span>04</span>
            <div class="process-symbol">♡</div>
            <h3>Explore Guidance</h3>
            <p>
                Use educational ingredient suggestions as a starting point
                for further research and professional advice when needed.
            </p>
        </article>
    </div>

    <div class="method-note">
        <p class="eyebrow">The oiliness reading</p>
        <h3>Why blotting paper and light?</h3>
        <p>
            The proposed method compares how light reflects from clean paper
            and paper after it contacts the skin. Oil can change the paper's
            appearance, and the BH1750 measures light levels. This is an
            estimate, not a clinical sebum test.
        </p>
    </div>
</section>

<section class="quote-section">
    <span class="quote-mark">“</span>
    <p>We don't guess your skin.<br>We measure it.</p>
    <span>SkinSense / DermaSense</span>
</section>

<section class="section" id="science">
    <div class="section-heading">
        <p class="eyebrow">Transparent by design</p>
        <h2>Science & Accuracy.</h2>
    </div>

    <div class="science-grid">
        <div class="science-content">
            <h3>Calibration plan</h3>
            <ul>
                <li>Moisture: compare dry-skin and wet-skin references.</li>
                <li>pH: use buffer references around pH 4.0 and 9.0.</li>
                <li>
                    Oiliness: compare clean paper with oil-saturated paper.
                </li>
            </ul>

            <h3>Why these readings?</h3>
            <p>
                Moisture, pH, and surface oil can provide context about how
                skin feels and behaves. They are only part of the picture.
                Readings can vary with placement, pressure, temperature,
                products, and calibration.
            </p>

            <h3>Research references</h3>
            <p>
                Research citations should be reviewed and added here before
                publication. Do not treat the prototype's measurements as
                clinically validated.
            </p>
        </div>

        <aside class="notice-card">
            <p class="eyebrow">Important note</p>
            <h3>A prototype, with limits.</h3>
            <p>
                DermaSense is intended for educational skin insights. It is
                not a clinical diagnostic device and does not replace
                professional dermatological advice.
            </p>
        </aside>
    </div>

    <div class="comparison-card">
        <h3>DermaSense and clinical devices</h3>
        <div class="comparison-row comparison-heading">
            <span></span>
            <span>DermaSense</span>
            <span>Clinical equipment</span>
        </div>
        <div class="comparison-row">
            <span>Purpose</span>
            <span>Educational prototype</span>
            <span>Used for specific clinical purposes</span>
        </div>
        <div class="comparison-row">
            <span>Interpretation</span>
            <span>General learning, not diagnosis</span>
            <span>Interpreted by qualified professionals</span>
        </div>
        <div class="comparison-row">
            <span>Validation</span>
            <span>Prototype testing is ongoing</span>
            <span>Depends on the device and its approved use</span>
        </div>
    </div>
</section>

<section class="section" id="insights">
    <div class="section-heading centered">
        <p class="eyebrow">Read your skin more clearly</p>
        <h2>Skin Insights.</h2>
        <p>
            Skin type patterns are educational descriptions, not diagnoses.
        </p>
    </div>

    <div class="skin-table">
        <div class="table-row table-header">
            <span>Skin pattern</span>
            <span>Possible reading pattern</span>
            <span>Educational focus</span>
        </div>

        <div class="table-row">
            <span>Oily</span>
            <span>Higher surface oil readings</span>
            <span>Consider lightweight, non-comedogenic products</span>
        </div>

        <div class="table-row">
            <span>Dry</span>
            <span>Lower moisture readings</span>
            <span>Explore hydration and barrier-support ingredients</span>
        </div>

        <div class="table-row">
            <span>Combination</span>
            <span>Readings vary across facial areas</span>
            <span>Consider that different areas may have different needs</span>
        </div>

        <div class="table-row">
            <span>Normal</span>
            <span>Readings appear relatively balanced</span>
            <span>Maintain a simple routine that suits your skin</span>
        </div>
    </div>

    <div class="insight-note">
        <h3>What your readings mean</h3>
        <p>
            A single measurement cannot determine your skin type or
            sensitivity. pH readings alone do not prove that skin is
            sensitive. Use repeated readings as general context, and seek
            professional advice about persistent symptoms.
        </p>
    </div>

    <div class="ingredient-grid">
        <article>
            <h3>For dry-feeling skin</h3>
            <p>Explore humectants, ceramides, and gentle moisturizers.</p>
        </article>
        <article>
            <h3>For oily-feeling skin</h3>
            <p>Explore lightweight hydration and non-comedogenic formulas.</p>
        </article>
        <article>
            <h3>For easily irritated skin</h3>
            <p>Explore gentle, fragrance-free options and patch testing.</p>
        </article>
    </div>
</section>

<section class="about-section" id="about">
    <div class="about-art">
        <div class="stem"></div>
        <div class="leaf leaf-one"></div>
        <div class="leaf leaf-two"></div>
        <div class="leaf leaf-three"></div>
        <div class="about-circle">SS</div>
    </div>

    <div class="about-copy">
        <p class="eyebrow">Our story</p>
        <h2>Science should feel accessible.</h2>
        <p>
            SkinSense was created around a simple idea: make practical,
            science-backed skin analysis easier to understand and more
            affordable.
        </p>
        <p>
            We want to build with care, explain what the device can and
            cannot tell you, and keep improving through testing.
        </p>

        <div class="values">
            <span>Science-backed</span>
            <span>Accessible</span>
            <span>Transparent</span>
        </div>

        <div class="roadmap">
            <h3>What's ahead</h3>
            <p>Prototype refinement, calibration tests, user feedback, and clearer skin education.</p>
        </div>
    </div>
</section>

<section class="form-panel" id="contact">
    <div>
        <p class="eyebrow">Contact & Support</p>
        <h2>Questions?<br>Let's talk.</h2>
        <p>
            Ask about setup, calibration, troubleshooting, shipping, returns,
            or the DermaSense project.
        </p>
        <p class="placeholder-note">
            Replace this note with your real support email and response time
            before publishing.
        </p>
    </div>

    <form onsubmit="return false;">
        <label for="contact-name">Name</label>
        <input id="contact-name" type="text" placeholder="Your name">

        <label for="contact-email">Email</label>
        <input id="contact-email" type="email" placeholder="you@example.com">

        <label for="contact-message">Message</label>
        <textarea id="contact-message" placeholder="How can we help?"></textarea>

        <button class="dark-button" type="submit">Send Message</button>
    </form>
</section>

<section class="faq-section">
    <p class="eyebrow">A few helpful answers</p>
    <h2>Frequently asked questions</h2>

    <details>
        <summary>Does DermaSense replace a dermatologist?</summary>
        <p>No. It is an educational prototype, not a diagnostic device.</p>
    </details>

    <details>
        <summary>Will I need to calibrate the device?</summary>
        <p>
            The prototype is designed around calibration references. Follow
            the final product instructions when they are available.
        </p>
    </details>

    <details>
        <summary>Is shipping or returns information available?</summary>
        <p>
            Add confirmed shipping and return details here before accepting
            orders.
        </p>
    </details>
</section>

<section class="waitlist-panel" id="waitlist">
    <div>
        <p class="eyebrow">Early access</p>
        <h2>Be the First to Try DermaSense.</h2>
        <p>
            Join the waitlist to follow the journey of affordable,
            practical skin analysis.
        </p>
    </div>

    <form onsubmit="showWaitlistMessage(); return false;">
        <label for="waitlist-name">Name</label>
        <input id="waitlist-name" type="text" placeholder="Your name" required>

        <label for="waitlist-email">Email</label>
        <input id="waitlist-email" type="email" placeholder="you@example.com" required>

        <label for="waitlist-skin">Optional skin type</label>
        <select id="waitlist-skin">
            <option>Prefer not to say</option>
            <option>Oily</option>
            <option>Dry</option>
            <option>Combination</option>
            <option>Normal</option>
        </select>

        <button class="light-button" type="submit">Join the Waitlist</button>
        <p id="waitlist-confirmation" class="confirmation"></p>
    </form>
</section>

</main>

<footer class="site-footer">
    <div class="footer-logo">
""" + logo_tag + """
    </div>

    <div>
        <p>We don't guess your skin. We measure it.</p>
        <p class="footer-small">
            DermaSense provides educational guidance and does not replace
            professional dermatological advice.
        </p>
    </div>

    <div class="footer-links">
        <a href="#home">Home</a>
        <a href="#product">Product</a>
        <a href="login.html">Log In</a>
        <a href="signup.html">Sign Up</a>
    </div>

    <p class="copyright">Copyright 2026 SkinSense</p>
</footer>

<script>
window.addEventListener("load", function () {
    var splash = document.getElementById("splash-screen");

    setTimeout(function () {
        if (splash) {
            splash.classList.add("splash-hidden");
        }
    }, 1600);
});

function showWaitlistMessage() {
    var message = document.getElementById("waitlist-confirmation");

    if (message) {
        message.innerHTML =
            "Thank you. Your details have been entered on this page.";
    }
}
</script>

</body>
</html>
"""

    file = open("index.html", "w", encoding="utf-8")
    file.write(html)
    file.close()

    print("index.html created.")


def create_css():
    css = """
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    scroll-behavior: smooth;
}

body {
    background:
        radial-gradient(circle at 12% 8%, rgba(255,255,255,.75), transparent 27%),
        radial-gradient(circle at 90% 77%, rgba(226,246,222,.7), transparent 30%),
        linear-gradient(135deg, #e5f6f0, #d2eee8 48%, #eff1e2);
    color: #234b49;
    font-family: Arial, sans-serif;
    line-height: 1.65;
}

a {
    color: inherit;
    text-decoration: none;
}

.splash-screen {
    align-items: center;
    background:
        radial-gradient(circle at 20% 20%, rgba(255,255,255,.8), transparent 28%),
        linear-gradient(135deg, #e5f6f0, #c6eae1 55%, #eff1e2);
    display: flex;
    height: 100vh;
    justify-content: center;
    left: 0;
    position: fixed;
    top: 0;
    transition: opacity .8s ease, visibility .8s ease;
    width: 100%;
    z-index: 9999;
}

.splash-hidden {
    opacity: 0;
    visibility: hidden;
}

.splash-content {
    text-align: center;
}

.splash-logo {
    margin-bottom: 20px;
}

.splash-logo .brand-logo {
    max-height: 85px;
    max-width: 180px;
}

.splash-content h1 {
    font-family: Georgia, serif;
    font-size: 48px;
    font-weight: normal;
    line-height: 1.15;
    margin-bottom: 10px;
}

.loading-line {
    background: rgba(255,255,255,.6);
    border-radius: 20px;
    height: 5px;
    margin: 28px auto 0;
    overflow: hidden;
    width: 170px;
}

.loading-line span {
    animation: load-bar 1.6s ease-in-out;
    background: #70aaa1;
    display: block;
    height: 100%;
    width: 100%;
}

@keyframes load-bar {
    from { transform: translateX(-100%); }
    to { transform: translateX(0); }
}

.site-header {
    align-items: center;
    display: flex;
    gap: 18px;
    justify-content: space-between;
    margin: auto;
    max-width: 1320px;
    padding: 22px 35px;
}

.brand-logo {
    background: transparent;
    display: block;
    max-height: 56px;
    max-width: 145px;
    object-fit: contain;
}

.navigation,
.account-links {
    align-items: center;
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
}

.navigation a,
.account-links a {
    border: 1px solid rgba(35,75,73,.25);
    border-radius: 28px;
    font-size: 11px;
    padding: 8px 12px;
    transition: .2s;
    white-space: nowrap;
}

.navigation a:hover,
.account-links a:hover {
    background: rgba(255,255,255,.55);
    transform: translateY(-2px);
}

.signup-link {
    background: rgba(255,255,255,.55);
}

main {
    margin: auto;
    max-width: 1320px;
    padding: 25px 35px 90px;
}

.hero-section {
    align-items: center;
    display: grid;
    gap: 65px;
    grid-template-columns: .95fr 1.05fr;
    min-height: 650px;
}

.eyebrow {
    color: #397e78;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 2px;
    margin-bottom: 16px;
    text-transform: uppercase;
}

.hero-copy h1 {
    font-family: Georgia, serif;
    font-size: 70px;
    font-weight: normal;
    line-height: 1.04;
    margin-bottom: 23px;
}

.hero-tagline {
    color: #397e78;
    font-family: Georgia, serif;
    font-size: 23px;
    margin-bottom: 15px;
}

.hero-description {
    max-width: 540px;
}

.hero-buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 25px;
}

.primary-button,
.secondary-button,
.dark-button,
.light-button {
    border: 0;
    border-radius: 30px;
    cursor: pointer;
    display: inline-block;
    font-size: 13px;
    font-weight: bold;
    padding: 13px 20px;
    transition: .2s;
}

.primary-button {
    background: rgba(255,255,255,.82);
    color: #397e78;
}

.secondary-button {
    background: rgba(73,145,137,.8);
    color: white;
}

.primary-button:hover,
.secondary-button:hover,
.dark-button:hover,
.light-button:hover {
    transform: translateY(-3px);
}

.hero-art {
    align-items: center;
    background:
        radial-gradient(circle at 72% 18%, rgba(255,255,255,.48), transparent 24%),
        radial-gradient(circle at 20% 80%, rgba(235,248,222,.3), transparent 30%),
        linear-gradient(140deg, rgba(124,197,186,.72), rgba(100,165,164,.66));
    border: 1px solid rgba(255,255,255,.42);
    border-radius: 36px;
    box-shadow: 0 24px 55px rgba(35,75,73,.1);
    display: flex;
    justify-content: center;
    min-height: 510px;
    overflow: hidden;
    position: relative;
}

.art-label {
    color: white;
    font-size: 11px;
    font-weight: bold;
    left: 28px;
    letter-spacing: 2px;
    position: absolute;
    top: 25px;
}

.device-photo {
    display: block;
    max-height: 72%;
    max-width: 65%;
    object-fit: contain;
    position: relative;
    z-index: 2;
    filter: drop-shadow(0 18px 22px rgba(35,75,73,.2));
}

.art-caption {
    bottom: 24px;
    color: white;
    font-family: Georgia, serif;
    font-size: 21px;
    position: absolute;
    right: 28px;
}

.decorative-dot {
    background: rgba(255,255,255,.75);
    border-radius: 50%;
    height: 9px;
    position: absolute;
    width: 9px;
}

.dot-one { right: 18%; top: 24%; }
.dot-two { left: 16%; top: 50%; }
.dot-three { bottom: 23%; left: 28%; }

.intro-strip {
    align-items: center;
    background: rgba(255,255,255,.34);
    border: 1px solid rgba(35,75,73,.1);
    border-radius: 26px;
    display: grid;
    gap: 25px;
    grid-template-columns: 65px 1fr 1fr;
    margin: 0 auto 105px;
    max-width: 1120px;
    padding: 30px;
}

.intro-number {
    color: #397e78;
    font-family: Georgia, serif;
    font-size: 34px;
}

.intro-strip h2,
.section-heading h2,
.product-copy h2,
.about-copy h2,
.form-panel h2,
.waitlist-panel h2 {
    font-family: Georgia, serif;
    font-size: 44px;
    font-weight: normal;
    line-height: 1.12;
}

.section {
    margin: 0 auto 115px;
    max-width: 1120px;
}

.section-heading {
    margin-bottom: 35px;
    max-width: 680px;
}

.centered {
    margin-left: auto;
    margin-right: auto;
    text-align: center;
}

.feature-grid {
    display: grid;
    gap: 18px;
    grid-template-columns: repeat(3, 1fr);
}

.feature-card {
    border: 1px solid rgba(35,75,73,.09);
    border-radius: 27px;
    min-height: 300px;
    padding: 28px;
    transition: .2s;
}

.feature-card:hover,
.process-card:hover,
.ingredient-grid article:hover {
    box-shadow: 0 15px 32px rgba(35,75,73,.1);
    transform: translateY(-5px);
}

.blue-card {
    background: linear-gradient(145deg, rgba(255,255,255,.55), transparent), #c4e4e5;
}

.cream-card {
    background: linear-gradient(145deg, rgba(255,255,255,.7), transparent), #f5f0e2;
}

.sage-card {
    background: linear-gradient(145deg, rgba(255,255,255,.5), transparent), #d3e3c9;
}

.feature-icon {
    color: #4c928a;
    font-size: 52px;
    margin-bottom: 25px;
}

.card-number {
    color: #397e78;
    font-size: 10px;
    font-weight: bold;
    letter-spacing: 1.5px;
}

.feature-card h3,
.process-card h3,
.box-note h3,
.method-note h3,
.notice-card h3,
.comparison-card h3,
.insight-note h3,
.ingredient-grid h3,
.roadmap h3 {
    font-family: Georgia, serif;
    font-size: 25px;
    font-weight: normal;
    margin: 8px 0 10px;
}

.product-panel,
.form-panel {
    align-items: center;
    background:
        radial-gradient(circle at 85% 12%, rgba(255,255,255,.75), transparent 26%),
        linear-gradient(135deg, #f8f3e7, #e8f0e2);
    border-radius: 34px;
    display: grid;
    gap: 55px;
    grid-template-columns: 1fr 1fr;
    margin: 0 auto 115px;
    max-width: 1120px;
    padding: 55px;
}

.product-copy p {
    max-width: 520px;
}

.dark-button {
    background: #315f5b;
    color: white;
    margin-top: 16px;
}

.spec-card {
    background: rgba(255,255,255,.75);
    border: 1px solid rgba(255,255,255,.8);
    border-radius: 24px;
    padding: 25px;
}

.spec-top {
    display: flex;
    font-size: 10px;
    font-weight: bold;
    justify-content: space-between;
    letter-spacing: 1px;
}

.spec-list {
    display: grid;
    gap: 13px;
    grid-template-columns: 1fr 1fr;
    margin-top: 23px;
}

.spec-list div {
    border-bottom: 1px solid rgba(35,75,73,.13);
    display: flex;
    flex-direction: column;
    padding-bottom: 9px;
}

.spec-list span {
    color: #54817c;
    font-size: 11px;
}

.spec-list strong {
    font-size: 14px;
}

.box-note {
    border-top: 1px solid rgba(35,75,73,.14);
    margin-top: 24px;
    padding-top: 12px;
}

.process-grid {
    display: grid;
    gap: 16px;
    grid-template-columns: repeat(4, 1fr);
}

.process-card {
    background: rgba(255,255,255,.4);
    border: 1px solid rgba(35,75,73,.1);
    border-radius: 23px;
    min-height: 270px;
    padding: 23px;
    transition: .2s;
}

.process-card > span {
    color: #397e78;
    font-size: 11px;
    font-weight: bold;
}

.process-symbol {
    color: #55968d;
    font-size: 42px;
    margin: 20px 0;
}

.method-note,
.insight-note {
    background: rgba(255,255,255,.42);
    border-radius: 23px;
    margin-top: 25px;
    padding: 28px;
}

.quote-section {
    background:
        radial-gradient(circle at 20% 15%, rgba(255,255,255,.3), transparent 26%),
        linear-gradient(135deg, #89c8bd, #75b3b0);
    border-radius: 32px;
    color: white;
    margin: 0 auto 115px;
    max-width: 1120px;
    padding: 75px 30px;
    text-align: center;
}

.quote-mark {
    font-family: Georgia, serif;
    font-size: 68px;
}

.quote-section p {
    font-family: Georgia, serif;
    font-size: 40px;
    line-height: 1.2;
    margin: 15px auto 22px;
}

.science-grid {
    display: grid;
    gap: 35px;
    grid-template-columns: 1.2fr .8fr;
}

.science-content h3 {
    font-family: Georgia, serif;
    font-size: 25px;
    font-weight: normal;
    margin: 22px 0 10px;
}

.science-content ul {
    padding-left: 22px;
}

.notice-card {
    align-self: start;
    background: rgba(255,249,234,.8);
    border: 1px solid rgba(255,255,255,.65);
    border-radius: 25px;
    padding: 30px;
}

.comparison-card {
    background: rgba(255,255,255,.4);
    border-radius: 22px;
    margin-top: 30px;
    overflow: hidden;
    padding-top: 15px;
}

.comparison-card h3 {
    padding: 0 22px;
}

.comparison-row,
.table-row {
    display: grid;
    gap: 15px;
    grid-template-columns: 1fr 1fr 1.2fr;
    padding: 16px 22px;
}

.comparison-row:not(:last-child),
.table-row:not(:last-child) {
    border-bottom: 1px solid rgba(35,75,73,.12);
}

.comparison-heading,
.table-header {
    background: rgba(91,169,164,.67);
    color: white;
    font-weight: bold;
}

.skin-table {
    background: rgba(255,255,255,.42);
    border-radius: 20px;
    overflow: hidden;
}

.ingredient-grid {
    display: grid;
    gap: 16px;
    grid-template-columns: repeat(3, 1fr);
    margin-top: 22px;
}

.ingredient-grid article {
    background: rgba(255,255,255,.55);
    border: 1px solid rgba(35,75,73,.08);
    border-radius: 20px;
    padding: 22px;
    transition: .2s;
}

.about-section {
    align-items: center;
    display: grid;
    gap: 65px;
    grid-template-columns: 1fr 1fr;
    margin: 0 auto 115px;
    max-width: 1120px;
}

.about-art {
    background:
        radial-gradient(circle at 50% 50%, rgba(255,255,255,.6), transparent 38%),
        linear-gradient(135deg, #f4efdf, #dce9d3);
    border-radius: 48% 52% 45% 55%;
    height: 370px;
    position: relative;
}

.about-circle {
    align-items: center;
    background: rgba(120,177,166,.85);
    border: 10px solid rgba(255,255,255,.8);
    border-radius: 50%;
    color: white;
    display: flex;
    font-family: Georgia, serif;
    font-size: 46px;
    height: 140px;
    justify-content: center;
    left: 36%;
    position: absolute;
    top: 33%;
    width: 140px;
}

.stem {
    background: #7d9f73;
    height: 205px;
    left: 52%;
    position: absolute;
    top: 22%;
    transform: rotate(12deg);
    width: 4px;
}

.leaf {
    background: #a8c59a;
    border-radius: 100% 0 100% 0;
    height: 58px;
    position: absolute;
    width: 36px;
}

.leaf-one { left: 42%; top: 28%; transform: rotate(-35deg); }
.leaf-two { left: 54%; top: 42%; transform: rotate(35deg); }
.leaf-three { left: 43%; top: 57%; transform: rotate(-35deg); }

.values {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 20px;
}

.values span {
    border: 1px solid #6a9b91;
    border-radius: 22px;
    color: #397e78;
    font-size: 11px;
    padding: 7px 12px;
}

.roadmap {
    margin-top: 22px;
}

.form-panel {
    margin-bottom: 35px;
}

.form-panel form,
.waitlist-panel form {
    display: flex;
    flex-direction: column;
}

.form-panel label,
.waitlist-panel label {
    font-size: 12px;
    font-weight: bold;
    margin-top: 13px;
}

.form-panel input,
.form-panel textarea,
.waitlist-panel input,
.waitlist-panel select {
    background: rgba(255,255,255,.85);
    border: 1px solid rgba(35,75,73,.17);
    border-radius: 11px;
    font-family: Arial, sans-serif;
    font-size: 14px;
    margin-top: 6px;
    padding: 12px;
}

.form-panel textarea {
    min-height: 110px;
}

.placeholder-note {
    color: #687e78;
    font-size: 12px;
    margin-top: 20px;
}

.faq-section {
    margin: 0 auto 85px;
    max-width: 1120px;
}

.faq-section h2 {
    font-family: Georgia, serif;
    font-size: 37px;
    font-weight: normal;
    margin-bottom: 20px;
}

.faq-section details {
    background: rgba(255,255,255,.42);
    border-radius: 14px;
    margin: 10px 0;
    padding: 16px 20px;
}

.faq-section summary {
    cursor: pointer;
    font-weight: bold;
}

.faq-section details p {
    margin-top: 10px;
}

.waitlist-panel {
    align-items: center;
    background:
        radial-gradient(circle at 80% 15%, rgba(255,255,255,.3), transparent 25%),
        linear-gradient(135deg, #85c5ba, #75b2ad);
    border-radius: 32px;
    color: white;
    display: grid;
    gap: 50px;
    grid-template-columns: 1fr 1fr;
    margin: 0 auto 80px;
    max-width: 1120px;
    padding: 50px;
}

.waitlist-panel h2 {
    color: white;
}

.waitlist-panel .eyebrow {
    color: #f0fffa;
}

.light-button {
    background: rgba(255,255,255,.9);
    color: #397e78;
    margin-top: 20px;
}

.confirmation {
    margin-top: 15px;
}

.site-footer {
    align-items: center;
    background: rgba(42,83,79,.92);
    color: white;
    display: grid;
    gap: 25px;
    grid-template-columns: 150px 1fr 1fr;
    padding: 40px max(30px, calc((100% - 1200px) / 2));
}

.footer-logo .brand-logo {
    max-height: 58px;
    max-width: 140px;
}

.footer-small {
    color: #d0e6e0;
    font-size: 11px;
    margin-top: 8px;
    max-width: 450px;
}

.footer-links {
    display: flex;
    flex-wrap: wrap;
    gap: 9px;
    justify-content: flex-end;
}

.footer-links a {
    border: 1px solid rgba(255,255,255,.4);
    border-radius: 22px;
    font-size: 11px;
    padding: 7px 11px;
}

.copyright {
    color: #d0e6e0;
    font-size: 10px;
    grid-column: 1 / 4;
    margin-top: 12px;
    text-align: center;
}

@media screen and (max-width: 1000px) {
    .site-header {
        align-items: flex-start;
        flex-wrap: wrap;
    }

    .navigation {
        order: 3;
        width: 100%;
    }

    .hero-section,
    .product-panel,
    .science-grid,
    .about-section,
    .form-panel,
    .waitlist-panel {
        grid-template-columns: 1fr;
    }

    .process-grid {
        grid-template-columns: 1fr 1fr;
    }
}

@media screen and (max-width: 650px) {
    .site-header {
        padding: 18px;
    }

    main {
        padding: 20px 18px 60px;
    }

    .hero-section {
        gap: 35px;
        min-height: auto;
        padding: 45px 0;
    }

    .hero-copy h1 {
        font-size: 48px;
    }

    .hero-tagline {
        font-size: 20px;
    }

    .hero-art {
        min-height: 390px;
    }

    .device-photo {
        max-height: 68%;
        max-width: 72%;
    }

    .intro-strip {
        grid-template-columns: 1fr;
        margin-bottom: 75px;
        padding: 23px;
    }

    .intro-strip h2,
    .section-heading h2,
    .product-copy h2,
    .about-copy h2,
    .form-panel h2,
    .waitlist-panel h2 {
        font-size: 35px;
    }

    .feature-grid,
    .process-grid,
    .ingredient-grid {
        grid-template-columns: 1fr;
    }

    .product-panel,
    .form-panel,
    .waitlist-panel {
        padding: 26px;
    }

    .quote-section p {
        font-size: 30px;
    }

    .comparison-row,
    .table-row {
        font-size: 11px;
        gap: 8px;
        padding: 13px 10px;
    }

    .site-footer {
        display: block;
        padding: 35px 22px;
    }

    .footer-links {
        justify-content: flex-start;
        margin-top: 20px;
    }

    .copyright {
        margin-top: 25px;
        text-align: left;
    }
}
"""

    file = open("style.css", "w", encoding="utf-8")
    file.write(css)
    file.close()

    print("style.css created.")


def check_image_files():
    filenames = ["logo.png", "device.png"]

    for filename in filenames:
        try:
            file = open(filename, "rb")
            file.close()
            print(filename + " found.")
        except:
            print("Please put " + filename + " in this folder.")


def create_website():
    check_image_files()
    create_html()
    create_css()

    print("")
    print("SkinSense website created.")
    print("Upload index.html, style.css, logo.png, and device.png to GitHub.")
    print("The waitlist and contact forms are visual only and do not save entries.")


create_website()