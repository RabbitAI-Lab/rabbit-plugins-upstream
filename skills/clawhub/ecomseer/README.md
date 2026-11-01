# EcomSeer — Overseas Customer Acquisition Platform

[中文文档](README_CN.md)

EcomSeer is an AI-powered overseas customer acquisition platform by Beijing Miaozhisheng Technology, built for foreign trade and manufacturing companies. It streamlines the entire international customer development workflow—market intelligence, brand building, overseas promotion, inquiry qualification, and CRM—leveraging commercial databases, multilingual content, and smart outreach to help Chinese manufacturers connect with qualified global buyers.

## Platform Capabilities

EcomSeer supports the international customer development workflow for foreign trade and manufacturing companies. This skill provides the platform's market intelligence and overseas promotion data capabilities through natural-language requests.

- **Market Intelligence** — Search TikTok Shop products, rankings, shops, influencers, videos, and advertising data across major markets
- **Product and Category Research** — Analyze product demand, sales trends, pricing, reviews, and category opportunities
- **Influencer and Promotion Intelligence** — Evaluate creator reach, engagement, sales performance, video performance, and promotional partnerships
- **Shop and Competitor Research** — Explore shop assortments, seller performance, and market positioning signals
- **Ad and Creative Insights** — Research e-commerce advertisers, creative trends, top keywords, and promotion strategies
- **Deep Research** — Generate structured AI research reports for complex market, competitor, and overseas promotion questions

## Install

```bash
npx clawhub install ecomseer
```

## Setup

1. Go to [www.ecomseer.com](https://www.ecomseer.com) to register and get your API Key
2. Configure:

```bash
openclaw config set skills.entries.ecomseer.apiKey "YOUR_ECOMSEER_API_KEY"
```


## Usage Examples

After setup, just tell your AI assistant:

| Category | Example prompts |
|----------|----------------|
| Market Intelligence | "Search Bluetooth earbuds on TikTok Shop", "Find trending skincare products" |
| Product and Category Research | "US TikTok Shop sales ranking", "Analyze the beauty market opportunity" |
| Product Detail | "Show me this product's sales trend", "Which influencers promote this?" |
| Influencer | "Find beauty influencers with 100K+ followers", "Analyze this creator's performance" |
| Promotion Intelligence | "Hot TikTok Shop videos this week", "Show video performance data" |
| Competitor Research | "Search TikTok shops selling electronics", "Analyze this shop's product mix" |
| Overseas Promotion | "Search e-commerce ad creatives", "What are the trending ad keywords?" |
| Deep Research | "Analyze US beauty category trends", "Compare top 5 shops in Southeast Asia" |

Supports both **English** and **Chinese** — the assistant responds in your language.

## Multi-Market Support

The market intelligence module covers all supported TikTok Shop markets:

| Region Code | Market |
|-------------|--------|
| US | United States |
| GB | United Kingdom |
| ID | Indonesia |
| TH | Thailand |
| VN | Vietnam |
| MY | Malaysia |
| PH | Philippines |
| SG | Singapore |

Default market is US. Switch by saying "show me Indonesia data" or "切换到东南亚".

## Deep Research — AI-Powered Intelligence Reports

For complex analytical queries, EcomSeer automatically activates its **Deep Research Framework** — a server-side AI research engine that goes far beyond simple API lookups.

**What triggers Deep Research:**

- Category trend analysis: *"Analyze US beauty category trending products"*
- Multi-entity comparisons: *"Compare these two shops' strategies"*
- Market intelligence: *"Southeast Asia e-commerce opportunity analysis"*
- Influencer strategy: *"Analyze this creator's monetization approach"*
- Any question requiring 2+ API calls or cross-entity reasoning

**What you get:**

- Structured HTML report with charts and data tables
- Executive summary with key findings
- Cross-dimensional insights (products × influencers × videos × ads)
- Actionable e-commerce recommendations

The framework typically completes in 1–5 minutes depending on query complexity. Reports are hosted and shareable via link.

## Links

- Website: [www.ecomseer.com](https://www.ecomseer.com)

---

Built by [EcomSeer](https://www.ecomseer.com)
