# SkinSense website generator
# Keep this file as skinsense.py
# Keep logo.png in the same folder

def create_logo_tag():
    start = chr(60) + "img "
    details = (
        'class="brand-logo" '
        'src="logo.png" '
        'alt="SkinSense logo"'
    )
    end = chr(62)

    return start + details + end


def create_html():
    logo_tag = create_logo_tag()

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

        <p class="splash-label">SKINSENSE</p>
        <h1>Know Your Skin.</h1>
        <p>Care better with clearer insight.</p>

        <div class="loading-line">
            <span></span>
        </div>
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

    <a class="header-button" href="#waitlist">
        Join Waitlist
    </a>

</header>


<main>

<section class="hero-section" id="home">

    <div class="hero-copy">
        <p class="eyebrow">Affordable skincare technology</p>

        <h1>
            Know Your Skin,
            <br>
            Care Better.
        </h1>

        <p class="hero-tagline">
            We don't guess your skin. We measure it.
        </p>

        <p class="hero-description">
            DermaSense is a low-cost, IoT-enabled device that measures
            moisture, pH, and oiliness, then helps you understand which
            skincare ingredients your skin may need.
        </p>

        <div class="hero-buttons">
            <a class="primary-button" href="#how-it-works">
                See How It Works
            </a>

            <a class="secondary-button" href="#waitlist">
                Join the Waitlist
            </a>
        </div>
    </div>

    <div class="hero-art">
        <p class="art-label">DERMASENSE</p>

        <div class="floating-dot dot-one"></div>
        <div class="floating-dot dot-two"></div>
        <div class="floating-dot dot-three"></div>

        <div class="device">
            <div class="device-lights">
                <span></span>
                <span></span>
                <span></span>
            </div>

            <div class="device-screen">
                <small>SKIN</small>
                <strong>INSIGHT</strong>
            </div>

            <div class="device-buttons">
                <span></span>
                <span></span>
            </div>

            <div class="sensor">
                <span></span>
            </div>
        </div>

        <div class="face-art">
            <span class="eye eye-left"></span>
            <span class="eye eye-right"></span>
            <span class="nose"></span>
            <span class="mouth"></span>
        </div>

        <p class="art-caption">
            Measure. Understand. Care.
        </p>
    </div>

</section>


<section class="intro-strip">
    <div class="intro-number">01</div>

    <div>
        <p class="eyebrow">A clearer starting point</p>
        <h2>Skin insights without the guesswork.</h2>
    </div>

    <p>
        SkinSense combines accessible electronics with simple explanations
        so skincare feels more personal, practical, and transparent.
    </p>
</section>


<section class="section" id="product">

    <div class="section-heading">
        <p class="eyebrow">Three simple readings</p>
        <h2>Understand what your skin is telling you.</h2>
    </div>

    <div class="feature-grid">

        <article class="feature-card blue-card">
            <div class="feature-icon">◌</div>
            <p class="card-number">01</p>
            <h3>Moisture</h3>
            <p>
                Capacitive sensing helps estimate hydration levels and gives
                you a clearer starting point for your routine.
            </p>
        </article>

        <article class="feature-card cream-card">
            <div class="feature-icon">✧</div>
            <p class="card-number">02</p>
            <h3>pH Balance</h3>
            <p>
                A liquid probe reads the acid-alkaline state of your skin
                and helps explain what the result may mean.
            </p>
        </article>

        <article class="feature-card sage-card">
            <div class="feature-icon">☼</div>
            <p class="card-number">03</p>
            <h3>Oiliness</h3>
            <p>
                Blotting paper and light sensing estimate surface sebum
                in an accessible, educational way.
            </p>
        </article>

    </div>

</section>


