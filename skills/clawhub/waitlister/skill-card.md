## Description: <br>
Create and run product-launch waitlists on waitlister.me: create a waitlist and publish a hosted landing page, collect signups with a referral program, and read stats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ilpr](https://clawhub.ai/user/ilpr) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, founders, and launch teams use this skill to create hosted Waitlister waitlists, publish landing pages, manage signups, and read stats through the Waitlister API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish a publicly reachable Waitlister landing page. <br>
Mitigation: Confirm the page copy, status, and publish intent before calling the publish endpoint. <br>
Risk: Signup operations send email addresses to Waitlister. <br>
Mitigation: Submit only real email addresses with proper authorization or consent. <br>
Risk: The required API key can create and manage Waitlister resources for the connected account. <br>
Mitigation: Use an API key you control, store it securely, and avoid exposing it in prompts, logs, or generated output. <br>
Risk: AI landing page generation consumes Waitlister AI credits and may incur account-specific limits. <br>
Mitigation: Ask for confirmation before generation calls and do not automatically retry credit or rate-limit failures. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ilpr/skills/waitlister) <br>
- [Waitlister OpenAPI Specification](https://waitlister.me/openapi.json) <br>
- [Waitlister Agent Guide](https://waitlister.me/skill.md) <br>
- [Waitlister Docs Overview](https://waitlister.me/docs/overview) <br>
- [Waitlister Pricing](https://waitlister.me/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with REST API examples and curl command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires WAITLISTER_API_KEY for authenticated Waitlister API calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
