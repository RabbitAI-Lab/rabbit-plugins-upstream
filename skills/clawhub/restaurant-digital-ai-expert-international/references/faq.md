# Frequently Asked Questions (FAQ)

## Getting Started with Digitalization

### Q1: I run a small mom-and-pop shop with just me and my spouse. Do we really need to digitize?
**A**: Yes, but only the "lightest" level of digitalization -- a cloud-based POS (basic tier is often free) + get listed on delivery platforms (basic tier is usually free) + accept digital payments (Apple Pay / Google Pay / card). Only do three things: accept payments, receive delivery orders, view revenue reports. Do not buy extra features you will not use. Keep annual spend under $500.

### Q2: My restaurant has been using paper menus and manual bookkeeping for 3 years. Where should I start?
**A**: Step one is always: switch to a restaurant-specific cloud POS. Selection criteria: 1) supports QR / table ordering 2) integrates with delivery platforms 3) lets you view revenue reports on your phone. Only once this step is solid should you consider loyalty and inventory management.

### Q3: How much does digitalization cost?
**A**: It depends on store count and segment. 1 location, basic: $500-1,200/year. 10-location chain: $8,000-25,000/year. 100-location brand: $80,000-300,000/year. Key principle: "Invest 10%, see results, then invest more."

### Q4: We deployed a system and it turned out to be hard to use. Can we get a refund?
**A**: Most SaaS platforms let you cancel anytime (for annual contracts, negotiate refund terms upfront). This is why you MUST run a PoC (1-2 week free trial) during selection, with frontline staff testing in the real environment. Hard to use = nobody uses it = investment wasted.

---

## Vendor Selection & Implementation

### Q5: How do I choose between Toast, Square, Lightspeed, Clover, and others?
**A**:
- 1-5 locations, small/independent -> Square or Clover (lowest barrier, best value)
- 5-50 locations, growing chain -> Toast (best restaurant-specific ecosystem, robust chain features)
- 50+ locations, boutique/fine dining -> Lightspeed (strong inventory, table management, multi-location)
- Hotels / casinos / global enterprise -> Oracle MICROS (deepest enterprise, widest integrations)
- Delivery-heavy / multi-platform -> ensure your POS integrates with Deliverect or similar order aggregation
- Always test at least 2 vendors with frontline staff before deciding.

### Q6: Should I build my own system or use SaaS?
**A**: If you have fewer than 100 locations, do NOT build your own. The traps of building in-house: 1) costs at least 3-5x SaaS 2) requires maintaining a tech team 3) product iteration speed is slower than dedicated SaaS companies 4) if the tech lead leaves, the system stalls. Unless your operating model is so unique that no solution on the market fits, use SaaS first.

### Q7: How do I ensure business continuity during a system switch?
**A**: Use a "dual-run" strategy: run the old and new systems side by side for 1-2 weeks. The old system remains primary, the new system is secondary, gradually transitioning. Never switch during holidays or peak season. Pick a Monday-to-Wednesday during a slow period to cut over.

### Q8: There is too much data -- where do I even look?
**A**: Start by watching only 3 numbers: daily revenue, labor efficiency (revenue / labor hours), and food cost ratio. Get comfortable reading these 3 before adding more. Do not let data become a "forgettable waterfall of numbers."

---

## AI Applications

### Q9: We only have 5 locations. Can we do AI?
**A**: Yes, but do the ONE thing you need most. For a 5-location operation, the most likely worthwhile AI scenarios are:
1. AI customer service (handling phone / chat inquiries) -- costs a few hundred dollars/month
2. AI personalized recommendations (upsell during online/app ordering) -- many SaaS platforms already include this
3. Basic demand forecasting (predict how much to prep tomorrow) -- some inventory SaaS tools already have this
Do NOT try to train your own models. Use the AI features already integrated into your SaaS vendor.

### Q10: Is AI voice ordering reliable? Will it mess up orders constantly?
**A**: As of 2026, AI voice ordering achieves >95% accuracy in quiet environments, but noisy environments + strong accents + children's voices remain challenging. Deployment essentials: 1) dual microphone noise-cancellation array 2) seamless human handoff (AI cannot handle -> transfers to human within 1 second) 3) start with standard menu items; do not support all custom phrasing on day one. Taco Bell has already processed 2M+ AI voice orders successfully.

### Q11: How much cost can AI realistically save?
**A**: It depends on the scenario. Validated industry data:
- AI voice ordering: 20-40% of one Drive-Thru staff member's workload
- AI demand forecasting: 15-28% food waste reduction
- AI scheduling: 10-22% labor cost reduction
- AI customer service: 50-80% CS labor reduction
But there is one prerequisite -- your data quality must be solid. If your POS data is inaccurate, you are building AI on a foundation of garbage.