<section class="product-panel">

    <div class="product-copy">
        <p class="eyebrow">Meet the device</p>

        <h2>Small device.<br>Clearer skin insights.</h2>

        <p>
            DermaSense brings together simple sensors, a compact interface,
            and ingredient education to make skin analysis more approachable.
        </p>

        <a class="dark-button" href="#waitlist">
            Be First to Try It
        </a>
    </div>

    <div class="spec-card">
        <div class="spec-top">
            <span>DERMASENSE</span>
            <span>01 / 06</span>
        </div>

        <div class="mini-device">
            <div class="mini-screen">READY</div>
            <div class="mini-sensor"></div>
        </div>

        <div class="spec-list">
            <div>
                <span>Controller</span>
                <strong>ESP32</strong>
            </div>

            <div>
                <span>Moisture</span>
                <strong>YL-69</strong>
            </div>

            <div>
                <span>pH Sensor</span>
                <strong>PH-4502C</strong>
            </div>

            <div>
                <span>Light Sensor</span>
                <strong>BH1750</strong>
            </div>

            <div>
                <span>Display</span>
                <strong>16x2 LCD</strong>
            </div>

            <div>
                <span>Estimated Cost</span>
                <strong>Rs. 2,500</strong>
            </div>
        </div>
    </div>

</section>


<section class="section" id="how-it-works">

    <div class="section-heading centered">
        <p class="eyebrow">The process</p>
        <h2>From measurement to meaning.</h2>
        <p>
            Four simple steps help turn readings into a better understanding
            of your skin.
        </p>
    </div>

    <div class="process-grid">

        <div class="process-card">
            <span>01</span>
            <div class="process-symbol">⌁</div>
            <h3>Calibrate</h3>
            <p>
                Prepare the sensors using known dry, wet, pH, clean-paper,
                and oil-paper references.
            </p>
        </div>

        <div class="process-card">
            <span>02</span>
            <div class="process-symbol">◉</div>
            <h3>Measure</h3>
            <p>
                Place the device on your skin and collect moisture, pH,
                and oiliness readings.
            </p>
        </div>

        <div class="process-card">
            <span>03</span>
            <div class="process-symbol">✦</div>
            <h3>See Results</h3>
            <p>
                Review the readings in simple language instead of confusing
                technical numbers.
            </p>
        </div>

        <div class="process-card">
            <span>04</span>
            <div class="process-symbol">♡</div>
            <h3>Get Guidance</h3>
            <p>
                Explore educational ingredient suggestions based on your
                overall skin pattern.
            </p>
        </div>

    </div>

</section>


<section class="quote-section">
    <div class="quote-mark">“</div>

    <p>
        We don't guess your skin.<br>
        We measure it.
    </p>

    <span>SkinSense / DermaSense</span>
</section>


<section class="section" id="science">

    <div class="section-heading">
        <p class="eyebrow">Transparent by design</p>
        <h2>Science & Accuracy.</h2>
    </div>

    <div class="science-grid">

        <div class="science-content">
            <h3>Why these readings matter</h3>

            <p>
                Moisture can affect comfort and the appearance of dryness.
                pH provides context about the skin barrier and cleansing
                routine. Oiliness can help identify possible skin type patterns.
            </p>

            <h3>Calibration process</h3>

            <ul>
                <li>Moisture: compare dry-skin and wet-skin references.</li>
                <li>pH: use buffer references around pH 4.0 and 9.0.</li>
                <li>Oiliness: compare clean paper with oil-saturated paper.</li>
            </ul>
        </div>

        <div class="notice-card">
            <p class="eyebrow">Important note</p>

            <h3>Honest about limits.</h3>

            <p>
                DermaSense is an educational prototype and should not be
                treated as a clinical diagnostic device.
            </p>

            <p>
                It does not replace professional dermatological advice.
            </p>
        </div>

    </div>

</section>


