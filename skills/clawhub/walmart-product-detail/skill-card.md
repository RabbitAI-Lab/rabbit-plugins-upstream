## Description: <br>
Extracts structured data from Walmart product detail pages, including product identity, pricing, availability, seller details, images, specifications, variants, fulfillment options, return policy, and review summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and catalog operators use this skill to collect structured product detail data from user-provided Walmart product URLs for catalog enrichment, competitive research, price and availability monitoring, or batch product analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags guidance for increasing scraping throughput with multiple stealth browser sessions. <br>
Mitigation: Use conservative, user-directed collection, respect Walmart's terms and rate limits, and avoid the stealth multi-session throughput guidance. <br>
Risk: A disclosed memory file may persist troubleshooting notes between runs. <br>
Mitigation: Check the memory file path before use and remove or avoid retained notes when persistence is not desired. <br>
Risk: Extracted product fields can be incomplete or location-dependent when Walmart does not expose values in the current browser session. <br>
Mitigation: Treat null or session-dependent fields as expected output conditions and verify critical product data against the live page before downstream use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/walmart-product-detail) <br>
- [Publisher profile](https://clawhub.ai/user/browseract-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [JSON product records with concise progress or error messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads product data visible in the user's browser session; some fields may be null when Walmart does not expose them on the page.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
