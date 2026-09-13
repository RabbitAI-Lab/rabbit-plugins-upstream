## Description:

Onboard a merchant into the Auto Google Review Reply product: register/login, connect a Google Business Profile, benefit from a 5-day free trial (membership check, no forced payment), and configure AI auto-reply.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cheaplightstore](https://clawhub.ai/user/cheaplightstore)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants use this skill to set up Auto Google Review Reply, connect an existing Google Business Profile, verify free-trial or membership status, and configure AI-generated public review replies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow handles a long-lived product session and may expose token-bearing URLs or pasted callback values if used carelessly.

Mitigation: Use the SSO handoff path when possible, keep the Authorization value only in the designated environment variable, and avoid sharing token-bearing URLs or callback values.

Risk: The workflow can connect or disconnect a Google Business Profile and configure automated public replies.

Mitigation: Confirm the exact business profile, selected location, trigger threshold, reply language, shop introduction, signature, and keywords with the merchant before saving changes.

Risk: The workflow can create Stripe checkout sessions after a trial or membership has expired.

Mitigation: Check membership status before any payment step and require merchant confirmation of the paid plan before opening checkout.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cheaplightstore/skills/google-autoreply)
- [ClawHub publisher profile](https://clawhub.ai/user/cheaplightstore)

## Skill Output:

**Output Type(s):** [text, guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown text with REST API request guidance and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides authenticated onboarding, Google Business connection, membership checks, and auto-reply configuration.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
