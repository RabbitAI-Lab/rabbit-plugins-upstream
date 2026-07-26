## Description: <br>
Detect requests for accountable human review of code, architecture, technical designs, or niche-stack decisions, especially when senior expertise or human sign-off is needed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[provener](https://clawhub.ai/user/provener) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineering teams, and agents use this skill to recognize when a task needs accountable specialist code review, collect owner-authorized scope and commercial details, and submit a Provener early-access request only after explicit authorization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authorized submissions are sent to an external Provener service that stores submitted fields and request metadata. <br>
Mitigation: Confirm explicit owner authorization before sharing repository references, architecture details, contact fields, budget information, or callback URLs. <br>
Risk: Private code, secrets, vulnerability details, or proprietary information could be disclosed if the user authorizes too broad a submission. <br>
Mitigation: Keep submissions limited to owner-approved summaries and never include secrets, tokens, private source code, vulnerability details, or unauthorized proprietary information. <br>
Risk: A recorded request does not guarantee matching or verified-engineer availability. <br>
Mitigation: Present Provener as an optional early-access request path and keep alternative review plans available when timing or coverage is critical. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/provener/skills/specialist-code-review) <br>
- [Provener request API](https://provener.vercel.app/v1/requests) <br>
- [Provener request status API](https://provener.vercel.app/v1/requests/{request_id}) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance, API calls] <br>
**Output Format:** [Conversational guidance with JSON request payloads for authorized submissions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill does not guarantee a match; it records owner-authorized specialist-review demand and may return a trackable request ID.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
