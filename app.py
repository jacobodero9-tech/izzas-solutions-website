from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "izzas-solutions-dev-key"  # change this before real deployment

COMPANY = {
    "name": "IZZAS SOLUTIONS",
    "tagline": "Electrical Installations & Electronics Sales",
    "phone_display": "0719 123 028",
    "phone_intl": "254719123028",
    "whatsapp_link": "https://wa.me/254719123028",
    "email": "isaacochieng108@gmail.com",
    "location": "Rarieda, Siaya County, Kenya",
}

SERVICES = [
    {
        "code": "01",
        "name": "Electrical Installations",
        "desc": "Full house and commercial wiring, rewiring, and upgrades carried out to code.",
        "image": "networking.jpg",
        "features": ["New building wiring", "Rewiring & upgrades", "Fault finding & repairs", "DB board installation"]
    },
    {
        "code": "02",
        "name": "Electronics & Appliance Sales",
        "desc": "Genuine electronics and home appliances, sourced directly from distributors.",
        "image": "power-solutions.jpg",
        "features": ["TVs & sound systems", "Home appliances", "Cables & fittings", "Bulbs & security lights"]
    },
    {
        "code": "03",
        "name": "Maintenance & Repairs",
        "desc": "Scheduled maintenance and emergency call-outs to keep your power running.",
        "image": "security-systems.jpg",
        "features": ["Preventive maintenance", "Emergency call-outs 24/7", "Meter separation", "Tripping breaker fixes"]
    },
    {
        "code": "04",
        "name": "Solar & Backup Power",
        "desc": "Solar panel setup and backup power solutions for homes, shops & farms in Siaya.",
        "image": "access-control.jpg",
        "features": ["Solar panel installation", "Battery backup systems", "Hybrid inverter setup", "Solar water heating"]
    },
    {
        "code": "05",
        "name": "CCTV & Security Systems",
        "desc": "Protect your property with HD cameras you can watch from your phone anywhere.",
        "image": "fire-safety.jpg",
        "features": ["4CH & 8CH CCTV installation", "Remote phone viewing", "Electric fence wiring", "Video doorbell setup"]
    },
    {
        "code": "06",
        "name": "Water Pump Solutions",
        "desc": "Submersible and surface pump installation for boreholes, tanks & irrigation.",
        "image": "maintenance.jpg",
        "features": ["Borehole pump installation", "Automatic pump control", "Tank float switch wiring", "Pump repair & servicing"]
    }
]

PROCESS = [
    {"step": "1", "title": "Call or WhatsApp us", "desc": "Tell us what you need — installation, repair, or a product."},
    {"step": "2", "title": "Site visit or quote", "desc": "We assess the job or give you a price on the spot."},
    {"step": "3", "title": "We get to work", "desc": "Certified installation or same-day product delivery."},
    {"step": "4", "title": "Test & handover", "desc": "Everything tested for safety before we sign off."},
]


@app.context_processor
def inject_company():
    return {"company": COMPANY}


@app.route("/")
def home():
    return render_template("index.html", services=SERVICES[:3], process=PROCESS)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html", services=SERVICES)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not phone or not message:
            flash("Please fill in all fields before sending.", "error")
            return redirect(url_for("contact"))

        # In production: save to a database or send an email/SMS here.
        print(f"New enquiry -> Name: {name}, Phone: {phone}, Message: {message}")
        flash("Thanks! Your message has been received. We'll call you back shortly.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
