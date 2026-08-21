# Theme Configurations & Customization

This reference documents all available themes, their configurations, and how to
customize every aspect of your landing page.

---

## Available Themes

### 1. `saas` — Software Products & B2B Tools

**Best for:** SaaS products, B2B platforms, developer tools, productivity apps.

```json
{
  "theme": "saas",
  "color": "#6366f1"
}
```

**Sections:** Hero → Logos → Features → How It Works → Pricing → Testimonials → CTA → FAQ → Footer

**Fonts:** Poppins (headings) + Inter (body)

**Default Features:**
- ⚡ Lightning Fast
- 🔒 Bank-Grade Security
- 📊 Deep Analytics
- 🤝 Seamless Collaboration
- 🎯 Smart Automation
- 🔄 100+ Integrations

**Pricing Tiers:** Starter ($0), Pro ($29), Enterprise (Custom)

---

### 2. `startup` — Early-Stage Companies

**Best for:** Startups, pitch pages, product launches, venture-backed companies.

```json
{
  "theme": "startup",
  "color": "#8b5cf6"
}
```

**Sections:** Hero → Logos → Features → How It Works → Testimonials → CTA → Footer

**Fonts:** Poppins + Inter

**Tone:** Bold, energetic, growth-focused. No pricing (early stage — focus on momentum).

---

### 3. `portfolio` — Creative Professionals

**Best for:** Freelancers, designers, photographers, artists, creative agencies.

```json
{
  "theme": "portfolio",
  "color": "#ec4899"
}
```

**Sections:** Hero → Features (services) → How It Works → CTA → Footer

**Fonts:** Poppins + Inter

**Tone:** Personal, showcase-oriented. Features double as services offered.

---

### 4. `restaurant` — Food & Beverage

**Best for:** Restaurants, cafés, bars, bakeries, food trucks.

```json
{
  "theme": "restaurant",
  "color": "#dc2626"
}
```

**Sections:** Hero → Features → Testimonials → CTA → Footer

**Fonts:** Poppins + Inter

**Hero Image:** Warm, inviting restaurant interior.

**Tone:** Appetizing, warm, experiential. CTA focuses on reservations.

---

### 5. `fitness` — Health & Wellness

**Best for:** Gyms, personal trainers, fitness apps, yoga studios, wellness brands.

```json
{
  "theme": "fitness",
  "color": "#f97316"
}
```

**Sections:** Hero → Features → Pricing (memberships) → Testimonials → CTA → Footer

**Fonts:** Poppins + Inter

**Pricing:** Day Pass ($15), Monthly ($49), Annual ($399)

**Tone:** Energetic, motivational, transformation-focused.

---

### 6. `agency` — Service Businesses

**Best for:** Marketing agencies, dev shops, consultancies, design studios.

```json
{
  "theme": "agency",
  "color": "#0ea5e9"
}
```

**Sections:** Hero → Logos → Features (services) → How It Works → Testimonials → CTA → Footer

**Fonts:** Poppins + Inter

**Tone:** Professional, results-driven, ROI-focused.

---

### 7. `ecommerce` — Online Stores

**Best for:** E-commerce sites, product launches, online shops, retail brands.

```json
{
  "theme": "ecommerce",
  "color": "#10b981"
}
```

**Sections:** Hero → Features → Pricing → Testimonials → CTA → Footer

**Fonts:** Poppins + Inter

**Tone:** Trustworthy, benefit-driven, urgency-friendly.

---

## Customization

### Full JSON Config Example

Every field below is optional — the script fills gaps with intelligent defaults:

