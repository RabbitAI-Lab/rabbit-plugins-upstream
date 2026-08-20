#!/usr/bin/env python3
"""
landing_builder.py — Generate beautiful, production-quality landing pages from a
simple text description. Pure Python stdlib only. Output is a single standalone
HTML file with embedded CSS (only external dep is Google Fonts).

Usage:
  python landing_builder.py build --name 'TaskFlow' --desc 'AI task management' --theme saas --color '#6366f1'
  python landing_builder.py build --config product.json
  echo 'Coffee shop in Portland called Brew & Co' | python landing_builder.py --auto
  python landing_builder.py build           # interactive

Author: Denis Voronin
License: MIT
Version: 1.0.0
"""

import argparse
import colorsys
import hashlib
import json
import math
import os
import re
import sys
from html import escape as html_escape
from textwrap import dedent

VERSION = "1.0.0"

# ---------------------------------------------------------------------------
# THEMES
# ---------------------------------------------------------------------------

THEMES = {
    "saas": {
        "fonts": ("Poppins", "Inter"),
        "hero_img": "https://images.unsplash.com/photo-1551434678-e076c223a692?w=1200&q=80",
        "sections": ["hero", "logos", "features", "how", "pricing", "testimonials", "cta", "faq", "footer"],
        "feature_icons": ["⚡", "🔒", "📊", "🤝", "🎯", "🔄"],
        "features": [
            ("Lightning Fast", "Built for speed — every interaction is optimized for sub-100ms response times."),
            ("Bank-Grade Security", "SOC 2 Type II compliant with end-to-end encryption and SSO support."),
            ("Deep Analytics", "Real-time dashboards that turn raw data into actionable insights."),
            ("Seamless Collaboration", "Built-in commenting, mentions, and shared workspaces for your team."),
            ("Smart Automation", "Automate repetitive workflows and let AI handle the busywork."),
            ("100+ Integrations", "Connect Slack, GitHub, Stripe, and 100+ tools your team already uses."),
        ],
        "pricing": [
            ("Starter", "$0", ["/mo", "For individuals getting started"], ["Up to 3 projects", "Basic analytics", "Community support", "1 GB storage"]),
            ("Pro", "$29", ["/mo", "For growing teams that need more"], ["Unlimited projects", "Advanced analytics", "Priority support", "100 GB storage", "Custom integrations", "API access"]),
            ("Enterprise", "Custom", ["", "For large organizations"], ["Everything in Pro", "Dedicated manager", "99.9% SLA", "SSO & SAML", "Audit logs", "Custom contracts"]),
        ],
        "testimonials": [
            ("Sarah Chen", "VP Engineering, Acme Corp", "This transformed how our team ships. We cut delivery time by 40%."),
            ("Marcus Rivera", "CTO, Boltline", "The automation features alone save us 15 hours a week. Incredible."),
            ("Aisha Patel", "Founder, NimbleLabs", "Best decision we made this year. The analytics are next level."),
        ],
        "cta_title": "Start your free trial today",
        "cta_subtitle": "No credit card required. Set up in 2 minutes.",
        "nav": ["Features", "Pricing", "Testimonials", "FAQ"],
        "footer_tagline": "Build better products, faster.",
    },
    "startup": {
        "fonts": ("Poppins", "Inter"),
        "hero_img": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1200&q=80",
        "sections": ["hero", "logos", "features", "how", "testimonials", "cta", "footer"],
        "feature_icons": ["🚀", "💡", "📈", "🌍", "⚙️", "🛡️"],
        "features": [
            ("Move Fast", "Ship features at startup speed without sacrificing quality or stability."),
            ("Bold Ideas", "We challenge the status quo and build what others say is impossible."),
            ("Growth Engine", "Data-driven growth tools that scale with you from 0 to 1M users."),
            ("Global Reach", "Available in 30+ countries with multi-currency and localization support."),
            ("Powerful APIs", "Developer-first architecture with clean, documented REST and GraphQL APIs."),
            ("Future-Proof", "Built on cutting-edge tech that scales infinitely as you grow."),
        ],
        "testimonials": [
            ("James Liu", "Early Adopter", "This is the tool I wish I had 5 years ago."),
            ("Priya Sharma", "Growth Lead, Scaleup.io", "We tripled our signups in the first month."),
            ("Tom O'Brien", "Angel Investor", "The most promising platform I've seen this year."),
        ],
        "cta_title": "Join the revolution",
        "cta_subtitle": "Be the first to experience the future.",
        "nav": ["Features", "Testimonials"],
        "footer_tagline": "Building the future, today.",
    },
    "portfolio": {
        "fonts": ("Poppins", "Inter"),
        "hero_img": "https://images.unsplash.com/photo-1517180102446-f3ece451e9d8?w=1200&q=80",
        "sections": ["hero", "features", "how", "cta", "footer"],
        "feature_icons": ["🎨", "✨", "📐", "📸"],
        "features": [
            ("Brand Identity", "Logos, color systems, and guidelines that make your brand unforgettable."),
            ("UI/UX Design", "User-centered interfaces that are beautiful, accessible, and conversion-focused."),
            ("Art Direction", "Photography, illustration, and visual storytelling that captivates."),
            ("Motion Design", "Micro-interactions and animations that bring your product to life."),
        ],
        "testimonials": [],
        "cta_title": "Let's work together",
        "cta_subtitle": "Available for freelance projects and collaborations.",
        "nav": ["Work", "About", "Contact"],
        "footer_tagline": "Design that matters.",
    },
    "restaurant": {
        "fonts": ("Poppins", "Inter"),
        "hero_img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&q=80",
        "sections": ["hero", "features", "testimonials", "cta", "footer"],
        "feature_icons": ["🍽️", "🍷", "👨‍🍳", "🌿"],
        "features": [
            ("Seasonal Menu", "Farm-to-table dishes crafted with the freshest local ingredients."),
            ("Curated Wine List", "Over 200 selections hand-picked by our certified sommeliers."),
            ("Award-Winning Chef", "Michelin-recognized cuisine from our executive chef."),
            ("Cozy Atmosphere", "Warm, intimate setting perfect for any occasion."),
        ],
        "testimonials": [
            ("Food Critic Magazine", "★★★★★", "The best dining experience I've had this year. Every dish is a masterpiece."),
            ("Emily Watson", "Food Blogger", "An absolute gem. The flavors, the service, the ambiance — perfection."),
            ("Local Eats Guide", "Editor's Choice", "Consistently excellent. A must-visit destination restaurant."),
        ],
        "cta_title": "Reserve Your Table",
        "cta_subtitle": "Book your unforgettable dining experience today.",
        "nav": ["Menu", "About", "Reservations"],
        "footer_tagline": "Where every meal is a memory.",
    },
    "fitness": {
        "fonts": ("Poppins", "Inter"),
        "hero_img": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1200&q=80",
        "sections": ["hero", "features", "pricing", "testimonials", "cta", "footer"],
        "feature_icons": ["💪", "🏃", "🥗", "📈", "🔥", "⏱️"],
        "features": [
            ("Expert Coaches", "Certified trainers who create personalized plans just for you."),
            ("Modern Equipment", "State-of-the-art machines and free weights for every workout style."),
            ("Nutrition Plans", "Custom meal plans designed by registered dietitians."),
            ("Progress Tracking", "Real-time analytics that show your improvement week over week."),
            ("Group Classes", "Over 50 weekly classes from HIIT to yoga to spin."),
            ("24/7 Access", "Work out on your schedule with round-the-clock gym access."),
        ],
        "pricing": [
            ("Day Pass", "$15", ["", "Try us out"], ["Full gym access", "1 group class", "Locker rental"]),
            ("Monthly", "$49", ["/mo", "Most popular"], ["Unlimited gym access", "All group classes", "1 PT session", "Nutrition guide"]),
            ("Annual", "$399", ["/yr", "Best value"], ["Everything in Monthly", "Weekly PT sessions", "Custom meal plan", "Free guest passes"]),
        ],
        "testimonials": [
            ("Jake Morrison", "Lost 30 lbs", "The coaches genuinely care. I'm in the best shape of my life."),
            ("Lisa Park", "Marathon Runner", "The training programs took 20 minutes off my PR."),
            ("Dev Williams", "Member since 2022", "Best gym I've ever joined. The community is incredible."),
        ],
        "cta_title": "Start Your Transformation",
        "cta_subtitle": "First class is on us. No commitment required.",
        "nav": ["Classes", "Pricing", "About"],
        "footer_tagline": "Stronger every day.",
    },
    "agency": {
        "fonts": ("Poppins", "Inter"),
        "hero_img": "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=1200&q=80",
        "sections": ["hero", "logos", "features", "how", "testimonials", "cta", "footer"],
        "feature_icons": ["🎯", "📈", "🎨", "💡", "🤝", "🏆"],
        "features": [
            ("Brand Strategy", "Positioning, messaging, and identity that sets you apart from competitors."),
            ("Digital Marketing", "SEO, PPC, and social campaigns that drive measurable ROI."),
            ("Creative Design", "Award-winning design that captures attention and converts visitors."),
            ("Web Development", "Fast, responsive websites built with modern best practices."),
            ("Content Creation", "Compelling copy, video, and visual content that tells your story."),
            ("Analytics & Reporting", "Transparent dashboards that show exactly where your budget goes."),
        ],
        "testimonials": [
            ("David Kim", "CEO, TechFlow", "We saw a 300% increase in qualified leads in just 3 months."),
            ("Sofia Mendez", "Marketing Director", "Their creative team is unmatched. Our brand has never looked better."),
            ("Robert Chen", "Founder, DataHive", "The ROI speaks for itself. Best agency partnership we've ever had."),
        ],
        "cta_title": "Let's Grow Together",
        "cta_subtitle": "Book a free strategy session with our team.",
        "nav": ["Services", "Work", "Contact"],
        "footer_tagline": "Your growth is our mission.",
    },
    "ecommerce": {
        "fonts": ("Poppins", "Inter"),
        "hero_img": "https://images.unsplash.com/photo-1556742502-ec7c0e9f34b1?w=1200&q=80",
        "sections": ["hero", "features", "pricing", "testimonials", "cta", "footer"],
        "feature_icons": ["🛍️", "🚚", "💳", "🎁", "⭐", "🔄"],
        "features": [
            ("Premium Products", "Carefully curated items that meet our highest quality standards."),
            ("Free Fast Shipping", "Free 2-day shipping on all orders over $50."),
            ("Secure Checkout", "Shop with confidence — encrypted payments and buyer protection."),
            ("Gift Cards", "Perfect gifts for any occasion, available in any amount."),
            ("5-Star Rated", "Over 10,000 verified reviews from happy customers."),
            ("Easy Returns", "30-day no-questions-asked return policy on everything."),
        ],
        "testimonials": [
            ("Happy Customer", "Verified Buyer", "Amazing quality and super fast shipping. Will buy again!"),
            ("Sarah J.", "Verified Buyer", "Best online shopping experience I've had. Highly recommend."),
            ("Mike R.", "Verified Buyer", "Products exceeded expectations. Customer service is top notch."),
        ],
        "cta_title": "Shop the Collection",
        "cta_subtitle": "Free shipping on orders over $50.",
        "nav": ["Shop", "New Arrivals", "Sale"],
        "footer_tagline": "Quality you can trust.",
    },
}

