# pages.py
# Page content stored as dictionaries
# Reference: Dictionary.pdf, M1_LIST.ipynb, M3_Python functions_kss.pdf

from templates import base_template

# --- Home Page ---
def home_page():
    features = [
        {"icon": "💧", "title": "Moisture", "text": "Capacitive sensing detects hydration levels."},
        {"icon": "🧪", "title": "pH Balance", "text": "Liquid pH probe reads your skin's acid-alkaline state."},
        {"icon": "🛢️", "title": "Oiliness", "text": "Blotting paper and light sensor quantify sebum."},
        {"icon": "📋", "title": "Ingredient Guidance", "text": "Decision-tree algorithm suggests ingredients."}
    ]

    cards = ""
    for f in features:
        cards += f"""
        <div class="card">
            <span class="icon">{f['icon']}</span>
            <h3>{f['title']}</h3>
            <p>{f['text']}</p>
        </div>"""

    steps_data = ["Press the sensors to your skin", "Get instant readings", "Receive ingredient suggestions"]
    steps = ""
    for i, s in enumerate(steps_data, 1):
        steps += f'<div class="step"><span class="num">{i}</span> {s}</div>'

    content = f"""
    <section class="hero">
        <div class="container">
            <div class="brand-tag">Meet DermaSense</div>
            <h1>Know Your Skin, <span>Care Better</span></h1>
            <p class="sub">DermaSense is a low-cost, IoT-enabled skin analysis device by SkinSense. It measures moisture, pH, and oiliness.</p>
            <a href="/how-it-works" class="btn">See How It Works</a>
            <a href="/contact" class="btn btn-outline">Join the Waitlist</a>
        </div>
    </section>

    <section>
        <div class="container">
            <div class="section-head">
                <h2>What DermaSense Measures</h2>
                <p>Three key parameters, one simple device.</p>
            </div>
            <div class="card-grid">{cards}</div>
        </div>
    </section>

    <section>
        <div class="container">
            <div class="section-head">
                <h2>How It Works</h2>
                <p>Three steps. Under a minute.</p>
            </div>
            <div class="steps">{steps}</div>
        </div>
    </section>

    <div class="quote">
        <blockquote>"We don't guess your skin. We measure it."</blockquote>
        <div class="attr">— The SkinSense Team</div>
    </div>
    """
    return base_template("Home", content)


# --- Product Page ---
def product_page():
    specs = [
        ("Microcontroller", "ESP32 DevKit V1 (Wi-Fi + Bluetooth)"),
        ("Moisture Sensor", "Capacitive soil moisture sensor (YL-69)"),
        ("pH Sensor", "PH-4502C analog pH meter with glass probe"),
        ("Light Sensor", "BH1750 ambient light sensor"),
        ("Display", "16x2 I2C LCD"),
        ("Power", "USB 5V"),
        ("Total Cost", "~Rs. 2,500 ($30)")
    ]

    rows = ""
    for s in specs:
        rows += f"<tr><td>{s[0]}</td><td>{s[1]}</td></tr>"

    comparison = [
        ("VISIA Complexion", "14+", "4.2L – 16.8L"),
        ("HiMirror", "3", "8.4K – 25K"),
        ("Neutrogena Skin360", "3", "Free"),
        ("DermaSense", "3", "~2.5K")
    ]

    comp_rows = ""
    for c in comparison:
        comp_rows += f"<tr><td>{c[0]}</td><td>{c[1]}</td><td>{c[2]}</td></tr>"

    content = f"""
    <section class="hero" style="padding:4rem 1rem 3rem;">
        <div class="container">
            <div class="brand-tag">The Product</div>
            <h1>Meet <span>DermaSense</span></h1>
            <p class="sub">A handheld IoT device that measures three skin parameters for under Rs. 2,500.</p>
            <a href="/contact" class="btn">Join Waitlist</a>
        </div>
    </section>

    <section>
        <div class="container">
            <div class="section-head"><h2>Technical Specifications</h2></div>
            <table>
                <tr><th>Component</th><th>Specification</th></tr>
                {rows}
            </table>
        </div>
    </section>

    <section>
        <div class="container">
            <div class="section-head"><h2>How It Compares</h2></div>
            <table>
                <tr><th>Device</th><th>Parameters</th><th>Price (Rs.)</th></tr>
                {comp_rows}
            </table>
        </div>
    </section>
    """
    return base_template("Product", content)


