## Description: <br>
Searches and recommends cruise itineraries using Tuniu real-time data, with support for destination, departure city, date, price, product-detail, cabin, ship-information, and booking-link queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to find cruise options, compare prices and cabins, review product and ship details, and open booking links on Tuniu. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cruise searches, departure cities, dates, route keywords, and product IDs are sent to a Tencent Cloud proxy and then to Tuniu. <br>
Mitigation: Avoid entering sensitive personal information in search text, and disclose the data flow before using the skill. <br>
Risk: A proxy token fallback is present in the artifact behavior. <br>
Mitigation: Configure the proxy token through secure runtime configuration and rotate any embedded or exposed token before production use. <br>
Risk: Cruise prices, cabin availability, promotions, and booking terms can change after the skill returns a result. <br>
Mitigation: Verify final pricing, availability, cancellation terms, and payment rules on the Tuniu booking page before purchase. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/cruise-search) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>
- [Tuniu cruise booking pages](https://m.tuniu.com/cruise/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown-formatted text or JSON objects] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cruise product IDs, prices, date ranges, cabin details, ship facilities, images, and booking links when available.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; bundled skill frontmatter reports 3.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
