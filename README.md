# IZZAS SOLUTIONS — Business Website

A Flask website for IZZAS SOLUTIONS (electrical installations & electronics sales).

## Pages
- **Home** (`/`) — hero, services preview, how-it-works, WhatsApp CTA
- **About** (`/about`) — company story, values
- **Services** (`/services`) — full service list with details
- **Contact** (`/contact`) — contact form + phone/WhatsApp/email

Contact number (call & WhatsApp): **+254 719 123 028**

## Run locally

```bash
pip install flask
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Project structure

```
izzas/
├── app.py                  # Flask routes & content data
├── templates/
│   ├── base.html           # shared layout, nav, footer, WhatsApp button
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   └── contact.html
└── static/
    ├── css/style.css        # design system (charcoal / amber / copper)
    └── js/main.js
```

## Customizing

- **Company details, services, and process steps** are all defined at the
  top of `app.py` in the `COMPANY`, `SERVICES`, and `PROCESS` variables —
  edit the text there and it updates across every page automatically.
- **Contact form**: currently prints the enquiry to the console
  (`print(...)` in the `/contact` route in `app.py`). For a real deployment,
  replace that with code to save to a database or send an email/SMS.
- **Colors/fonts**: defined as CSS variables at the top of
  `static/css/style.css` under `:root`.

## Before going live

- Change `app.secret_key` in `app.py` to a random, a random value.
- Set `debug=False` in `app.run()`.
- Deploy behind a real WSGI server (e.g. gunicorn) — `app.run()` is for
  local development only.
- Consider adding a real email address and business registration details
  if required in your jurisdiction.