# --- How It Works Page ---
def how_it_works_page():
    readings = [
        ("Moisture", "Low <40%: Dry. Normal 40-70%: Balanced. High >70%: Well-hydrated."),
        ("pH", "Healthy 4.5-5.8: Barrier intact. Acidic <4.5: Irritation. Alkaline >5.8: Compromised."),
        ("Oiliness", "Low <20%: Dry. Medium 20-60%: Normal. High >60%: Oily.")
    ]

    cards = ""
    for r in readings:
        cards += f"""
        <div class="card">
            <h3>{r[0]}</h3>
            <p>{r[1]}</p>
        </div>"""

    content = f"""
    <section class="hero" style="padding:4rem 1rem 3rem;">
        <div class="container">
            <div class="brand-tag">How It Works</div>
            <h1>From Skin to <span>Solution</span> in Under a Minute</h1>
        </div>
    </section>

    <section>
        <div class="container">
            <div class="section-head"><h2>What Each Reading Means</h2></div>
            <div class="card-grid">{cards}</div>
        </div>
    </section>

    <section>
        <div class="container">
            <div class="section-head">
                <h2>How the Oiliness Sensor Works</h2>
                <p>We use cosmetic blotting paper pressed against the skin. As it absorbs oil, the paper becomes more transparent. A BH1750 light sensor paired with a yellow LED measures light transmission.</p>
            </div>
        </div>
    </section>
    """
    return base_template("How It Works", content)


# --- Science Page ---
def science_page():
    content = """
    <section class="hero" style="padding:4rem 1rem 3rem;">
        <div class="container">
            <div class="brand-tag">Science &amp; Accuracy</div>
            <h1>Built on <span>Measurement</span></h1>
            <p class="sub">Every reading is calibrated and grounded in dermatological research.</p>
        </div>
    </section>

    <section>
        <div class="container">
            <div class="section-head"><h2>Calibration Process</h2></div>
            <div class="card-grid">
                <div class="card"><h3>Moisture</h3><p>Two-point calibration on dry and wet skin. Range: 236 ADC units.</p></div>
                <div class="card"><h3>pH</h3><p>Calibrated with pH 4.0 and pH 9.0 buffers. R-squared = 0.999.</p></div>
                <div class="card"><h3>Oiliness</h3><p>Calibrated with clean and oil-saturated blotting paper. Range: 600 lux.</p></div>
            </div>
        </div>
    </section>
    """
    return base_template("Science", content)


# --- Insights Page ---
def insights_page():
    content = """
    <section class="hero" style="padding:4rem 1rem 3rem;">
        <div class="container">
            <div class="brand-tag">Skin Insights</div>
            <h1>Your Results, <span>Explained</span></h1>
        </div>
    </section>

    <section>
        <div class="container">
            <div class="section-head"><h2>Skin Type Classification</h2></div>
            <table>
                <tr><th>Skin Type</th><th>Condition</th></tr>
                <tr><td>Oily</td><td>Oiliness greater than 60%</td></tr>
                <tr><td>Dry</td><td>Oiliness less than 20% and Moisture less than 40%</td></tr>
                <tr><td>Combination</td><td>Oiliness between 20% and 60%</td></tr>
                <tr><td>Normal</td><td>Oiliness between 20% and 60% and Moisture greater than 40%</td></tr>
            </table>
        </div>
    </section>
    """
    return base_template("Insights", content)


# --- About Page ---
def about_page():
    content = """
    <section class="hero" style="padding:4rem 1rem 3rem;">
        <div class="container">
            <div class="brand-tag">About</div>
            <h1>Our <span>Mission</span></h1>
            <p class="sub">We believe skincare should be based on measurement, not marketing.</p>
        </div>
    </section>

    <section>
        <div class="container" style="text-align:center; max-width:700px; margin:0 auto;">
            <p style="color:#5a6672; font-size:1.05rem;">
                SkinSense was started because we were tired of wasting money on skincare that didn't work.
                So we built something that could actually tell us what our skin needed.
            </p>
        </div>
    </section>
    """
    return base_template("About", content)


# --- Contact Page ---
def contact_page():
    content = """
    <section class="hero" style="padding:4rem 1rem 3rem;">
        <div class="container">
            <div class="brand-tag">Contact</div>
            <h1>Get in <span>Touch</span></h1>
        </div>
    </section>

    <section>
        <div class="container" style="max-width:500px; margin:0 auto;">
            <form method="POST" action="/submit">
                <label for="name">Your Name</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message</label>
                <textarea id="message" name="message" rows="5" required></textarea>

                <button type="submit" class="btn" style="border:none; cursor:pointer;">Send Message</button>
            </form>
        </div>
    </section>
    """
    return base_template("Contact", content)
# --- Waitlist Page ---
def waitlist_page():
    content = """
    <section class="hero" style="padding:4rem 1rem 3rem;">
        <div class="container">
            <div class="brand-tag">Join the Waitlist</div>
            <h1>Be the First to Try <span>DermaSense</span></h1>
            <p class="sub">Sign up and we'll let you know the moment DermaSense is ready.</p>
        </div>
    </section>

    <section>
        <div class="container" style="max-width:500px; margin:0 auto;">
            <form method="POST" action="/submit-waitlist">
                <label for="name">Your Name</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" required>

                <label for="skintype">Your Skin Type (optional)</label>
                <input type="text" id="skintype" name="skintype">

                <button type="submit" class="btn" style="border:none; cursor:pointer;">Join Waitlist</button>
            </form>
        </div>
    </section>
    """
    return base_template("Waitlist", content)