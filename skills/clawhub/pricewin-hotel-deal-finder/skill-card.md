## Description: <br>
Find the cheapest hotel deal by comparing live prices across Booking.com, Agoda, Google Hotels, and OpenTravel for any city worldwide and any travel dates; one command returns ranked best-value, cheapest, and quality picks with direct booking links, all normalized to USD. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cotghw](https://clawhub.ai/user/cotghw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to compare live hotel prices for a city, date range, and guest count across multiple travel providers, then present ranked hotel deal options with booking links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads Patchright and Chromium and runs a local browser-control daemon. <br>
Mitigation: Install only in an environment where those dependencies and local browser automation are acceptable, and clear the skill cache or close the daemon after interrupted searches. <br>
Risk: Hotel search details are sent to travel providers and the OpenTravel API as part of normal operation. <br>
Mitigation: Avoid entering sensitive personal details; provide only the city, travel dates, guest count, and locale needed for price comparison. <br>
Risk: Results come from live public travel sites and may be partial when a provider is blocked or has no inventory. <br>
Mitigation: Present the generated output as current comparison data and rely on the skill's footer to disclose which providers returned results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cotghw/skills/pricewin-hotel-deal-finder) <br>
- [Project homepage](https://github.com/Price-Win/pricewin-skills-hub) <br>
- [SECURITY.md](artifact/SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown tier cards with inline booking links and command-line usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Hotel results are normalized to USD and may include partial provider coverage when a source is blocked or empty.] <br>

## Skill Version(s): <br>
1.1.2 (source: SKILL.md frontmatter, package.json, and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
