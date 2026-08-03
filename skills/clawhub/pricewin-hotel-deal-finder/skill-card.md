## Description: <br>
Finds hotel deals by comparing live prices across Booking.com, Agoda, Google Hotels, and OpenTravel, then returns ranked best-value, cheapest, and quality picks with direct booking links normalized to USD. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cotghw](https://clawhub.ai/user/cotghw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to compare hotel prices for a city, date range, and guest count, then present ranked options with per-night prices and booking links. It is intended for normal hotel deal searches where live provider results may vary by availability and provider response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads Patchright and Chromium and launches a local browser daemon to collect hotel listings. <br>
Mitigation: Install it only in an environment where local browser automation is acceptable, use the documented search command, and close the daemon if a run is interrupted. <br>
Risk: Hotel search details such as city, dates, and guest count are sent to travel providers and a currency-rate service. <br>
Mitigation: Use it only for intended hotel searches and avoid entering information that should not be shared with those providers. <br>
Risk: Lower-level browsing commands can navigate unrelated pages if used outside the documented workflow. <br>
Mitigation: Use the one-shot search.js path for normal operation and avoid ad hoc browsing commands for unrelated websites. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cotghw/skills/pricewin-hotel-deal-finder) <br>
- [Publisher profile](https://clawhub.ai/user/cotghw) <br>
- [PriceWin skills hub](https://github.com/Price-Win/pricewin-skills-hub) <br>
- [Security and Data Handling](artifact/SECURITY.md) <br>
- [OpenTravel API host](https://api.opentravel.one) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown-formatted hotel comparison with ranked sections, per-night prices, and inline booking links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prices are normalized to USD; provider coverage may be partial when a source is blocked or has no inventory.] <br>

## Skill Version(s): <br>
1.1.3 (source: SKILL.md frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
