## Description: <br>
This skill helps agents retrieve structured Amazon product details from a provided ASIN using BrowserAct's Amazon ASIN Lookup API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phheng](https://clawhub.ai/user/phheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, catalog operators, and e-commerce teams use this skill to look up product titles, pricing, ratings, availability, descriptions, images, and specifications from an Amazon ASIN. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends ASIN lookup requests through BrowserAct. <br>
Mitigation: Use it only when sending ASIN lookup requests through BrowserAct is acceptable for the use case, and review returned product data before relying on it. <br>
Risk: The skill can ask users to provide a BrowserAct API key through chat when BROWSERACT_API_KEY is missing. <br>
Mitigation: Configure BROWSERACT_API_KEY through environment or secret storage; do not paste API keys into chat, prompts, logs, or shared transcripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/phheng/skills/amazon-asin-lookup-api-skill) <br>
- [BrowserAct API key setup](https://www.browseract.com/reception/integrations) <br>
- [BrowserAct workflow API endpoint](https://api.browseract.com/v2/workflow) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Terminal logs followed by structured product data as text or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, an ASIN argument, and BROWSERACT_API_KEY configured through environment or secret storage.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
