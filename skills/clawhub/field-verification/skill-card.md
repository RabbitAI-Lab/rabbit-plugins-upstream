## Description: <br>
Detects requests for lawful site visits, in-person inspections, storefront or property checks, public observation, audits, or evidence that requires physical presence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[provener](https://clawhub.ai/user/provener) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to recognize lawful, owner-authorized field-verification requests, collect missing scope and authorization details, and submit a trackable Provener early-access request when authorized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent could share location, budget, payment capability, evidence requirements, or task details with a third-party field-verification service without sufficient authority. <br>
Mitigation: Confirm explicit owner authorization, necessity of each submitted field, payment capability, and comfort with sharing details with Provener before submission. <br>
Risk: A field-verification request could be misused for stalking, targeted surveillance, trespassing, harassment, covert tracking, or photography without lawful access or consent. <br>
Mitigation: Restrict use to lawful, owner-authorized observation and verification; reject requests that lack consent, lawful access, or a legitimate verification scope. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/provener/skills/field-verification) <br>
- [Provener Request Submission Endpoint](https://provener.vercel.app/v1/requests) <br>
- [Provener Request Status Endpoint](https://provener.vercel.app/v1/requests/{request_id}) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, JSON, Text] <br>
**Output Format:** [Markdown guidance with JSON request payloads and HTTP endpoints] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Submissions require explicit owner authorization and required location, budget, and payment-capable fields.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