# Default features (used when auto-generating from text)
DEFAULT_FEATURES = [
    ("Powerful & Intuitive", "Everything you need in one elegant package. No learning curve required."),
    ("Built for Scale", "From your first user to your millionth — we handle the growth with you."),
    ("Secure by Design", "Enterprise-grade security baked in from day one. Your data is safe."),
    ("Beautiful by Default", "Stunning interfaces that your users will love from the first click."),
    ("24/7 Support", "Real humans, always available. We're here when you need us most."),
    ("Integrates Everywhere", "Connects with the tools you already use and love. Zero friction."),
]

DEFAULT_NAV = ["Features", "Pricing", "Testimonials", "FAQ"]


# ---------------------------------------------------------------------------
# COLOR SCHEME GENERATION
# ---------------------------------------------------------------------------

def hex_to_rgb(hex_color: str) -> tuple:
    """Convert hex string to (r, g, b) tuple, each 0-255."""
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb: tuple) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def rgb_to_hsl(rgb: tuple) -> tuple:
    r, g, b = [x / 255.0 for x in rgb]
    return colorsys.rgb_to_hls(r, g, b)  # returns (H, L, S) — note: HLS not HSL


def hls_to_rgb(h, l, s) -> tuple:
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return (int(r * 255), int(g * 255), int(b * 255))


def generate_palette(seed_hex: str) -> dict:
    """
    Generate a full color palette from a single seed color.
    Returns dict with keys suitable for CSS custom properties.
    """
    base_rgb = hex_to_rgb(seed_hex)
    h, l, s = rgb_to_hsl(base_rgb)

    def var(lh, ls, ll):
        rgb = hls_to_rgb(lh, ll, ls)
        return rgb_to_hex(rgb)

    return {
        "primary": seed_hex,
        "primary_light": var(h, min(s, 0.8), min(l + 0.10, 0.92)),
        "primary_dark": var(h, min(s, 0.9), max(l - 0.12, 0.08)),
        "primary_50": var(h, s * 0.3, 0.97),
        "primary_100": var(h, s * 0.4, 0.93),
        "accent": var((h + 0.13) % 1.0, min(s + 0.05, 1.0), min(l + 0.03, 0.72)),
        "accent_2": var((h + 0.62) % 1.0, min(s, 0.85), min(l + 0.05, 0.65)),
        "gradient_start": seed_hex,
        "gradient_end": var((h + 0.08) % 1.0, min(s + 0.1, 1.0), max(l - 0.05, 0.30)),
        "gradient_accent": var((h + 0.15) % 1.0, min(s, 0.95), min(l + 0.05, 0.65)),
    }


# ---------------------------------------------------------------------------
# AUTO MODE — parse plain text descriptions
# ---------------------------------------------------------------------------

