## Description: <br>
Use Go2.gg API for URL shortening, link analytics, QR code generation, webhooks, and link-in-bio pages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rakesh1002](https://clawhub.ai/user/rakesh1002) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, marketers, and operators use this skill to have an agent prepare Go2.gg API calls and examples for short links, click analytics, QR codes, webhooks, branded URLs, and link-in-bio galleries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated Go2.gg account actions require an API key and can create, update, delete, publish, or inspect resources. <br>
Mitigation: Review proposed delete, publish, analytics, and webhook requests before execution, and use the GO2GG_API_KEY only for intended account actions. <br>
Risk: Webhook configuration can send event data to user-provided endpoints. <br>
Mitigation: Use trusted webhook endpoints, verify webhook signatures, and rotate the API key if the skill is no longer used. <br>


## Reference(s): <br>
- [Go2.gg API documentation](https://go2.gg/docs/api/links) <br>
- [Go2.gg API keys dashboard](https://go2.gg/dashboard/api-keys) <br>
- [Go2.gg ClawHub skill page](https://clawhub.ai/rakesh1002/skills/go2gg) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with cURL commands, JSON payloads, and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose authenticated Go2.gg account actions and unauthenticated QR generation requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