---

## Chain & Franchise Operations

### Q12: Our franchisees refuse to use our system. What do we do?
**A**: This is the most common problem. The approach:
1. **Do NOT force it**: Mandated = resistance, no matter how good the system is
2. **Give benefits first**: Deploy the supply chain system first -- once franchisees see "procurement costs dropped 8% with the system," they will willingly adopt more
3. **Champion-led rollout**: Find 5 cooperative franchisees, produce measurable results, data is the best persuasion tool
4. **Aligned incentives**: Lower commission on direct-channel orders vs. third-party platforms, material rebates tied to system adoption
5. **Incremental approach**: Start with modules that "help franchisees make/save money," then add modules that "help HQ manage"

### Q13: How much of franchisee operational data should HQ be able to see?
**A**: "See what you should see; do not see what you should not":
- **Must see**: Revenue trends (YoY / MoM), food safety / inspection compliance rate, core material purchasing compliance rate
- **Can see**: Gross margin, labor efficiency, table turnover rate, member data
- **Better not to see**: Franchisee's own bank statements, detailed profit margins (breeds distrust)
- Core principle: Data transparency exists to "help franchisees run better," not to "monitor franchisees"

---

## Food Safety & Compliance

### Q14: Is a digital food safety system expensive?
**A**: The basic version is not. Core sensors for one location (refrigerator / freezer temperature sensors + one camera) cost approximately $500-1,200 one-time + $200-400/year service fee. What it prevents: a single food safety incident that could incur tens or hundreds of thousands in fines + brand damage. For chains and institutional food service (cafeterias, hospitals, schools), digital food safety is a necessity, not a luxury. Compliance frameworks: FDA Food Code (US), ISO 22000 / HACCP (global).

### Q15: Is our POS data safe in the cloud?
**A**: Choose a certified SaaS vendor (SOC 2 Type II / ISO 27001 certified). Core considerations:
- Data jurisdiction: ensure data is stored in compliance with local regulations (GDPR in EU/UK, CCPA in California, etc.)
- Contract must explicitly state data ownership belongs to you (not the SaaS vendor)
- You must be able to export ALL your data at any time (avoid vendor lock-in)
- Payment data must be PCI-DSS compliant
- Customer / member data must not be exported, sold, or shared without consent

---

## Direct Channels & Loyalty

### Q16: Is building our own ordering channel (app/web) worth it? What is the ROI?
**A**: Very worthwhile, but you must do it well. The math: direct-channel orders save 15-30% in platform commissions. Assume your monthly delivery revenue is $15,000 (platforms take 20-30% commission). If 50% shifts to your own app/web = saving $1,500-2,250/month = $18,000-27,000/year. But the prerequisite is that your app/web experience meets or exceeds the delivery platforms (ordering flow, payments, offers, etc.), otherwise customers will stay on DoorDash/Uber Eats.

### Q17: How do we run effective WhatsApp / social media community marketing for our restaurant?
**A**: Three words: be human and warm. The most effective restaurant community engagement:
1. Post once a day (do NOT spam) -- content = today's special / off-menu items / behind-the-scenes from the owner
2. Community-exclusive perks (20% off Fridays, free tasting of new items) -- creates a sense of "privilege"
3. The owner or store manager posts personally -- AI-generated content is immediately recognizable
4. Engagement rate is NOT the goal -- repeat visit rate is. Do not chase an active chat; chase customers coming back to the restaurant

---

## Workforce & Scheduling

### Q18: Does AI scheduling really beat manual scheduling?
**A**: The more locations you have, the bigger the difference. 1-2 locations: the owner can do it manually. 5+ locations: AI scheduling advantage becomes apparent. 10+ locations: AI scheduling is almost a necessity -- it is impossible for a human to precisely match "each location's hourly traffic tomorrow" against "each employee's availability, skills, and labor law constraints."

---

> **Final word**: Digitalization is not the goal. Making your restaurant more money and giving the owner fewer headaches is the goal. For every dollar spent on digitalization, return to first principles: will this dollar bring back more than a dollar to the restaurant?

---

> **Cross-References**: For more detailed ROI calculations, see `benchmark-data-and-industry-metrics.md`. For vendor selection guidance, see `restaurant-tech-vendor-landscape.md`. For AI-specific Q&A and anti-patterns, see `restaurant-ai-application-framework.md`. For methodology frameworks referenced above (SPIN, 5-Whys, ADKAR, etc.), see `core-methodology-library.md`.
