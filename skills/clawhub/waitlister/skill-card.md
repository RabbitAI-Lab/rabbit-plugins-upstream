## Description: <br>
Create and run product-launch waitlists on waitlister.me, including hosted landing pages, email signups, referral programs, and waitlist statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ilpr](https://clawhub.ai/user/ilpr) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, founders, and launch teams use this skill to let an agent create, publish, update, and verify Waitlister-hosted waitlist landing pages. It is suitable when a user wants a coming-soon page, pre-launch email capture, referral-backed signups, or basic waitlist metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can cause account changes by creating waitlists, publishing public landing pages, and sending signup data to Waitlister. <br>
Mitigation: Install only for agents authorized to use the Waitlister account; review any published page before sharing it publicly. <br>
Risk: Verification can submit email addresses and create externally visible waitlist state. <br>
Mitigation: Use an authorized, deliverable test email and confirm status through the Waitlister API before reporting completion. <br>
Risk: Some endpoints are plan-gated or rate-limited, and AI page generation consumes credits. <br>
Mitigation: Respect documented plan limits and rate-limit headers, avoid automatic retries for gated endpoints, and do not auto-retry AI generation after credit errors. <br>


## Reference(s): <br>
- [Waitlister homepage](https://waitlister.me) <br>
- [Waitlister OpenAPI specification](https://waitlister.me/openapi.json) <br>
- [Waitlister agent guide](https://waitlister.me/skill.md) <br>
- [Waitlister documentation overview](https://waitlister.me/docs/overview) <br>
- [Waitlister pricing](https://waitlister.me/pricing) <br>
- [ClawHub skill page](https://clawhub.ai/ilpr/skills/waitlister) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with curl examples, API request patterns, and verification steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires WAITLISTER_API_KEY for authenticated Waitlister API calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