THEME_KEYWORDS = {
    "restaurant": ["restaurant", "cafe", "coffee", "food", "dining", "bar", "bakery", "kitchen", "menu", "chef", "eatery", "brew", "pizza", "sushi"],
    "fitness": ["gym", "fitness", "workout", "yoga", "health", "training", "crossfit", "pilates", "personal trainer", "wellness"],
    "ecommerce": ["shop", "store", "ecommerce", "e-commerce", "retail", "boutique", "fashion", "clothing", "product"],
    "agency": ["agency", "marketing", "consulting", "branding", "advertising", "studio", "design firm"],
    "portfolio": ["portfolio", "designer", "photographer", "freelance", "artist", "creative"],
    "startup": ["startup", "venture", "founder", "launch", "early stage", "incubator"],
    "saas": ["saas", "software", "app", "platform", "ai", "crm", "api", "dashboard", "automation", "b2b", "cloud", "developer", "task", "project management", "analytics"],
}

THEME_COLORS = {
    "saas": "#6366f1",
    "startup": "#8b5cf6",
    "portfolio": "#ec4899",
    "restaurant": "#dc2626",
    "fitness": "#f97316",
    "agency": "#0ea5e9",
    "ecommerce": "#10b981",
}


def detect_theme(text: str) -> str:
    text_lower = text.lower()
    scores = {}
    for theme, keywords in THEME_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in text_lower)
        if score:
            scores[theme] = score
    if scores:
        return max(scores, key=scores.get)
    return "saas"


def extract_name(text: str) -> str:
    """Try to extract a business/product name from free text."""
    text_lower = text.lower()
    # Pattern: "called X", "named X"
    for pattern in [r"called\s+([A-Z][A-Za-z0-9\s&'-]+?)(?:$|[,.\n])",
                    r"named\s+([A-Z][A-Za-z0-9\s&'-]+?)(?:$|[,.\n])",
                    r"for\s+([A-Z][A-Za-z0-9\s&'-]+?)(?:$|[,.\n])"]:
        m = re.search(pattern, text.strip())
        if m:
            return m.group(1).strip()
    # Check for capitalized words that might be a name
    words = text.strip().split()
    caps = [w for w in words if re.match(r"^[A-Z][a-z]+", w)]
    if caps:
        # Join consecutive capitalized words
        name_parts = []
        for w in words:
            if re.match(r"^[A-Z][A-Za-z0-9&'-]+$", w):
                name_parts.append(w)
            else:
                if name_parts:
                    break
        if name_parts:
            return " ".join(name_parts)
    # Fallback
    return "Your Brand"


def auto_parse(text: str) -> dict:
    """Parse a free-text description into config fields."""
    text = text.strip()
    name = extract_name(text)
    theme = detect_theme(text)
    color = THEME_COLORS.get(theme, "#6366f1")
    return {
        "name": name,
        "description": text,
        "theme": theme,
        "color": color,
    }


