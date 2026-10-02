# templates.py
# HTML templates built using Python strings and f-strings
# Reference: M1T2_Strings.docx, M3_Python functions_kss.pdf
# Restyled to the SkinSense sage / cream / charcoal design system.
def base_template(title, content):
    """Returns the full HTML page using string formatting."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | SkinSense</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Great+Vibes&family=Playfair+Display:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --cream: #FCFAF4;
            --paper: #FFFFFF;
            --sand: #F6F3EA;
            --mist: #F2F5F2;
            --sage-pale: #E3E9DC;
            --sage-wash: #F1F4EA;
            --sage: #8DA857;
            --sage-deep: #7A9249;
            --sage-soft: #A5C05A;
            --forest: #1F2A17;
            --ink: #222222;
            --body: #7A7A7A;
            --muted: #999999;
            --line: #E7E4D9;
            --line-soft: #F0EEE6;
            --peach: #E9C496;
            --radius: 6px;
            --radius-lg: 30px;
            --pill: 50px;
            --shadow-soft: 0 18px 40px rgba(31, 42, 23, .07);
            --shadow-card: 0 12px 30px rgba(31, 42, 23, .06);
            --wrap: 1180px;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: "Montserrat", "Helvetica Neue", Arial, sans-serif;
            font-size: 15px;
            background: var(--cream);
            color: var(--body);
            line-height: 1.75;
            -webkit-font-smoothing: antialiased;
        }}
        a {{ color: inherit; text-decoration: none; transition: color .2s ease; }}
        img {{ display: block; max-width: 100%; }}
        button, input, select, textarea {{ font: inherit; }}
        .container {{ max-width: var(--wrap); margin: 0 auto; padding: 0 24px; }}
        h1, h2, h3, h4 {{
            font-family: "Montserrat", "Helvetica Neue", Arial, sans-serif;
            font-weight: 700;
            color: var(--ink);
            line-height: 1.15;
            letter-spacing: -.01em;
        }}
        h1 {{ font-size: clamp(34px, 5vw, 58px); }}
        h2 {{ font-size: clamp(28px, 3.6vw, 42px); }}
        h3 {{ font-size: 19px; }}
        h4 {{ font-size: 15px; }}
        p {{ color: var(--body); }}
        /* Script accent replaces the old uppercase micro-label */
        .script {{
            display: block;
            font-family: "Great Vibes", "Segoe Script", cursive;
            font-size: clamp(27px, 3.1vw, 38px);
            font-weight: 400;
            line-height: 1.1;
            color: var(--sage);
            margin-bottom: 6px;
        }}
        .label {{
            display: block;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: .16em;
            text-transform: uppercase;
            color: var(--sage);
        }}
        /* Header */
        header {{
            background: var(--paper);
            border-bottom: 1px solid var(--line-soft);
            position: sticky;
            top: 0;
            z-index: 500;
        }}
        .header-inner {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 24px;
            min-height: 82px;
            padding: 12px 24px;
        }}
        .logo img {{ height: 34px; width: auto; }}
        nav {{ display: flex; flex-wrap: wrap; gap: 30px; }}
        nav a {{
            font-size: 11px;
            font-weight: 600;
            letter-spacing: .14em;
            text-transform: uppercase;
            color: var(--ink);
        }}
        nav a:hover {{ color: var(--sage); }}
        /* Hero */
        .hero {{
            text-align: center;
            padding: 96px 24px 88px;
            background:
                radial-gradient(circle at 82% 22%, rgba(141, 168, 87, .14), transparent 36%),
                radial-gradient(circle at 14% 80%, rgba(233, 196, 150, .16), transparent 32%),
                var(--cream);
        }}
        .hero h1 {{ max-width: 820px; margin: 8px auto 18px; }}
        .hero h1 span {{ color: var(--sage); }}
        .hero .sub {{
            font-size: 17px;
            max-width: 620px;
            margin: 0 auto 34px;
        }}
        .btn {{
            display: inline-block;
            background: var(--sage);
            border: 1.6px solid var(--sage);
            color: #fff;
            padding: 15px 34px;
            border-radius: var(--radius);
            font-size: 11px;
            font-weight: 700;
            letter-spacing: .16em;
            text-transform: uppercase;
            margin: 0 6px 10px;
            cursor: pointer;
            transition: background .22s ease, border-color .22s ease, transform .22s ease;
        }}
        .btn:hover {{ background: var(--forest); border-color: var(--forest); transform: translateY(-2px); }}
        .btn-dark {{ background: var(--ink); border-color: var(--ink); }}
        .btn-dark:hover {{ background: var(--sage); border-color: var(--sage); }}
        .btn-outline {{
            background: transparent;
            color: var(--ink);
            border-color: var(--line);
        }}
        .btn-outline:hover {{ background: var(--sage); border-color: var(--sage); color: #fff; }}
        section {{ padding: 88px 0; }}
        .section-head {{ max-width: 700px; margin-bottom: 40px; }}
        .section-head h2 {{ margin-bottom: 10px; }}
        .sand {{ background: var(--sand); }}
        .mist {{ background: var(--mist); }}
        /* Cards */
        .card-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 26px;
            margin-top: 10px;
        }}
        .card {{
            background: var(--paper);
            border: 1px solid var(--line-soft);
            border-radius: var(--radius);
            box-shadow: var(--shadow-card);
            padding: 32px 30px;
            display: flex;
            flex-direction: column;
        }}
        .card h3 {{ margin-bottom: 8px; }}
        .card p {{ font-size: 13.5px; }}
        .card .icon {{ display: block; font-size: 26px; margin-bottom: 12px; color: var(--sage); }}
        /* Steps */
        .steps {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 24px; }}
        .step {{
            background: var(--paper);
            border: 1px solid var(--line-soft);
            border-radius: var(--radius);
            box-shadow: var(--shadow-card);
            padding: 32px 28px;
            display: flex;
            align-items: flex-start;
            gap: 14px;
        }}
        .step .num {{
            background: var(--sage);
            color: #fff;
            border-radius: 50%;
            width: 32px;
            height: 32px;
            flex: 0 0 32px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 13px;
            font-weight: 700;
        }}
        /* Quote band */
        .quote-band {{
            background: var(--forest);
            color: #fff;
            text-align: center;
            padding: 92px 24px;
        }}
        .quote-band p {{
            font-family: "Playfair Display", Georgia, serif;
            font-size: clamp(26px, 3.4vw, 40px);
            line-height: 1.28;
            color: #fff;
            max-width: 760px;
            margin: 0 auto 20px;
        }}
        .quote-attribution {{
            font-size: 10px;
            font-weight: 600;
            letter-spacing: .24em;
            text-transform: uppercase;
            color: var(--sage-pale);
        }}
        /* Lists */
        .clean-list {{ list-style: none; margin-top: 24px; }}
        .clean-list li {{
            border-bottom: 1px solid var(--line);
            padding: 14px 0 14px 26px;
            position: relative;
            font-size: 14px;
            color: var(--body);
        }}
        .clean-list li::before {{
            content: "—";
            position: absolute;
            left: 0;
            color: var(--sage);
        }}
        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
            background: var(--paper);
            border-radius: var(--radius);
            box-shadow: var(--shadow-card);
            overflow: hidden;
        }}
        th, td {{ padding: 16px 20px; text-align: left; border-bottom: 1px solid var(--line-soft); }}
        th {{
            background: var(--sage-wash);
            color: var(--ink);
            font-size: 11px;
            font-weight: 700;
            letter-spacing: .12em;
            text-transform: uppercase;
        }}
        td {{ color: var(--body); font-size: 14px; }}
        /* Forms */
        .form-card {{
            background: var(--paper);
            border: 1px solid var(--line-soft);
            border-radius: var(--radius);
            box-shadow: var(--shadow-card);
            padding: 38px 34px;
        }}
        label {{
            display: block;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: .1em;
            text-transform: uppercase;
            color: var(--ink);
            margin: 22px 0 10px;
        }}
        label:first-child {{ margin-top: 0; }}
        input, textarea, select {{
            width: 100%;
            padding: 14px 16px;
            border: 1px solid #DED9C9;
            border-radius: var(--radius);
            background: var(--paper);
            color: var(--ink);
        }}
        input:focus, textarea:focus, select:focus {{ border-color: var(--sage); outline: none; }}
        .form-card .btn {{ margin-top: 26px; }}
        /* Footer */
        footer {{
            background: var(--sand);
            border-top: 1px solid var(--line);
            padding: 84px 24px 0;
        }}
        .footer-top {{
            display: grid;
            grid-template-columns: 1fr 1fr 1fr 1.3fr;
            gap: 46px;
            max-width: var(--wrap);
            margin: 0 auto;
            padding-bottom: 62px;
        }}
        .footer-col h4 {{
            font-size: 13px;
            font-weight: 700;
            letter-spacing: .08em;
            text-transform: uppercase;
            color: var(--ink);
            margin-bottom: 20px;
        }}
        .footer-col p {{ font-size: 13px; margin-bottom: 10px; }}
        .footer-col ul {{ list-style: none; }}
        .footer-col ul li {{ margin-bottom: 10px; }}
        .footer-col ul li a {{ font-size: 13px; color: var(--body); }}
        .footer-col ul li a:hover {{ color: var(--sage-deep); }}
        .footer-brand-card {{
            background: var(--cream);
            border: 1px solid var(--line-soft);
            border-radius: var(--radius);
            padding: 32px 28px;
            text-align: center;
        }}
        .footer-brand-card img {{ height: 24px; width: auto; margin: 0 auto 16px; }}
        .footer-brand-card p {{ font-size: 13px; line-height: 1.85; }}
        .footer-fine {{ font-size: 11px !important; color: var(--muted); margin-top: 10px; }}
        .footer-bottom {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: space-between;
            max-width: var(--wrap);
            margin: 0 auto;
            padding: 22px 0 26px;
            border-top: 1px solid var(--line);
        }}
        .footer-bottom p {{ font-size: 11px; color: var(--muted); }}
        @media screen and (max-width: 1000px) {{
            .footer-top {{ grid-template-columns: 1fr 1fr; }}
        }}
        @media screen and (max-width: 700px) {{
            .footer-top {{ grid-template-columns: 1fr; }}
            .header-inner {{ min-height: auto; }}
            nav {{ gap: 18px; }}
            .hero {{ padding: 70px 22px 64px; }}
            section {{ padding: 64px 0; }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="container header-inner">
            <div class="logo">
                <img src="/logo.png" alt="SkinSense">
            </div>
            <nav>
                <a href="/">Home</a>
                <a href="/product">Product</a>
                <a href="/how-it-works">How It Works</a>
                <a href="/science">Science &amp; Accuracy</a>
                <a href="/insights">Skin Insights</a>
                <a href="/about">About</a>
                <a href="/contact">Contact</a>
                <a href="/waitlist">Waitlist</a>
            </nav>
        </div>
    </header>
    {content}
    <footer>
        <div class="footer-top">
            <div class="footer-col">
                <h4>Contact us</h4>
                <p>Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh.</p>
                <p>Vidyalankar Institute of Technology<br>Mumbai, India</p>
                <p><a href="mailto:skinsense@example.com">skinsense@example.com</a></p>
            </div>
            <div class="footer-col">
                <h4>Follow us</h4>
                <ul>
                    <li><a href="/">Instagram</a></li>
                    <li><a href="/">LinkedIn</a></li>
                    <li><a href="/">YouTube</a></li>
                    <li><a href="/">Newsletter</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Useful links</h4>
                <ul>
                    <li><a href="/about">About us</a></li>
                    <li><a href="/product">DermaSense</a></li>
                    <li><a href="/how-it-works">How it works</a></li>
                    <li><a href="/science">Science</a></li>
                    <li><a href="/contact">Contact us</a></li>
                </ul>
            </div>
            <div class="footer-brand-card">
                <img src="/logo.png" alt="SkinSense">
                <p>Know your skin. Care better. DermaSense provides educational prototype readings and does not replace professional dermatological advice.</p>
                <p class="footer-fine">Readings depend on calibration, placement, and device condition.</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 SkinSense. All rights reserved.</p>
            <p>Designed for the DermaSense prototype.</p>
        </div>
    </footer>
</body>
</html>"""