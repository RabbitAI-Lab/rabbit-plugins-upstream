## Description:

Verifies email addresses before a campaign and reports which addresses may bounce or need review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, sales development, and revenue operations teams use the skill to check email lists before outreach and identify invalid or risky addresses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verifying a list sends target email addresses to Cargo/waterfall.

Mitigation: Confirm that sharing the addresses with these services is permitted before submitting the list.

Risk: The skill includes optional session telemetry, local tracking, and a GitHub starring action beyond email verification.

Mitigation: Review these steps before use; decline or remove the star flow if GitHub credential use or the local marker is unwanted.

Risk: Batch verification consumes credits in proportion to the number of addresses.

Mitigation: Test 10–20 addresses, estimate the full-list cost, and obtain approval before processing the entire list.

## Reference(s):

- [Verify Email List on ClawHub](https://clawhub.ai/cargo-ai/skills/verify-email-list)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo outreach activation recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/outreach-activation.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown table of email verification statuses with a summary and optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports valid, risky, and invalid addresses and an estimated batch credit cost.]

## Skill Version(s):

1.0.3 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