# ---------------------------------------------------------------------------
# HTML GENERATION
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def build_css(config: dict, palette: dict, fonts: tuple) -> str:
    head_font, body_font = fonts
    p = palette
    return f"""
:root {{
  --primary: {p['primary']};
  --primary-light: {p['primary_light']};
  --primary-dark: {p['primary_dark']};
  --primary-50: {p['primary_50']};
  --primary-100: {p['primary_100']};
  --accent: {p['accent']};
  --accent-2: {p['accent_2']};
  --gradient-start: {p['gradient_start']};
  --gradient-end: {p['gradient_end']};
  --gradient-accent: {p['gradient_accent']};

  --text-primary: #0f172a;
  --text-secondary: #475569;
  --text-light: #94a3b8;
  --text-white: #f8fafc;
  --bg-primary: #ffffff;
  --bg-secondary: #f8fafc;
  --bg-dark: #0f172a;
  --bg-card: #ffffff;
  --border-color: #e2e8f0;
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.07), 0 2px 4px -2px rgba(0,0,0,0.05);
  --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.08), 0 4px 6px -4px rgba(0,0,0,0.05);
  --shadow-xl: 0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.05);
  --shadow-glow: 0 0 40px rgba({int(p['primary'][1:3],16)},{int(p['primary'][3:5],16)},{int(p['primary'][5:7],16)},0.15);
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --radius-xl: 28px;
  --font-head: '{head_font}', system-ui, -apple-system, sans-serif;
  --font-body: '{body_font}', system-ui, -apple-system, sans-serif;
  --max-width: 1200px;
  --transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}}

*, *::before, *::after {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}

html {{
  scroll-behavior: smooth;
  font-size: 16px;
}}

body {{
  font-family: var(--font-body);
  color: var(--text-primary);
  background: var(--bg-primary);
  line-height: 1.6;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}}

h1, h2, h3, h4, h5, h6 {{
  font-family: var(--font-head);
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.02em;
}}

a {{
  color: inherit;
  text-decoration: none;
  transition: color var(--transition);
}}

img {{
  max-width: 100%;
  height: auto;
  display: block;
}}

.container {{
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 24px;
}}

.gradient-text {{
  background: linear-gradient(135deg, var(--gradient-start), var(--gradient-accent));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
}}

.section-tag {{
  display: inline-block;
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--primary);
  background: var(--primary-50);
  padding: 6px 16px;
  border-radius: 100px;
  margin-bottom: 16px;
  letter-spacing: 0.03em;
  text-transform: uppercase;
}}

/* ======== NAVBAR ======== */
.navbar {{
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  padding: 16px 0;
  transition: all var(--transition);
  background: transparent;
}}

.navbar.scrolled {{
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  box-shadow: var(--shadow-sm);
  padding: 10px 0;
}}

.navbar .container {{
  display: flex;
  align-items: center;
  justify-content: space-between;
}}

.nav-logo {{
  font-family: var(--font-head);
  font-size: 1.4rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  display: flex;
  align-items: center;
  gap: 8px;
}}

.nav-logo .logo-dot {{
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 0.9rem;
  font-weight: 800;
  box-shadow: var(--shadow-md);
}}

.nav-links {{
  display: flex;
  align-items: center;
  gap: 32px;
  list-style: none;
}}

.nav-links a {{
  font-weight: 500;
  font-size: 0.95rem;
  color: var(--text-secondary);
  position: relative;
}}

.nav-links a::after {{
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--primary);
  transition: width var(--transition);
}}

.nav-links a:hover {{ color: var(--primary); }}
.nav-links a:hover::after {{ width: 100%; }}

.nav-cta {{
  background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
  color: white !important;
  padding: 10px 24px;
  border-radius: 100px;
  font-weight: 600 !important;
  box-shadow: var(--shadow-md);
  transition: transform var(--transition), box-shadow var(--transition);
}}

.nav-cta:hover {{
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}}

.nav-cta::after {{ display: none; }}

.hamburger {{
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
  z-index: 1001;
}}

.hamburger span {{
  width: 24px;
  height: 2px;
  background: var(--text-primary);
  border-radius: 2px;
  transition: all var(--transition);
}}

.hamburger.active span:nth-child(1) {{ transform: translateY(7px) rotate(45deg); }}
.hamburger.active span:nth-child(2) {{ opacity: 0; }}
.hamburger.active span:nth-child(3) {{ transform: translateY(-7px) rotate(-45deg); }}

/* ======== HERO ======== */
.hero {{
  position: relative;
  padding: 140px 0 80px;
  overflow: hidden;
  background: var(--bg-secondary);
}}

.hero::before {{
  content: '';
  position: absolute;
  top: -200px;
  right: -200px;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, var(--primary-100) 0%, transparent 70%);
  border-radius: 50%;
  z-index: 0;
}}

.hero::after {{
  content: '';
  position: absolute;
  bottom: -150px;
  left: -150px;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, var(--primary-50) 0%, transparent 70%);
  border-radius: 50%;
  z-index: 0;
}}

.hero .container {{
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
}}

.hero-content {{
  opacity: 0;
  transform: translateY(30px);
  animation: fadeInUp 0.8s ease forwards;
}}

.hero h1 {{
  font-size: 3.5rem;
  margin-bottom: 24px;
  letter-spacing: -0.03em;
}}

.hero h1 .gradient-text {{
  display: inline;
}}

.hero-subtitle {{
  font-size: 1.2rem;
  color: var(--text-secondary);
  margin-bottom: 36px;
  max-width: 500px;
}}

.hero-buttons {{
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}}

.btn {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 14px 32px;
  border-radius: 100px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all var(--transition);
  border: none;
  font-family: var(--font-body);
}}

.btn-primary {{
  background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
  color: white;
  box-shadow: var(--shadow-md);
}}

.btn-primary:hover {{
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg), var(--shadow-glow);
}}

.btn-secondary {{
  background: var(--bg-primary);
  color: var(--text-primary);
  border: 2px solid var(--border-color);
}}

.btn-secondary:hover {{
  border-color: var(--primary);
  color: var(--primary);
  transform: translateY(-2px);
}}

.hero-image {{
  position: relative;
  opacity: 0;
  transform: translateY(30px);
  animation: fadeInUp 0.8s ease 0.2s forwards;
}}

.hero-image img {{
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-xl);
  width: 100%;
}}

.hero-image::after {{
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--radius-xl);
  background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
  opacity: 0.08;
  z-index: 1;
}}

/* ======== LOGO BAR ======== */
.logo-bar {{
  padding: 48px 0;
  text-align: center;
  border-bottom: 1px solid var(--border-color);
}}

.logo-bar p {{
  font-size: 0.85rem;
  color: var(--text-light);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 24px;
  font-weight: 600;
}}

.logo-row {{
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 48px;
  flex-wrap: wrap;
}}

.logo-row span {{
  font-family: var(--font-head);
  font-weight: 700;
  font-size: 1.4rem;
  color: var(--text-light);
  opacity: 0.7;
  transition: opacity var(--transition);
}}

.logo-row span:hover {{ opacity: 1; }}

/* ======== FEATURES ======== */
.features {{
  padding: 100px 0;
  background: var(--bg-primary);
}}

.section-header {{
  text-align: center;
  max-width: 700px;
  margin: 0 auto 60px;
}}

.section-header h2 {{
  font-size: 2.5rem;
  margin-bottom: 16px;
}}

.section-header p {{
  font-size: 1.15rem;
  color: var(--text-secondary);
}}

.features-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
}}

.feature-card {{
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 36px;
  transition: all var(--transition);
  position: relative;
  overflow: hidden;
}}

.feature-card::before {{
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--gradient-start), var(--gradient-end));
  transform: scaleX(0);
  transform-origin: left;
  transition: transform var(--transition);
}}

.feature-card:hover {{
  transform: translateY(-8px);
  box-shadow: var(--shadow-xl);
  border-color: transparent;
}}

.feature-card:hover::before {{
  transform: scaleX(1);
}}

.feature-icon {{
  width: 56px;
  height: 56px;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.6rem;
  background: var(--primary-50);
  margin-bottom: 20px;
  transition: transform var(--transition);
}}

.feature-card:hover .feature-icon {{
  transform: scale(1.1) rotate(-5deg);
}}

.feature-card h3 {{
  font-size: 1.25rem;
  margin-bottom: 10px;
}}

.feature-card p {{
  color: var(--text-secondary);
  font-size: 0.95rem;
}}

/* ======== HOW IT WORKS ======== */
.how {{
  padding: 100px 0;
  background: var(--bg-secondary);
}}

.steps-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
}}

.step {{
  text-align: center;
  position: relative;
}}

.step-number {{
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
  color: white;
  font-family: var(--font-head);
  font-size: 1.5rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 24px;
  box-shadow: var(--shadow-lg);
}}

.step h3 {{
  font-size: 1.3rem;
  margin-bottom: 10px;
}}

.step p {{
  color: var(--text-secondary);
  font-size: 0.95rem;
  max-width: 280px;
  margin: 0 auto;
}}

/* ======== PRICING ======== */
.pricing {{
  padding: 100px 0;
}}

.pricing-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
  align-items: stretch;
}}

.pricing-card {{
  background: var(--bg-card);
  border: 2px solid var(--border-color);
  border-radius: var(--radius-xl);
  padding: 40px;
  display: flex;
  flex-direction: column;
  transition: all var(--transition);
  position: relative;
}}

.pricing-card.featured {{
  border-color: var(--primary);
  box-shadow: var(--shadow-xl), var(--shadow-glow);
  transform: scale(1.03);
}}

.pricing-card.featured .badge {{
  position: absolute;
  top: -14px;
  left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
  color: white;
  font-size: 0.8rem;
  font-weight: 600;
  padding: 6px 20px;
  border-radius: 100px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  white-space: nowrap;
}}

.pricing-card:hover {{
  transform: translateY(-5px);
  box-shadow: var(--shadow-xl);
}}

.pricing-card.featured:hover {{
  transform: scale(1.03) translateY(-5px);
}}

.pricing-card h3 {{
  font-size: 1.3rem;
  margin-bottom: 8px;
}}

.pricing-card .plan-desc {{
  font-size: 0.9rem;
  color: var(--text-light);
  margin-bottom: 24px;
}}

.price {{
  font-family: var(--font-head);
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: 4px;
}}

.price .period {{
  font-size: 1rem;
  font-weight: 500;
  color: var(--text-light);
}}

.pricing-card ul {{
  list-style: none;
  margin: 24px 0;
  flex-grow: 1;
}}

.pricing-card ul li {{
  padding: 8px 0;
  font-size: 0.95rem;
  color: var(--text-secondary);
  display: flex;
  align-items: center;
  gap: 10px;
}}

.pricing-card ul li::before {{
  content: '✓';
  color: var(--primary);
  font-weight: 800;
  font-size: 1.1rem;
}}

.pricing-card .btn {{
  width: 100%;
  margin-top: auto;
}}

/* ======== TESTIMONIALS ======== */
.testimonials {{
  padding: 100px 0;
  background: var(--bg-secondary);
}}

.testimonials-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
}}

.testimonial-card {{
  background: var(--bg-card);
  border-radius: var(--radius-lg);
  padding: 36px;
  box-shadow: var(--shadow-sm);
  border: 1px solid var(--border-color);
  transition: all var(--transition);
  position: relative;
}}

.testimonial-card::before {{
  content: '"';
  position: absolute;
  top: 16px;
  right: 24px;
  font-size: 4rem;
  font-family: Georgia, serif;
  color: var(--primary-100);
  line-height: 1;
  z-index: 0;
}}

.testimonial-card:hover {{
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}}

.stars {{
  color: #fbbf24;
  font-size: 1.1rem;
  margin-bottom: 16px;
  position: relative;
  z-index: 1;
}}

.testimonial-text {{
  font-size: 1rem;
  color: var(--text-primary);
  margin-bottom: 24px;
  position: relative;
  z-index: 1;
  font-style: italic;
}}

.testimonial-author {{
  display: flex;
  align-items: center;
  gap: 12px;
  position: relative;
  z-index: 1;
}}

.author-avatar {{
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--gradient-start), var(--gradient-accent));
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 1rem;
}}

.author-info strong {{
  display: block;
  font-size: 0.95rem;
}}

.author-info span {{
  font-size: 0.85rem;
  color: var(--text-light);
}}

/* ======== CTA SECTION ======== */
.cta-section {{
  padding: 100px 0;
  position: relative;
  overflow: hidden;
}}

.cta-box {{
  background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
  border-radius: var(--radius-xl);
  padding: 70px 48px;
  text-align: center;
  position: relative;
  overflow: hidden;
  box-shadow: var(--shadow-xl);
}}

.cta-box::before {{
  content: '';
  position: absolute;
  top: -50%;
  right: -20%;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 60%);
  border-radius: 50%;
}}

.cta-box::after {{
  content: '';
  position: absolute;
  bottom: -50%;
  left: -20%;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
  border-radius: 50%;
}}

.cta-box h2 {{
  font-size: 2.5rem;
  color: white;
  margin-bottom: 16px;
  position: relative;
  z-index: 1;
}}

.cta-box p {{
  color: rgba(255, 255, 255, 0.9);
  font-size: 1.15rem;
  margin-bottom: 36px;
  position: relative;
  z-index: 1;
}}

.cta-box .btn-primary {{
  background: white;
  color: var(--primary);
  position: relative;
  z-index: 1;
}}

.cta-box .btn-primary:hover {{
  background: var(--text-white);
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}}

/* ======== FAQ ======== */
.faq {{
  padding: 100px 0;
}}

.faq-list {{
  max-width: 760px;
  margin: 0 auto;
}}

.faq-item {{
  border-bottom: 1px solid var(--border-color);
  padding: 0;
}}

.faq-question {{
  width: 100%;
  text-align: left;
  background: none;
  border: none;
  padding: 24px 0;
  font-family: var(--font-head);
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--text-primary);
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: color var(--transition);
}}

.faq-question:hover {{ color: var(--primary); }}

.faq-question .icon {{
  font-size: 1.5rem;
  color: var(--primary);
  transition: transform var(--transition);
}}

.faq-question.active .icon {{ transform: rotate(45deg); }}

.faq-answer {{
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease, padding 0.3s ease;
  color: var(--text-secondary);
  font-size: 0.95rem;
  line-height: 1.7;
}}

.faq-answer.open {{
  max-height: 300px;
  padding-bottom: 24px;
}}

/* ======== FOOTER ======== */
.footer {{
  background: var(--bg-dark);
  color: var(--text-light);
  padding: 70px 0 30px;
}}

.footer-grid {{
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 40px;
  margin-bottom: 50px;
}}

.footer-brand .nav-logo {{
  color: white;
  margin-bottom: 16px;
}}

.footer-brand p {{
  font-size: 0.95rem;
  max-width: 280px;
  margin-bottom: 20px;
}}

.social-links {{
  display: flex;
  gap: 12px;
}}

.social-links a {{
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  transition: all var(--transition);
}}

.social-links a:hover {{
  background: var(--primary);
  transform: translateY(-3px);
}}

.footer-col h4 {{
  color: white;
  font-size: 1rem;
  margin-bottom: 16px;
}}

.footer-col ul {{
  list-style: none;
}}

.footer-col ul li {{
  margin-bottom: 10px;
}}

.footer-col ul li a {{
  font-size: 0.9rem;
  color: var(--text-light);
  transition: color var(--transition);
}}

.footer-col ul li a:hover {{
  color: white;
}}

.footer-bottom {{
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 30px;
  text-align: center;
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.5);
}}

/* ======== ANIMATIONS ======== */
@keyframes fadeInUp {{
  to {{
    opacity: 1;
    transform: translateY(0);
  }}
}}

.reveal {{
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}}

.reveal.visible {{
  opacity: 1;
  transform: translateY(0);
}}

.reveal-delay-1 {{ transition-delay: 0.1s; }}
.reveal-delay-2 {{ transition-delay: 0.2s; }}
.reveal-delay-3 {{ transition-delay: 0.3s; }}

/* ======== RESPONSIVE ======== */
@media (max-width: 968px) {{
  .hero .container {{
    grid-template-columns: 1fr;
    gap: 40px;
  }}

  .hero h1 {{ font-size: 2.6rem; }}

  .hero-image {{
    order: -1;
    max-width: 500px;
    margin: 0 auto;
  }}

  .features-grid,
  .steps-grid,
  .pricing-grid,
  .testimonials-grid {{
    grid-template-columns: repeat(2, 1fr);
  }}

  .footer-grid {{
    grid-template-columns: 1fr 1fr;
  }}
}}

@media (max-width: 700px) {{
  .nav-links {{
    position: fixed;
    top: 0;
    right: -100%;
    width: 75%;
    max-width: 320px;
    height: 100vh;
    background: white;
    flex-direction: column;
    justify-content: flex-start;
    padding: 80px 30px 30px;
    gap: 20px;
    transition: right 0.4s ease;
    box-shadow: -10px 0 40px rgba(0,0,0,0.1);
    align-items: flex-start;
  }}

  .nav-links.active {{
    right: 0;
  }}

  .nav-links a {{
    font-size: 1.1rem;
  }}

  .hamburger {{ display: flex; }}

  .hero {{
    padding: 120px 0 60px;
  }}

  .hero h1 {{ font-size: 2rem; }}
  .hero-subtitle {{ font-size: 1rem; }}
  .section-header h2,
  .cta-box h2 {{ font-size: 1.8rem; }}

  .features-grid,
  .steps-grid,
  .pricing-grid,
  .testimonials-grid {{
    grid-template-columns: 1fr;
  }}

  .pricing-card.featured {{
    transform: none;
  }}

  .pricing-card.featured:hover {{
    transform: translateY(-5px);
  }}

  .footer-grid {{
    grid-template-columns: 1fr;
    gap: 30px;
  }}

  .cta-box {{
    padding: 50px 24px;
  }}

  .feature-card,
  .testimonial-card {{
    padding: 28px;
  }}
}}

/* Mobile nav overlay */
.nav-overlay {{
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.5);
  z-index: 999;
  opacity: 0;
  transition: opacity 0.3s ease;
}}

.nav-overlay.active {{
  display: block;
  opacity: 1;
}}
"""