```json
{
  "name": "TaskFlow",
  "description": "AI-powered task management for modern teams",
  "theme": "saas",
  "color": "#6366f1",
  "tagline": "Ship faster, together",
  "subtitle": "The intelligent project management platform that adapts to how your team actually works.",
  "hero_img": "https://images.unsplash.com/photo-1551434678-e076c223a692?w=1200&q=80",
  "output": "taskflow.html",
  "url": "https://taskflow.app",

  "nav": ["Features", "Pricing", "Testimonials", "FAQ"],

  "cta_primary": "Start Free Trial",
  "cta_secondary": "Watch Demo",
  "cta_title": "Start your free trial today",
  "cta_subtitle": "No credit card required. Set up in 2 minutes.",
  "cta_button": "Get Started Now",

  "features": [
    ["AI Prioritization", "Let AI rank your tasks by impact and urgency automatically."],
    ["Sprint Planning", "Drag-and-drop sprint boards with story points and velocity tracking."],
    ["Time Tracking", "Built-in timers with automatic categorization and reporting."]
  ],

  "steps": [
    ["Create your workspace", "Set up your team and invite members in 30 seconds."],
    ["Add your projects", "Import from Jira, Asana, or start fresh with templates."],
    ["Ship faster", "Watch your velocity increase as AI optimizes your workflow."]
  ],

  "pricing": [
    ["Free", "$0", ["/mo", "For individuals"], ["3 projects", "Basic analytics", "Community support"]],
    ["Pro", "$29", ["/mo", "For growing teams"], ["Unlimited projects", "AI features", "Priority support", "100GB storage"]],
    ["Enterprise", "Custom", ["", "For large teams"], ["Everything in Pro", "SSO/SAML", "Dedicated manager", "99.9% SLA"]]
  ],

  "testimonials": [
    ["Sarah Chen", "VP Engineering, Acme", "Cut our delivery time by 40%."],
    ["Marcus Rivera", "CTO, Boltline", "Saves us 15 hours a week."],
    ["Aisha Patel", "Founder, NimbleLabs", "Best decision we made this year."]
  ],

  "faq": [
    ["Is there a free trial?", "Yes! 14 days, full access, no credit card."],
    ["Can I import from other tools?", "Yes — we support Jira, Asana, Trello, and more."]
  ],

  "logos": ["Acme", "Globex", "Stark", "Wayne"],
  "sections": ["hero", "logos", "features", "pricing", "testimonials", "cta", "footer"]
}
```

---

## Color Palette Generation

The script generates a full palette from a single seed hex color:

| CSS Variable | Derivation | Usage |
|---|---|---|
| `--primary` | Seed color as-is | Buttons, links, accents |
| `--primary-light` | +10% lightness | Hover states |
| `--primary-dark` | -12% lightness | Active states, shadows |
| `--primary-50` | 97% lightness, low sat | Backgrounds, badges |
| `--primary-100` | 93% lightness | Decorative elements |
| `--accent` | Hue +47°, +3% lightness | Secondary gradient color |
| `--gradient-start` | Seed color | Gradient start |
| `--gradient-end` | Hue +29°, -5% lightness | Gradient end |
| `--gradient-accent` | Hue +54° | Text gradient |

### Recommended Seed Colors by Theme

| Theme | Default | Alternatives |
|-------|---------|-------------|
| SaaS | `#6366f1` | `#3b82f6`, `#8b5cf6`, `#06b6d4` |
| Startup | `#8b5cf6` | `#6366f1`, `#ec4899`, `#f59e0b` |
| Portfolio | `#ec4899` | `#8b5cf6`, `#f43f5e`, `#0ea5e9` |
| Restaurant | `#dc2626` | `#ea580c`, `#b91c1c`, `#ca8a04` |
| Fitness | `#f97316` | `#ef4444`, `#eab308`, `#22c55e` |
| Agency | `#0ea5e9` | `#6366f1`, `#14b8a6`, `#2563eb` |
| E-commerce | `#10b981` | `#059669`, `#0d9488`, `#65a30d` |

---

## Section Control

Override which sections appear using the `sections` array:

```json
{
  "sections": ["hero", "features", "pricing", "cta", "footer"]
}
```

**Available sections:** `hero`, `logos`, `features`, `how`, `pricing`, `testimonials`, `cta`, `faq`, `footer`

Sections render in the order listed. Omit any you don't need.

---

## Custom Features Format

Features can be strings or `[title, description]` tuples:

```json
{
  "features": [
    "Simple Feature Name",
    ["Feature with description", "Detailed description text here."],
    ["Another Feature", "Another description."]
  ]
}
```

---

## Custom Pricing Format

Each plan is: `[name, price, [period, description], [feature_list]]`

```json
[
  ["Free", "$0", ["/mo", "Get started"], ["3 projects", "Basic support"]],
  ["Pro", "$29", ["/mo", "For teams"], ["Unlimited projects", "Priority support"]]
]
```

- The **second plan** (index 1) automatically gets the "Most Popular" badge
- Use `"Custom"` as price to show "Contact Sales" button
