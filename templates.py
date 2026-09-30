# templates.py
# HTML templates built using Python strings and f-strings
# Reference: M1T2_Strings.docx, M3_Python functions_kss.pdf

def base_template(title, content):
    """Returns the full HTML page using string formatting."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | SkinSense</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: Arial, sans-serif;
            background: #f8fafb;
            color: #1a1f24;
            line-height: 1.6;
        }}
        .container {{ max-width: 1100px; margin: 0 auto; padding: 0 1.5rem; }}
        header {{
            padding: 1.8rem 0;
            border-bottom: 1px solid #dde6ea;
            background: #fff;
            position: sticky;
            top: 0;
        }}
        .header-inner {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
        }}
        .logo {{ font-size: 1.5rem; font-weight: 700; color: #1a1f24; }}
        .logo span {{ color: #3b7ea1; }}
        nav a {{
            margin-left: 2rem;
            text-decoration: none;
            color: #5a6672;
            font-size: 0.95rem;
        }}
        nav a:hover {{ color: #3b7ea1; }}
        .hero {{ text-align: center; padding: 5rem 1rem 4rem; }}
        .hero .brand-tag {{
            display: inline-block;
            background: #e8f1f5;
            color: #3b7ea1;
            padding: 0.35rem 1.1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            margin-bottom: 1.5rem;
        }}
        .hero h1 {{
            font-size: 3.4rem;
            font-weight: 700;
            max-width: 800px;
            margin: 0 auto 1.2rem;
        }}
        .hero h1 span {{ color: #3b7ea1; }}
        .hero .sub {{
            font-size: 1.2rem;
            color: #5a6672;
            max-width: 620px;
            margin: 0 auto 2.5rem;
        }}
        .btn {{
            display: inline-block;
            background: #3b7ea1;
            color: #fff;
            padding: 0.9rem 2.4rem;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 500;
            margin: 0.3rem;
        }}
        .btn-outline {{
            background: transparent;
            color: #3b7ea1;
            border: 1.5px solid #3b7ea1;
        }}
        section {{ padding: 5rem 0; }}
        .section-head {{ text-align: center; margin-bottom: 3rem; }}
        .section-head h2 {{ font-size: 2.2rem; margin-bottom: 0.6rem; }}
        .section-head p {{ color: #5a6672; }}
        .card-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1.5rem;
            margin: 2.5rem 0;
        }}
        .card {{
            background: #fff;
            padding: 2rem 1.6rem;
            border-radius: 14px;
            border: 1px solid #dde6ea;
        }}
        .card h3 {{ font-size: 1.1rem; margin-bottom: 0.4rem; }}
        .card p {{ font-size: 0.95rem; color: #5a6672; }}
        .card .icon {{ font-size: 1.8rem; display: block; margin-bottom: 0.7rem; }}
        .steps {{
            display: flex;
            justify-content: center;
            gap: 1.2rem;
            flex-wrap: wrap;
            margin: 2.5rem 0;
        }}
        .step {{
            background: #fff;
            padding: 1.4rem 2rem;
            border-radius: 60px;
            border: 1px solid #dde6ea;
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }}
        .step .num {{
            background: #3b7ea1;
            color: #fff;
            border-radius: 50%;
            width: 30px;
            height: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.85rem;
            font-weight: 600;
        }}
        .quote {{
            text-align: center;
            padding: 3.5rem 1rem;
            background: #e8f1f5;
            border-top: 1px solid #dde6ea;
            border-bottom: 1px solid #dde6ea;
        }}
        .quote blockquote {{
            font-size: 1.9rem;
            font-weight: 300;
            max-width: 700px;
            margin: 0 auto 0.6rem;
        }}
        .quote .attr {{ font-size: 0.95rem; color: #5a6672; }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 2rem 0;
            background: #fff;
            border-radius: 12px;
            overflow: hidden;
        }}
        th, td {{
            padding: 1rem 1.2rem;
            text-align: left;
            border-bottom: 1px solid #dde6ea;
        }}
        th {{
            background: #e8f1f5;
            color: #2c5f7a;
            font-size: 0.92rem;
        }}
        footer {{
            text-align: center;
            padding: 3.5rem 1rem 2.5rem;
            border-top: 1px solid #dde6ea;
            background: #fff;
        }}
        footer .tagline {{ font-size: 1.05rem; margin-bottom: 1rem; }}
        footer a {{ color: #3b7ea1; text-decoration: none; }}
        input, textarea {{
            width: 100%;
            padding: 0.85rem 1rem;
            border: 1px solid #dde6ea;
            border-radius: 10px;
            margin-bottom: 1.2rem;
            font-family: inherit;
        }}
        label {{ display: block; font-size: 0.9rem; font-weight: 500; margin-bottom: 0.4rem; }}
    </style>
</head>
<body>
    <header>
        <div class="container header-inner">
            <div class="logo">
    		<img src="/logo.png" alt="SkinSense" style="height:50px;">
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
        <div class="container">
            <p class="tagline">Know Your Skin, Care Better</p>
            <p><a href="mailto:skinsense@example.com">skinsense@example.com</a></p>
            <p>Vidyalankar Institute of Technology, Mumbai, India</p>
            <p style="margin-top:1rem; font-size:0.85rem;">&copy; 2025 SkinSense</p>
        </div>
    </footer>
</body>
</html>"""