<section class="section" id="insights">

    <div class="section-heading centered">
        <p class="eyebrow">Read your skin more clearly</p>
        <h2>Skin Insights.</h2>
        <p>
            Turn basic readings into a clearer picture of your skin patterns.
        </p>
    </div>

    <div class="skin-table">

        <div class="table-row table-header">
            <span>Skin type</span>
            <span>Common pattern</span>
            <span>Possible focus</span>
        </div>

        <div class="table-row">
            <span>Oily</span>
            <span>Higher surface oil readings</span>
            <span>Lightweight, non-comedogenic care</span>
        </div>

        <div class="table-row">
            <span>Dry</span>
            <span>Lower moisture readings</span>
            <span>Hydration and barrier support</span>
        </div>

        <div class="table-row">
            <span>Combination</span>
            <span>Different readings across areas</span>
            <span>Area-specific routine choices</span>
        </div>

        <div class="table-row">
            <span>Normal</span>
            <span>Relatively balanced readings</span>
            <span>Simple maintenance routine</span>
        </div>

    </div>

    <div class="ingredient-grid">
        <div>
            <h3>Dry skin</h3>
            <p>
                Explore humectants, ceramides, and gentle moisturizers.
            </p>
        </div>

        <div>
            <h3>Oily skin</h3>
            <p>
                Explore lightweight hydration and non-comedogenic formulas.
            </p>
        </div>

        <div>
            <h3>Sensitive skin</h3>
            <p>
                Focus on gentle formulas and avoid unnecessary irritation.
            </p>
        </div>
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
            SkinSense was created to make skin analysis more affordable,
            understandable, and practical.
        </p>

        <p>
            Our mission is affordable, science-backed skin analysis
            for everyone.
        </p>

        <div class="values">
            <span>Science-backed</span>
            <span>Accessible</span>
            <span>Transparent</span>
        </div>
    </div>

</section>


<section class="form-panel" id="contact">

    <div>
        <p class="eyebrow">We would love to hear from you</p>

        <h2>Questions?<br>Let's talk.</h2>

        <p>
            Ask us about setup, calibration, troubleshooting, shipping,
            returns, or the DermaSense roadmap.
        </p>
    </div>

    <form onsubmit="return false;">

        <label for="contact-name">Name</label>
        <input id="contact-name" type="text" placeholder="Your name">

        <label for="contact-email">Email</label>
        <input id="contact-email" type="email" placeholder="you@example.com">

        <label for="contact-message">Message</label>
        <textarea id="contact-message" placeholder="How can we help?"></textarea>

        <button class="dark-button" type="submit">
            Send Message
        </button>

    </form>

</section>


<section class="waitlist-panel" id="waitlist">

    <div>
        <p class="eyebrow">Early access</p>

        <h2>Be the First to Try DermaSense.</h2>

        <p>
            Join the waitlist and follow the journey of affordable,
            practical skin analysis.
        </p>
    </div>

    <form onsubmit="showConfirmation(); return false;">

        <label for="waitlist-name">Name</label>
        <input id="waitlist-name" type="text" placeholder="Your name">

        <label for="waitlist-email">Email</label>
        <input id="waitlist-email" type="email" placeholder="you@example.com">

        <label for="waitlist-skin">Optional skin type</label>
        <select id="waitlist-skin">
            <option>Prefer not to say</option>
            <option>Oily</option>
            <option>Dry</option>
            <option>Combination</option>
            <option>Normal</option>
        </select>

        <button class="light-button" type="submit">
            Join the Waitlist
        </button>

        <p id="confirmation" class="confirmation"></p>

    </form>

</section>

</main>


<footer class="site-footer">

    <div class="footer-logo">
""" + logo_tag + """
    </div>

    <div>
        <p>
            We don't guess your skin. We measure it.
        </p>

        <p class="footer-small">
            DermaSense provides educational guidance and does not replace
            professional dermatological advice.
        </p>
    </div>

    <div class="footer-links">
        <a href="#home">Home</a>
        <a href="#product">Product</a>
        <a href="#waitlist">Waitlist</a>
    </div>

    <p class="copyright">
        Copyright 2026 SkinSense
    </p>

</footer>


<script>
window.addEventListener("load", function () {
    var splash = document.getElementById("splash-screen");

    setTimeout(function () {
        splash.classList.add("splash-hidden");
    }, 1800);
});

function showConfirmation() {
    var confirmation = document.getElementById("confirmation");

    if (confirmation) {
        confirmation.innerHTML =
            "Thank you. You have joined the SkinSense waitlist.";
    }
}
</script>

