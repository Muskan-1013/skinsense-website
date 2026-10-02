# Local file checker for the SkinSense static website.
# Vercel publishes the HTML, CSS, JavaScript, and image files directly.
required_files = [
    "index.html",
    "style.css",
    "auth.js",
    "login.html",
    "signup.html",
    "logo.png",
    "images/dermasense-device.jpg",
    "images/insight-1.jpg",
    "images/insight-2.jpg",
    "images/insight-3.jpg",
    "images/testimonial-1.jpg",
    "images/testimonial-2.jpg",
    "images/testimonial-3.jpg"
]
def check_file(filename):
    try:
        file = open(filename, "rb")
        file.close()
        print(filename + " found.")
        return True
    except OSError:
        print(filename + " is missing.")
        return False
def check_website_files():
    all_files_found = True
    for filename in required_files:
        file_found = check_file(filename)
        if not file_found:
            all_files_found = False
    if all_files_found:
        print("")
        print("SkinSense files are ready to upload to GitHub.")
    else:
        print("")
        print("Add the missing files before uploading.")
check_website_files()