def generate_logo_initial(name: str) -> str:
    words = name.strip().split()
    if len(words) >= 2:
        return (words[0][0] + words[1][0]).upper()
    return name[0:2].upper()


def render_nav(config: dict, nav_items: list) -> str:
    name = config.get("name", "Brand")
    items_html = "\n".join(
        f'      <li><a href="#{slugify(item)}">{html_escape(item)}</a></li>' for item in nav_items
    )
    items_html += '\n      <li><a href="#cta" class="nav-cta">Get Started</a></li>'
    return f"""
  <nav class="navbar" id="navbar">
    <div class="container">
      <a href="#" class="nav-logo">
        <span class="logo-dot">{generate_logo_initial(name)}</span>
        {html_escape(name)}
      </a>
      <ul class="nav-links" id="navLinks">
{items_html}
      </ul>
      <button class="hamburger" id="hamburger" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>
  <div class="nav-overlay" id="navOverlay"></div>"""


def render_hero(config: dict, theme_conf: dict) -> str:
    name = config.get("name", "Your Brand")
    desc = config.get("description", "")
    tagline = config.get("tagline", "")
    hero_img = config.get("hero_img") or theme_conf.get("hero_img", "")

    # Generate headline from name + description
    if tagline:
        headline = tagline
    elif desc:
        # Try to craft a punchy headline
        headline = desc
    else:
        headline = f"Welcome to {name}"

    # Split for gradient text effect on part of headline
    words = headline.split()
    if len(words) > 2:
        first_part = " ".join(words[:len(words) // 2])
        second_part = " ".join(words[len(words) // 2:])
        headline_html = f'{html_escape(first_part)} <span class="gradient-text">{html_escape(second_part)}</span>'
    else:
        headline_html = f'<span class="gradient-text">{html_escape(headline)}</span>'

    subtitle = config.get("subtitle") or desc or "Build something amazing with a modern, conversion-optimized landing page that your visitors will love."
    cta_primary = config.get("cta_primary", "Get Started Free")
    cta_secondary = config.get("cta_secondary", "Learn More")

    img_html = f'<img src="{hero_img}" alt="{html_escape(name)} preview" loading="lazy">' if hero_img else ""

    return f"""
  <section class="hero" id="home">
    <div class="container">
      <div class="hero-content">
        <h1>{headline_html}</h1>
        <p class="hero-subtitle">{html_escape(subtitle)}</p>
        <div class="hero-buttons">
          <a href="#cta" class="btn btn-primary">{html_escape(cta_primary)}</a>
          <a href="#features" class="btn btn-secondary">{html_escape(cta_secondary)}</a>
        </div>
      </div>
      <div class="hero-image">
        {img_html}
      </div>
    </div>
  </section>"""


def render_logos(config: dict) -> str:
    logos = config.get("logos", ["Acme", "Globex", "Stark", "Wayne", "Umbrella", "Hooli"])
    logo_spans = "\n      ".join(f"<span>{html_escape(l)}</span>" for l in logos)
    return f"""
  <section class="logo-bar">
    <div class="container">
      <p>Trusted by teams at</p>
      <div class="logo-row">
      {logo_spans}
      </div>
    </div>
  </section>"""


def render_features(theme_conf: dict, config: dict) -> str:
    features = config.get("features") or theme_conf.get("features", DEFAULT_FEATURES)
    icons = theme_conf.get("feature_icons", ["✨"] * len(features))

    cards = []
    for i, feat in enumerate(features):
        if isinstance(feat, (list, tuple)) and len(feat) >= 2:
            title, desc = feat[0], feat[1]
        elif isinstance(feat, str):
            title, desc = feat, ""
        else:
            title, desc = "Feature", ""
        icon = icons[i % len(icons)]
        delay_class = f"reveal-delay-{(i % 3) + 1}"
        cards.append(f"""
      <div class="feature-card reveal {delay_class}">
        <div class="feature-icon">{icon}</div>
        <h3>{html_escape(str(title))}</h3>
        <p>{html_escape(str(desc))}</p>
      </div>""")

    return f"""
  <section class="features" id="features">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-tag">Features</span>
        <h2>Everything you need to <span class="gradient-text">succeed</span></h2>
        <p>Powerful features designed to help you achieve your goals faster and more efficiently.</p>
      </div>
      <div class="features-grid">
        {''.join(cards)}
      </div>
    </div>
  </section>"""


def render_how(config: dict, theme_conf: dict) -> str:
    steps = config.get("steps") or [
        ("Sign Up", "Create your account in seconds. No credit card required to get started."),
        ("Set Up", "Configure your workspace and invite your team members with one click."),
        ("Launch", "Start seeing results immediately with our intuitive dashboard and tools."),
    ]
    cards = []
    for i, step in enumerate(steps):
        if isinstance(step, (list, tuple)):
            title, desc = step[0], step[1]
        else:
            title, desc = step, ""
        cards.append(f"""
      <div class="step reveal reveal-delay-{(i % 3) + 1}">
        <div class="step-number">{i + 1}</div>
        <h3>{html_escape(str(title))}</h3>
        <p>{html_escape(str(desc))}</p>
      </div>""")

    return f"""
  <section class="how" id="how-it-works">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-tag">How It Works</span>
        <h2>Get started in <span class="gradient-text">three easy steps</span></h2>
        <p>From sign-up to success in under five minutes.</p>
      </div>
      <div class="steps-grid">
        {''.join(cards)}
      </div>
    </div>
  </section>"""


def render_pricing(config: dict, theme_conf: dict) -> str:
    pricing = config.get("pricing") or theme_conf.get("pricing")
    if not pricing:
        return ""

    cards = []
    for i, plan in enumerate(pricing):
        name, price, period_desc, features_list = plan[0], plan[1], plan[2], plan[3]
        featured_class = " featured" if i == 1 else ""
        badge = '<span class="badge">Most Popular</span>' if i == 1 else ""
        period = period_desc[0] if len(period_desc) > 0 else ""
        desc_text = period_desc[1] if len(period_desc) > 1 else ""

        feat_items = "".join(f"<li>{html_escape(str(f))}</li>" for f in features_list)
        btn_class = "btn-primary" if i == 1 else "btn-secondary"
        btn_text = "Contact Sales" if price == "Custom" else "Get Started"

        cards.append(f"""
        <div class="pricing-card{featured_class} reveal reveal-delay-{(i % 3) + 1}">
          {badge}
          <h3>{html_escape(str(name))}</h3>
          <p class="plan-desc">{html_escape(desc_text)}</p>
          <div class="price">{html_escape(str(price))}<span class="period">{html_escape(period)}</span></div>
          <ul>{feat_items}</ul>
          <button class="btn {btn_class}">{btn_text}</button>
        </div>""")

    return f"""
  <section class="pricing" id="pricing">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-tag">Pricing</span>
        <h2>Simple, <span class="gradient-text">transparent pricing</span></h2>
        <p>Choose the plan that's right for you. Cancel anytime.</p>
      </div>
      <div class="pricing-grid">
        {''.join(cards)}
      </div>
    </div>
  </section>"""


def render_testimonials(config: dict, theme_conf: dict) -> str:
    testimonials = config.get("testimonials") or theme_conf.get("testimonials", [])
    if not testimonials:
        return ""

    cards = []
    for t in testimonials:
        if isinstance(t, (list, tuple)) and len(t) >= 3:
            author, role, text = t[0], t[1], t[2]
        elif isinstance(t, dict):
            author = t.get("name", "")
            role = t.get("role", "")
            text = t.get("text", "")
        else:
            continue
        initials = "".join([w[0] for w in author.split()[:2]]).upper() if author else "?"
        stars = "★" * 5
        cards.append(f"""
        <div class="testimonial-card reveal reveal-delay-{(len(cards) % 3) + 1}">
          <div class="stars">{stars}</div>
          <p class="testimonial-text">{html_escape(str(text))}</p>
          <div class="testimonial-author">
            <div class="author-avatar">{initials}</div>
            <div class="author-info">
              <strong>{html_escape(str(author))}</strong>
              <span>{html_escape(str(role))}</span>
            </div>
          </div>
        </div>""")

    return f"""
  <section class="testimonials" id="testimonials">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-tag">Testimonials</span>
        <h2>Loved by <span class="gradient-text">thousands of customers</span></h2>
        <p>Don't just take our word for it — hear what our community has to say.</p>
      </div>
      <div class="testimonials-grid">
        {''.join(cards)}
      </div>
    </div>
  </section>"""


def render_cta(config: dict, theme_conf: dict) -> str:
    title = config.get("cta_title") or theme_conf.get("cta_title", "Ready to get started?")
    subtitle = config.get("cta_subtitle") or theme_conf.get("cta_subtitle", "Join thousands of happy customers today.")
    btn_text = config.get("cta_button", "Get Started Now")
    return f"""
  <section class="cta-section" id="cta">
    <div class="container">
      <div class="cta-box reveal">
        <h2>{html_escape(title)}</h2>
        <p>{html_escape(subtitle)}</p>
        <a href="#" class="btn btn-primary">{html_escape(btn_text)}</a>
      </div>
    </div>
  </section>"""


def render_faq(config: dict) -> str:
    faqs = config.get("faq") or [
        ("Is there a free trial?", "Yes! We offer a 14-day free trial with full access to all features. No credit card required to sign up."),
        ("Can I cancel anytime?", "Absolutely. You can cancel your subscription at any time directly from your dashboard. No questions asked."),
        ("Do you offer discounts?", "Yes, we offer discounts for annual subscriptions, startups, non-profits, and educational institutions. Contact our sales team for details."),
        ("How secure is my data?", "We use bank-grade encryption (AES-256) and are SOC 2 Type II compliant. Your data is never shared with third parties."),
        ("What payment methods do you accept?", "We accept all major credit cards, PayPal, and bank transfers for annual plans."),
    ]

    items = []
    for q, a in faqs:
        items.append(f"""
      <div class="faq-item">
        <button class="faq-question">
          <span>{html_escape(str(q))}</span>
          <span class="icon">+</span>
        </button>
        <div class="faq-answer">
          <p>{html_escape(str(a))}</p>
        </div>
      </div>""")

    return f"""
  <section class="faq" id="faq">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-tag">FAQ</span>
        <h2>Frequently asked <span class="gradient-text">questions</span></h2>
        <p>Everything you need to know. Can't find an answer? Reach out to our team.</p>
      </div>
      <div class="faq-list reveal">
        {''.join(items)}
      </div>
    </div>
  </section>"""


def render_footer(config: dict, theme_conf: dict) -> str:
    name = config.get("name", "Brand")
    tagline = theme_conf.get("footer_tagline", "Build something amazing.")

    return f"""
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="#" class="nav-logo">
            <span class="logo-dot">{generate_logo_initial(name)}</span>
            {html_escape(name)}
          </a>
          <p>{html_escape(tagline)}</p>
          <div class="social-links">
            <a href="#" aria-label="Twitter">𝕏</a>
            <a href="#" aria-label="LinkedIn">in</a>
            <a href="#" aria-label="GitHub">⌥</a>
            <a href="#" aria-label="Instagram">◎</a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Product</h4>
          <ul>
            <li><a href="#features">Features</a></li>
            <li><a href="#pricing">Pricing</a></li>
            <li><a href="#">Integrations</a></li>
            <li><a href="#">Changelog</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="#">About</a></li>
            <li><a href="#">Blog</a></li>
            <li><a href="#">Careers</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Resources</h4>
          <ul>
            <li><a href="#">Documentation</a></li>
            <li><a href="#">Help Center</a></li>
            <li><a href="#">Privacy Policy</a></li>
            <li><a href="#">Terms of Service</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 {html_escape(name)}. All rights reserved. Built with ♥ using landing-page-builder.</p>
      </div>
    </div>
  </footer>"""


SECTION_RENDERERS = {
    "hero": lambda c, t: render_hero(c, t),
    "logos": lambda c, t: render_logos(c),
    "features": lambda c, t: render_features(t, c),
    "how": lambda c, t: render_how(c, t),
    "pricing": lambda c, t: render_pricing(c, t),
    "testimonials": lambda c, t: render_testimonials(c, t),
    "cta": lambda c, t: render_cta(c, t),
    "faq": lambda c, t: render_faq(c),
    "footer": lambda c, t: render_footer(c, t),
}


def build_html(config: dict) -> str:
    name = config.get("name", "Your Brand")
    theme_name = config.get("theme", "saas")
    theme_conf = THEMES.get(theme_name, THEMES["saas"])
    seed_color = config.get("color", "#6366f1")
    palette = generate_palette(seed_color)
    fonts = theme_conf.get("fonts", ("Poppins", "Inter"))
    head_font, body_font = fonts

    # Merge theme sections with config override
    sections = config.get("sections") or theme_conf.get("sections", ["hero", "features", "cta", "footer"])
    nav_items = config.get("nav") or theme_conf.get("nav", DEFAULT_NAV)

    # SEO
    desc_short = config.get("description", config.get("subtitle", f"Welcome to {name}"))
    desc_short = desc_short[:160]
    og_image = config.get("hero_img") or theme_conf.get("hero_img", "")
    url = config.get("url", "https://example.com")

    # Google Fonts
    fonts_href = (
        f"https://fonts.googleapis.com/css2?"
        f"{head_font.replace(' ', '+')}:wght@600;700;800&"
        f"{body_font.replace(' ', '+')}:wght@400;500;600;700&display=swap"
    )

    # Build sections
    sections_html = []
    for sec in sections:
        renderer = SECTION_RENDERERS.get(sec)
        if renderer:
            result = renderer(config, theme_conf)
            if result:
                sections_html.append(result)

    css = build_css(config, palette, fonts)
    nav_html = render_nav(config, nav_items)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html_escape(name)} — {html_escape(desc_short[:80])}</title>
  <meta name="description" content="{html_escape(desc_short)}">
  <meta name="keywords" content="{html_escape(name.lower())}, {html_escape(theme_name)}, landing page">
  <meta name="author" content="{html_escape(name)}">
  <meta name="robots" content="index, follow">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{html_escape(name)}">
  <meta property="og:description" content="{html_escape(desc_short)}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:url" content="{url}">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html_escape(name)}">
  <meta name="twitter:description" content="{html_escape(desc_short)}">
  <meta name="twitter:image" content="{og_image}">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{fonts_href}" rel="stylesheet">

  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='20' fill='{seed_color}'/><text x='50' y='70' font-size='55' font-weight='bold' text-anchor='middle' fill='white' font-family='sans-serif'>{generate_logo_initial(name)}</text></svg>">

  <style>{css}</style>
</head>
<body>
{nav_html}
{''.join(sections_html)}

<script>
(function() {{
  // Navbar scroll effect
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', function() {{
    if (window.scrollY > 30) navbar.classList.add('scrolled');
    else navbar.classList.remove('scrolled');
  }});

  // Hamburger menu
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('navLinks');
  const overlay = document.getElementById('navOverlay');

  function toggleNav() {{
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('active');
    overlay.classList.toggle('active');
  }}

  hamburger.addEventListener('click', toggleNav);
  overlay.addEventListener('click', toggleNav);

  // Close mobile menu when clicking a link
  navLinks.querySelectorAll('a').forEach(function(link) {{
    link.addEventListener('click', function() {{
      hamburger.classList.remove('active');
      navLinks.classList.remove('active');
      overlay.classList.remove('active');
    }});
  }});

  // Intersection Observer for scroll reveal animations
  var observer = new IntersectionObserver(function(entries) {{
    entries.forEach(function(entry) {{
      if (entry.isIntersecting) {{
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }}
    }});
  }}, {{ threshold: 0.1, rootMargin: '0px 0px -50px 0px' }});

  document.querySelectorAll('.reveal').forEach(function(el) {{
    observer.observe(el);
  }});

  // FAQ accordion
  document.querySelectorAll('.faq-question').forEach(function(question) {{
    question.addEventListener('click', function() {{
      var answer = this.nextElementSibling;
      var isOpen = answer.classList.contains('open');
      // Close all
      document.querySelectorAll('.faq-answer').forEach(function(a) {{ a.classList.remove('open'); }});
      document.querySelectorAll('.faq-question').forEach(function(q) {{ q.classList.remove('active'); }});
      // Toggle this one
      if (!isOpen) {{
        answer.classList.add('open');
        this.classList.add('active');
      }}
    }});
  }});

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {{
    anchor.addEventListener('click', function(e) {{
      var href = this.getAttribute('href');
      if (href === '#') return;
      var target = document.querySelector(href);
      if (target) {{
        e.preventDefault();
        target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      }}
    }});
  }});
}})();
</script>
</body>
</html>"""

    return html


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def interactive_prompt() -> dict:
    print("\n🎨 Landing Page Builder — Interactive Mode\n")
    print("Press Enter to use defaults.\n")

    name = input("Business/Product name [My Brand]: ").strip() or "My Brand"
    desc = input("Short description [A modern platform]: ").strip() or "A modern platform"
    print(f"\nAvailable themes: {', '.join(THEMES.keys())}")
    theme = input("Theme [saas]: ").strip().lower() or "saas"
    if theme not in THEMES:
        print(f"  Unknown theme '{theme}', using 'saas'")
        theme = "saas"
    color = input("Brand color (#hex) [#6366f1]: ").strip() or "#6366f1"
    output = input("Output file [landing.html]: ").strip() or "landing.html"

    return {"name": name, "description": desc, "theme": theme, "color": color, "output": output}


def write_output(html: str, output_path: str) -> str:
    """Write HTML to file and return absolute path."""
    abs_path = os.path.abspath(output_path)
    with open(abs_path, "w", encoding="utf-8") as f:
        f.write(html)
    return abs_path


def cmd_build(args) -> int:
    config = {}

    # Load from JSON config file if provided
    if args.config:
        if not os.path.exists(args.config):
            print(f"Error: config file '{args.config}' not found", file=sys.stderr)
            return 1
        with open(args.config, "r", encoding="utf-8") as f:
            config = json.load(f)

    # Override with CLI args
    if args.name:
        config["name"] = args.name
    if args.desc:
        config["description"] = args.desc
    if args.theme:
        if args.theme not in THEMES:
            print(f"Warning: theme '{args.theme}' not found. Available: {', '.join(THEMES.keys())}", file=sys.stderr)
        else:
            config["theme"] = args.theme
    if args.color:
        config["color"] = args.color
    if args.output:
        config["output"] = args.output

    # If no name or description provided, go interactive
    if not config.get("name") and not config.get("description") and not args.config:
        config.update(interactive_prompt())

    # Defaults
    config.setdefault("name", "My Brand")
    config.setdefault("description", "A modern platform for the modern world.")
    config.setdefault("theme", "saas")
    config.setdefault("color", "#6366f1")
    config.setdefault("output", "landing.html")

    html = build_html(config)
    out_path = write_output(html, config["output"])
    size_kb = os.path.getsize(out_path) / 1024
    print(f"\n✅ Landing page generated successfully!")
    print(f"   📄 File: {out_path}")
    print(f"   📦 Size: {size_kb:.1f} KB")
    print(f"   🎨 Theme: {config['theme']}")
    print(f"   🖌️  Color: {config['color']}")
    print(f"\n   Open in browser: file://{out_path}\n")
    return 0


def cmd_auto(args) -> int:
    """Auto-generate from piped stdin text."""
    if sys.stdin.isatty():
        print("Error: --auto mode requires piped input via stdin", file=sys.stderr)
        print("Example: echo 'Coffee shop called Brew & Co' | python landing_builder.py --auto", file=sys.stderr)
        return 1

    text = sys.stdin.read().strip()
    if not text:
        print("Error: no input received on stdin", file=sys.stderr)
        return 1

    config = auto_parse(text)
    html = build_html(config)

    slug = slugify(config["name"])
    output = args.output or f"{slug}.html"
    out_path = write_output(html, output)
    size_kb = os.path.getsize(out_path) / 1024

    print(f"\n✅ Landing page auto-generated!")
    print(f"   📄 File: {out_path}")
    print(f"   📦 Size: {size_kb:.1f} KB")
    print(f"   🔍 Detected theme: {config['theme']}")
    print(f"   🏷️  Brand name: {config['name']}")
    print(f"   🎨 Color: {config['color']}")
    print(f"\n   Open in browser: file://{out_path}\n")
    return 0


def main():
    parser = argparse.ArgumentParser(
        prog="landing_builder.py",
        description="Generate beautiful, modern landing pages from text descriptions.",
    )
    parser.add_argument("--version", action="version", version=f"landing-page-builder v{VERSION}")

    subparsers = parser.add_subparsers(dest="command")

    # build subcommand
    build_parser = subparsers.add_parser("build", help="Build a landing page")
    build_parser.add_argument("--name", "-n", help="Business/product name")
    build_parser.add_argument("--desc", "-d", help="Short description")
    build_parser.add_argument("--theme", "-t", choices=list(THEMES.keys()), help="Theme")
    build_parser.add_argument("--color", "-c", help="Seed color (hex, e.g. #6366f1)")
    build_parser.add_argument("--config", help="Path to JSON config file")
    build_parser.add_argument("--output", "-o", help="Output HTML filename")

    # auto subcommand (implicit when --auto is passed)
    auto_parser = subparsers.add_parser("auto", help="Auto-generate from piped text")
    auto_parser.add_argument("--output", "-o", help="Output HTML filename")

    # Top-level --auto flag (shortcut for 'auto' subcommand)
    parser.add_argument("--auto", action="store_true", help="Auto-generate from piped stdin text")

    args = parser.parse_args()

    if args.auto or args.command == "auto":
        # Normalize args for cmd_auto
        if not hasattr(args, "output"):
            args.output = None
        return cmd_auto(args)
    elif args.command == "build":
        return cmd_build(args)
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