</body>
</html>
"""

    file = open("index.html", "w", encoding="utf-8")
    file.write(html)
    file.close()

    print("index.html created successfully.")


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
        radial-gradient(
            circle at 10% 10%,
            rgba(255, 255, 255, 0.7),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 80%,
            rgba(226, 246, 222, 0.7),
            transparent 30%
        ),
        linear-gradient(135deg, #dff7f3, #c7ebe4 48%, #edf2df);
    color: #234b49;
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

a {
    color: inherit;
    text-decoration: none;
}

.splash-screen {
    align-items: center;
    background:
        radial-gradient(
            circle at 20% 20%,
            rgba(255, 255, 255, 0.8),
            transparent 28%
        ),
        radial-gradient(
            circle at 80% 75%,
            rgba(255, 255, 255, 0.5),
            transparent 30%
        ),
        linear-gradient(135deg, #dff7f3, #bde8e0 50%, #e8f1dc);
    display: flex;
    height: 100vh;
    justify-content: center;
    left: 0;
    opacity: 1;
    position: fixed;
    top: 0;
    transition: opacity 0.8s ease, visibility 0.8s ease;
    visibility: visible;
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
    margin-bottom: 25px;
}

.splash-logo .brand-logo {
    background: transparent;
    border-radius: 0;
    max-height: 95px;
    max-width: 190px;
    padding: 0;
}

.splash-label {
    color: #397e78;
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 4px;
    margin-bottom: 18px;
}

.splash-content h1 {
    color: #234b49;
    font-family: Georgia, serif;
    font-size: 52px;
    font-weight: normal;
    margin-bottom: 12px;
}

.splash-content p {
    color: #397e78;
}

.loading-line {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 20px;
    height: 5px;
    margin: 35px auto 0;
    overflow: hidden;
    width: 180px;
}

.loading-line span {
    animation: loading-animation 1.8s ease-in-out;
    background: #78aaa0;
    border-radius: 20px;
    display: block;
    height: 100%;
    transform: translateX(-100%);
    width: 100%;
}

@keyframes loading-animation {
    from {
        transform: translateX(-100%);
    }

    to {
        transform: translateX(0);
    }
}

.site-header {
    align-items: center;
    display: flex;
    gap: 25px;
    justify-content: space-between;
    margin: auto;
    max-width: 1280px;
    padding: 24px 40px;
}

.brand-logo {
    background: transparent;
    border-radius: 0;
    display: block;
    max-height: 58px;
    max-width: 145px;
    object-fit: contain;
    padding: 0;
}

.navigation {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
}

.navigation a,
.header-button {
    border: 1px solid rgba(35, 75, 73, 0.3);
    border-radius: 30px;
    font-size: 12px;
    padding: 9px 15px;
    transition: 0.25s;
    white-space: nowrap;
}

.navigation a:hover,
.header-button:hover {
    background: rgba(255, 255, 255, 0.5);
    transform: translateY(-3px);
}

.header-button {
    font-weight: bold;
}

main {
    margin: auto;
    max-width: 1280px;
    padding: 30px 40px 100px;
}

.hero-section {
    align-items: center;
    display: grid;
    gap: 75px;
    grid-template-columns: 0.9fr 1.1fr;
    min-height: 700px;
}

.eyebrow {
    color: #397e78;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 2px;
    margin-bottom: 18px;
    text-transform: uppercase;
}

.hero-copy h1 {
    color: #234b49;
    font-family: Georgia, serif;
    font-size: 76px;
    font-weight: normal;
    line-height: 1.02;
    margin-bottom: 25px;
}

.hero-tagline {
    color: #397e78;
    font-family: Georgia, serif;
    font-size: 25px;
    margin-bottom: 20px;
}

.hero-description {
    font-size: 17px;
    max-width: 530px;
}

.hero-buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 30px;
}

.primary-button,
.secondary-button,
.dark-button,
.light-button {
    border: none;
    border-radius: 30px;
    display: inline-block;
    font-size: 13px;
    font-weight: bold;
    padding: 14px 22px;
    transition: 0.25s;
}

.primary-button {
    background: rgba(255, 255, 255, 0.85);
    color: #397e78;
}

.secondary-button {
    background: rgba(58, 126, 120, 0.85);
    color: white;
}

.primary-button:hover,
.secondary-button:hover,
.dark-button:hover,
.light-button:hover {
    transform: translateY(-4px);
}

.hero-art {
    background:
        radial-gradient(
            circle at 75% 20%,
            rgba(255, 255, 255, 0.35),
            transparent 25%
        ),
        linear-gradient(
            135deg,
            rgba(108, 198, 188, 0.85),
            rgba(75, 158, 157, 0.78)
        );
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 34px;
    box-shadow: 0 25px 60px rgba(35, 75, 73, 0.12);
    min-height: 550px;
    overflow: hidden;
    padding: 35px;
    position: relative;
}

.art-label {
    color: white;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 2px;
}

.floating-dot {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 50%;
    height: 10px;
    position: absolute;
    width: 10px;
}

.dot-one {
    right: 17%;
    top: 20%;
}

.dot-two {
    left: 14%;
    top: 45%;
}

.dot-three {
    bottom: 22%;
    right: 28%;
}

.device {
    background: rgba(247, 255, 253, 0.93);
    border: 8px solid rgba(198, 242, 235, 0.85);
    border-radius: 28px;
    box-shadow: 18px 25px 0 rgba(35, 119, 113, 0.25);
    height: 235px;
    left: 19%;
    padding: 18px;
    position: absolute;
    top: 24%;
    transform: rotate(-8deg);
    width: 285px;
}

.device-lights {
    display: flex;
    gap: 7px;
}

.device-lights span {
    background: #68ada5;
    border-radius: 50%;
    height: 9px;
    width: 9px;
}

.device-screen {
    align-items: center;
    background: #204b49;
    color: #b8eee8;
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin: 25px auto 18px;
    padding: 18px;
    width: 150px;
}

.device-screen strong {
    color: white;
    font-size: 16px;
    letter-spacing: 2px;
}

.device-buttons {
    display: flex;
    gap: 12px;
    justify-content: center;
}

.device-buttons span {
    background: #68ada5;
    border-radius: 50%;
    height: 25px;
    width: 25px;
}

.sensor {
    background: #397e78;
    border-radius: 50%;
    bottom: 18px;
    height: 38px;
    position: absolute;
    right: 20px;
    width: 38px;
}

.sensor span {
    background: #c3f0e9;
    border-radius: 50%;
    display: block;
    height: 15px;
    margin: 11px;
    width: 15px;
}

.face-art {
    border: 4px solid rgba(255, 255, 255, 0.85);
    border-radius: 48% 48% 45% 45%;
    bottom: 9%;
    height: 150px;
    position: absolute;
    right: 16%;
    transform: rotate(8deg);
    width: 130px;
}

.eye {
    background: white;
    border-radius: 50%;
    height: 7px;
    position: absolute;
    top: 55px;
    width: 7px;
}

.eye-left {
    left: 32px;
}

.eye-right {
    right: 32px;
}

.nose {
    border-right: 2px solid white;
    height: 28px;
    left: 62px;
    position: absolute;
    top: 61px;
    transform: rotate(15deg);
}

.mouth {
    border-bottom: 2px solid white;
    border-radius: 50%;
    height: 13px;
    left: 47px;
    position: absolute;
    top: 100px;
    width: 36px;
}

.art-caption {
    bottom: 30px;
    color: white;
    font-family: Georgia, serif;
    font-size: 22px;
    position: absolute;
    right: 35px;
}

.intro-strip {
    align-items: center;
    background: rgba(255, 255, 255, 0.3);
    border: 1px solid rgba(35, 75, 73, 0.12);
    border-radius: 28px;
    display: grid;
    gap: 30px;
    grid-template-columns: 80px 1fr 1fr;
    margin: 0 auto 110px;
    max-width: 1100px;
    padding: 35px;
}

.intro-number {
    color: #397e78;
    font-family: Georgia, serif;
    font-size: 35px;
}

.section {
    margin: 0 auto 130px;
    max-width: 1100px;
}

.section-heading {
    margin-bottom: 40px;
    max-width: 650px;
}

.centered {
    margin-left: auto;
    margin-right: auto;
    text-align: center;
}

.section-heading h2,
.intro-strip h2,
.product-copy h2,
.about-copy h2,
.form-panel h2,
.waitlist-panel h2 {
    color: #234b49;
    font-family: Georgia, serif;
    font-size: 48px;
    font-weight: normal;
    line-height: 1.1;
}

.feature-grid {
    display: grid;
    gap: 20px;
    grid-template-columns: repeat(3, 1fr);
}

.feature-card {
    border: 1px solid rgba(35, 75, 73, 0.1);
    border-radius: 28px;
    min-height: 330px;
    padding: 30px;
    transition: 0.25s;
}

.feature-card:hover,
.process-card:hover,
.ingredient-grid div:hover {
    box-shadow: 0 18px 35px rgba(35, 75, 73, 0.1);
    transform: translateY(-7px);
}

.blue-card {
    background: linear-gradient(
        145deg,
        rgba(255, 255, 255, 0.42),
        transparent
    ), #b5dfe1;
}

.cream-card {
    background: linear-gradient(
        145deg,
        rgba(255, 255, 255, 0.75),
        transparent
    ), #f5f0df;
}

.sage-card {
    background: linear-gradient(
        145deg,
        rgba(255, 255, 255, 0.45),
        transparent
    ), #c4dbbc;
}

.feature-icon {
    color: #397e78;
    font-size: 60px;
    margin-bottom: 35px;
}

.card-number {
    color: #397e78;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 2px;
}

.feature-card h3,
.process-card h3,
.ingredient-grid h3,
.notice-card h3 {
    color: #234b49;
    font-family: Georgia, serif;
    font-weight: normal;
}

.feature-card h3 {
    font-size: 30px;
    margin-bottom: 12px;
}

.product-panel,
.form-panel,
.waitlist-panel {
    align-items: center;
    border-radius: 35px;
    display: grid;
    gap: 70px;
    grid-template-columns: 1fr 1fr;
    margin: 0 auto 130px;
    max-width: 1100px;
    padding: 65px;
}

.product-panel,
.form-panel {
    background:
        radial-gradient(
            circle at 85% 15%,
            rgba(255, 255, 255, 0.75),
            transparent 25%
        ),
        linear-gradient(135deg, #f8f2e4, #e8f0df);
}

.product-copy p {
    max-width: 500px;
}

.dark-button {
    background: rgba(35, 75, 73, 0.92);
    color: white;
    cursor: pointer;
    margin-top: 20px;
}

.spec-card {
    background: rgba(255, 255, 255, 0.82);
    border-radius: 25px;
    box-shadow: 0 20px 45px rgba(35, 75, 73, 0.1);
    padding: 28px;
}

.spec-top {
    display: flex;
    font-size: 11px;
    font-weight: bold;
    justify-content: space-between;
}

.mini-device {
    background: linear-gradient(145deg, #b5dfe1, #76bdb8);
    border-radius: 20px;
    height: 170px;
    margin: 25px 0;
    padding: 35px;
    position: relative;
}

.mini-screen {
    background: #204b49;
    color: #b8eee8;
    margin: auto;
    padding: 20px;
    text-align: center;
    width: 130px;
}

.mini-sensor {
    background: #a5e8df;
    border: 8px solid white;
    border-radius: 50%;
    bottom: 18px;
    height: 35px;
    position: absolute;
    right: 25px;
    width: 35px;
}

.spec-list {
    display: grid;
    gap: 15px;
    grid-template-columns: 1fr 1fr;
}

.spec-list div {
    border-bottom: 1px solid #d8e4df;
    display: flex;
    flex-direction: column;
    padding-bottom: 10px;
}

.spec-list span {
    color: #53827d;
    font-size: 11px;
}

.spec-list strong {
    font-size: 14px;
}

.process-grid {
    display: grid;
    gap: 18px;
    grid-template-columns: repeat(4, 1fr);
}

.process-card {
    background: rgba(255, 255, 255, 0.35);
    border: 1px solid rgba(35, 75, 73, 0.12);
    border-radius: 25px;
    min-height: 300px;
    padding: 26px;
    transition: 0.25s;
}

.process-card span {
    color: #397e78;
    font-size: 12px;
    font-weight: bold;
}

.process-symbol {
    color: #397e78;
    font-size: 50px;
    margin: 30px 0;
}

.process-card h3 {
    font-size: 25px;
    margin-bottom: 12px;
}

.quote-section {
    background:
        radial-gradient(
            circle at 20% 20%,
            rgba(255, 255, 255, 0.3),
            transparent 25%
        ),
        linear-gradient(135deg, #82c8be, #63a9a8);
    border-radius: 35px;
    color: white;
    margin: 0 auto 130px;
    max-width: 1100px;
    padding: 90px 40px;
    text-align: center;
}

.quote-mark {
    font-family: Georgia, serif;
    font-size: 80px;
    line-height: 0.7;
}

.quote-section p {
    font-family: Georgia, serif;
    font-size: 45px;
    line-height: 1.15;
    margin: 25px auto;
}

.science-grid {
    display: grid;
    gap: 40px;
    grid-template-columns: 1.2fr 0.8fr;
}

.science-content h3 {
    font-family: Georgia, serif;
    font-size: 28px;
    font-weight: normal;
    margin: 30px 0 15px;
}

.science-content ul {
    padding-left: 25px;
}

.notice-card {
    background: rgba(255, 249, 233, 0.8);
    border-radius: 28px;
    padding: 35px;
}

.notice-card h3 {
    font-size: 30px;
    margin-bottom: 18px;
}

.skin-table {
    background: rgba(255, 255, 255, 0.4);
    border-radius: 22px;
    overflow: hidden;
}

.table-row {
    display: grid;
    gap: 20px;
    grid-template-columns: 1fr 1fr 1fr;
    padding: 20px 25px;
}

.table-row:not(:last-child) {
    border-bottom: 1px solid rgba(35, 75, 73, 0.13);
}

.table-header {
    background: rgba(91, 169, 164, 0.75);
    color: white;
    font-weight: bold;
}

.ingredient-grid {
    display: grid;
    gap: 18px;
    grid-template-columns: repeat(3, 1fr);
    margin-top: 25px;
}

.ingredient-grid div {
    background: rgba(255, 255, 255, 0.55);
    border-radius: 22px;
    padding: 25px;
    transition: 0.25s;
}

.ingredient-grid h3 {
    font-size: 24px;
    margin-bottom: 10px;
}

.about-section {
    align-items: center;
    display: grid;
    gap: 80px;
    grid-template-columns: 1fr 1fr;
    margin: 0 auto 130px;
    max-width: 1100px;
}

.about-art {
    background: linear-gradient(135deg, #f7f0df, #d9e8cf);
    border-radius: 45% 55% 48% 52%;
    height: 420px;
    position: relative;
}

.about-circle {
    align-items: center;
    background: #8bbdb5;
    border: 12px solid rgba(255, 255, 255, 0.85);
    border-radius: 50%;
    color: white;
    display: flex;
    font-family: Georgia, serif;
    font-size: 50px;
    height: 150px;
    justify-content: center;
    left: 35%;
    position: absolute;
    top: 33%;
    width: 150px;
}

.stem {
    background: #77a270;
    height: 230px;
    left: 51%;
    position: absolute;
    top: 22%;
    transform: rotate(12deg);
    width: 5px;
}

.leaf {
    background: #a3c59a;
    border-radius: 100% 0 100% 0;
    height: 70px;
    position: absolute;
    width: 40px;
}

.leaf-one {
    left: 42%;
    top: 28%;
    transform: rotate(-35deg);
}

.leaf-two {
    left: 54%;
    top: 42%;
    transform: rotate(35deg);
}

.leaf-three {
    left: 43%;
    top: 57%;
    transform: rotate(-35deg);
}

.values {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 25px;
}

.values span {
    border: 1px solid #397e78;
    border-radius: 25px;
    color: #397e78;
    font-size: 12px;
    padding: 9px 14px;
}

.form-panel,
.waitlist-panel {
    margin-bottom: 90px;
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
    margin-top: 15px;
}

.form-panel input,
.form-panel textarea,
.waitlist-panel input,
.waitlist-panel select {
    background: rgba(255, 255, 255, 0.85);
    border: 1px solid rgba(35, 75, 73, 0.18);
    border-radius: 12px;
    font-family: Arial, sans-serif;
    font-size: 14px;
    margin-top: 6px;
    padding: 13px;
}

.form-panel textarea {
    min-height: 130px;
}

.waitlist-panel {
    background:
        radial-gradient(
            circle at 80% 20%,
            rgba(255, 255, 255, 0.28),
            transparent 25%
        ),
        linear-gradient(135deg, #82c8be, #63a9a8);
    color: white;
}

.waitlist-panel h2 {
    color: white;
}

.waitlist-panel .eyebrow {
    color: #e0fff9;
}

.light-button {
    background: rgba(255, 255, 255, 0.9);
    color: #397e78;
    cursor: pointer;
    margin-top: 23px;
}

.confirmation {
    color: #e0fff9;
    font-weight: bold;
    margin-top: 18px;
}

.site-footer {
    align-items: center;
    background: rgba(35, 75, 73, 0.92);
    color: white;
    display: grid;
    gap: 30px;
    grid-template-columns: 160px 1fr 1fr;
    padding: 55px max(40px, calc((100% - 1200px) / 2));
}

.footer-logo .brand-logo {
    background: transparent;
    max-height: 65px;
    max-width: 145px;
    padding: 0;
}

.footer-small {
    color: #c3e2dd;
    font-size: 12px;
    margin-top: 10px;
    max-width: 470px;
}

.footer-links {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    justify-content: flex-end;
}

.footer-links a {
    border: 1px solid rgba(255, 255, 255, 0.35);
    border-radius: 25px;
    font-size: 12px;
    padding: 8px 13px;
}

.copyright {
    color: #c3e2dd;
    font-size: 11px;
    grid-column: 1 / 4;
    margin-top: 20px;
    text-align: center;
}

@media screen and (max-width: 950px) {
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
    .about-section,
    .form-panel,
    .waitlist-panel,
    .science-grid {
        grid-template-columns: 1fr;
    }

    .hero-copy h1 {
        font-size: 60px;
    }

    .feature-grid,
    .process-grid {
        grid-template-columns: 1fr 1fr;
    }

    .site-footer {
        grid-template-columns: 1fr 1fr;
    }

    .copyright {
        grid-column: 1 / 3;
    }
}

@media screen and (max-width: 600px) {
    .site-header {
        padding: 20px;
    }

    main {
        padding: 20px 20px 70px;
    }

    .hero-copy h1 {
        font-size: 45px;
    }

    .hero-tagline {
        font-size: 21px;
    }

    .hero-art {
        min-height: 440px;
    }

    .device {
        left: 8%;
        transform: rotate(-5deg) scale(0.82);
        transform-origin: center;
    }

    .face-art {
        right: 5%;
        transform: rotate(6deg) scale(0.8);
    }

    .intro-strip {
        grid-template-columns: 1fr;
        margin-bottom: 80px;
        padding: 25px;
    }

    .section-heading h2,
    .intro-strip h2,
    .product-copy h2,
    .about-copy h2,
    .form-panel h2,
    .waitlist-panel h2 {
        font-size: 36px;
    }

    .feature-grid,
    .process-grid,
    .ingredient-grid {
        grid-template-columns: 1fr;
    }

    .product-panel,
    .form-panel,
    .waitlist-panel {
        padding: 30px;
    }

    .quote-section {
        padding: 65px 25px;
    }

    .quote-section p {
        font-size: 32px;
    }

    .table-row {
        font-size: 12px;
        gap: 10px;
        padding: 15px 12px;
    }

    .site-footer {
        display: block;
        padding: 40px 25px;
    }

    .footer-links {
        justify-content: flex-start;
        margin-top: 25px;
    }

    .copyright {
        margin-top: 30px;
        text-align: left;
    }
}
"""

    file = open("style.css", "w", encoding="utf-8")
    file.write(css)
    file.close()

    print("style.css created successfully.")


def create_website():
    create_html()
    create_css()

    print("")
    print("SkinSense website created successfully.")
    print("The splash screen and soft gradients were added.")
    print("The logo background was removed through CSS.")
    print("logo.png is used only as the logo.")


create_website()