## Description: <br>
Compares flight and train ticket prices across multiple platforms, including real-time 12306 train availability, optional Firecrawl-rendered Ctrip flight data, direct booking links, WeChat mini program quick links, and discount condition details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amurtiger01](https://clawhub.ai/user/amurtiger01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to compare domestic China and international flight options, train availability, fares, booking links, and discount restrictions for a requested route and date. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live travel searches may share departure, destination, travel date, and possibly locale with booking, scraping, or API providers. <br>
Mitigation: Use live lookup only for travel plans that are appropriate to share with those providers, and leave optional API keys unset when reduced third-party exposure is preferred. <br>
Risk: Real-time fares, availability, and discount rules can change or differ by provider at booking time. <br>
Mitigation: Confirm final price, seat availability, refund rules, baggage limits, and discount conditions on the booking platform or official operator site before purchase. <br>
Risk: Optional provider credentials enable richer flight data but increase exposure to external services. <br>
Mitigation: Configure only the provider credentials needed for the task, keep them in environment variables, and avoid pasting secrets into prompts or shared logs. <br>


## Reference(s): <br>
- [Ticket Price Compare Skill Page](https://clawhub.ai/amurtiger01/skills/ticket-price-compare) <br>
- [Platform Discount Conditions Guide](references/platforms_guide.md) <br>
- [Firecrawl](https://firecrawl.dev) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown-style route summaries, price tables, discount notes, platform links, and command output from the ticket search script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live or provider-derived availability and fare data, direct booking links, airline site links, and fallback guidance when live flight prices are unavailable.] <br>

## Skill Version(s): <br>
1.2.7 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
