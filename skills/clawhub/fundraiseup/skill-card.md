## Description: <br>
Interact with FundraiseUp REST API to manage donations, recurring plans, supporters, campaigns, and donor portal access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aamish99](https://clawhub.ai/user/aamish99) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and nonprofit operations teams use this skill to draft Fundraise Up API requests, review donation and supporter workflows, and integrate fundraising data with CRM or analytics systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide live donation, payment, and donor portal actions through Fundraise Up API requests. <br>
Mitigation: Use test-mode keys by default, grant only the required API permissions, and require explicit human confirmation before POST or PATCH requests. <br>
Risk: Prompts, logs, or shared outputs may expose donor PII, payment identifiers, or donor portal access links. <br>
Mitigation: Avoid including sensitive donor data, payment identifiers, or donor portal links in prompts, logs, or shared outputs unless necessary. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aamish99/skills/fundraiseup) <br>
- [Fundraise Up REST API documentation](https://fundraiseup.com/docs/rest-api/) <br>
- [Fundraise Up API resources](https://fundraiseup.com/docs/rest-api-resources/) <br>
- [Fundraise Up donor portal integration](https://fundraiseup.com/docs/seamless-donor-portal/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON, Python, JavaScript, and cURL examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live API request examples that require a Fundraise Up API key.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
