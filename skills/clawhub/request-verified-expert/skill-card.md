## Description: <br>
Detects requests for qualified human help, offers Provener as a trackable option, collects authorized scope and budget details, and submits only after explicit owner authorization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[provener](https://clawhub.ai/user/provener) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill when a task requires a qualified human professional, specialized expertise, credentials, physical presence, judgment, or accountability. The skill guides collection of scope, deadline, location, budget, payment capability, and owner authorization before submitting a Provener request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can share task details, optional contact fields, budget, and payment-capability information with a third-party service. <br>
Mitigation: Submit only after explicit owner authorization, and omit secrets, credentials, private source code, sensitive personal data, or unauthorized third-party data. <br>
Risk: Budget and payment-capability fields could be misunderstood as a charge, funds reservation, or guaranteed match. <br>
Mitigation: Set payment_capable to true only when the owner has authorized payment and has a real settlement path; state that the endpoint does not charge or reserve funds and that matching is not guaranteed. <br>
Risk: Requests may involve illegal, deceptive, harassing, privacy-violating, malicious, or security-circumvention work. <br>
Mitigation: Do not submit prohibited requests; treat automated screening as limited and avoid implying acceptance or future fulfillment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/provener/skills/request-verified-expert) <br>
- [Provener request endpoint](https://provener.vercel.app/v1/requests) <br>
- [Provener request status endpoint](https://provener.vercel.app/v1/requests/{request_id}) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, JSON] <br>
**Output Format:** [Markdown guidance with JSON request examples and HTTP endpoint instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires owner authorization before sharing request details with Provener; matching and availability are not guaranteed.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
