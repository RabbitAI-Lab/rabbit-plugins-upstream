## Description: <br>
TravelHound compares flights and hotels across Google Flights, Skyscanner, Kayak, Booking.com, Agoda, and Trip.com with book-now-vs-wait timing, OTA coupon stacking, and destination intelligence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiajiaoy](https://clawhub.ai/user/jiajiaoy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to compare live flight and hotel options, estimate trip budgets, check destination context, and decide whether to book now or wait. It is intended for travel search and planning workflows that need platform-by-platform price comparisons and concise booking guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send travel search details to an external flyai/Fliggy-backed CLI and live travel websites. <br>
Mitigation: Use it only when live travel search is intended, avoid sensitive personal details, and confirm before allowing external search or installation steps. <br>
Risk: Flight and hotel prices, availability, coupon codes, visa rules, exchange rates, safety advisories, and news can change quickly. <br>
Mitigation: Treat results as planning guidance and verify final price, terms, eligibility, and official travel requirements before booking. <br>
Risk: The skill may suggest running sibling OpenClaw skills such as CouponClaw and NewsToday. <br>
Mitigation: Confirm those skills are trusted and installed before running suggested commands. <br>


## Reference(s): <br>
- [TravelHound ClawHub listing](https://clawhub.ai/jiajiaoy/skills/travelhound) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [CouponClaw](https://github.com/jiajiaoy/CouponClaw) <br>
- [NewsToday](https://github.com/jiajiaoy/NewsToday) <br>
- [BuyWise](https://github.com/jiajiaoy/BuyWise) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands] <br>
**Output Format:** [Markdown travel reports with browser, web-search, and OpenClaw command instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include live travel-site links, price comparison tables, booking timing advice, coupon lookup commands, and destination context.] <br>

## Skill Version(s): <br>
1.1.5 (source: package.json, _meta.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
