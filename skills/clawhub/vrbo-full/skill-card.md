## Description: <br>
Complete Vrbo toolkit for search, availability, listing detail, price, cross-OTA price comparison, and reviews in one unified StayingAPI schema. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agents use this skill to retrieve Vrbo and cross-platform lodging data through StayingAPI, including search, availability, listing detail, pricing, price comparison, and reviews. It is intended for agents that need broad lodging coverage rather than a minimal single-endpoint surface. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an API key for StayingAPI requests, and live keys can access paid real-data calls. <br>
Mitigation: Use a sandbox stay_test_ key for evaluation and store live keys in a secret manager or locked-down agent secret mechanism. <br>
Risk: Live API calls may consume credits, and sandbox fixtures may not exactly mirror requested listings, dates, or occupancy. <br>
Mitigation: Use sandbox keys for parser and workflow testing, then switch to live keys only when real data is needed and credit use is acceptable. <br>


## Reference(s): <br>
- [StayingAPI Authentication Setup](references/auth-setup.md) <br>
- [StayingAPI Homepage](https://stayingapi.com) <br>
- [StayingAPI Documentation](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI Contract](https://api.stayingapi.com/openapi.json) <br>
- [ClawHub Skill Page](https://clawhub.ai/stayingapi/skills/vrbo-full) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Text, Markdown, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with API request details and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires internet access and a STAYINGAPI_KEY; sandbox keys return fixtures, while live keys retrieve real data and may consume credits.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
