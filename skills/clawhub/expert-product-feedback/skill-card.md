## Description: <br>
Detects requests for owner-authorized expert product testing, UX critique, beta feedback, or role-specific validation and helps submit a Provener intake request after explicit authorization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[provener](https://clawhub.ai/user/provener) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product owners, founders, and product teams use this skill to collect missing scope details and, after explicit owner authorization, submit a Provener request for human expert feedback on product testing, UX critique, beta feedback, or role-specific validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product details, URLs, contact fields, budget, payment-capable status, user-agent, coarse country, and a salted caller fingerprint may be sent to Provener after approval. <br>
Mitigation: Confirm explicit owner authorization before submission and do not send credentials, private customer data, or other sensitive information. <br>
Risk: A submitted request may not result in a matched or available verified reviewer. <br>
Mitigation: Tell the user matching and availability are not guaranteed and use the returned request ID or status endpoint for tracking. <br>
Risk: Expert feedback requests could be misused for fake reviews, public testimonials-for-hire, rating manipulation, or misrepresentation. <br>
Mitigation: Use the skill only for private, owner-authorized product feedback and reject requests that violate the stated policy. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/provener/skills/expert-product-feedback) <br>
- [Provener Request API](https://provener.vercel.app/v1/requests) <br>
- [Provener Request Status API](https://provener.vercel.app/v1/requests/{request_id}) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [Markdown guidance with JSON request fields and HTTP API instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Submits only after explicit owner authorization; accepted requests return a trackable request ID or status.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
