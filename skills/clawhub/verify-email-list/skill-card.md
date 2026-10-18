## Description:

Verifies email lists with Cargo so marketing and sales teams can identify addresses likely to bounce before sending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, sales development, and revenue operations teams use this skill to check email deliverability and remove risky or invalid addresses before a campaign.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup can send session attribution to Cargo and inspect a local agent plugin configuration file.

Mitigation: Skip the optional attribution step and local configuration check if they are not needed.

Risk: The skill proposes an unrelated GitHub starring action using the user's account.

Mitigation: Do not run the starring command unless the user explicitly opts in.

Risk: Verifying a full email list consumes credits proportional to the number of addresses.

Mitigation: Test a small sample, confirm the estimated credit use, and obtain approval before running the full batch.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/verify-email-list)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo outreach activation recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/outreach-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with per-address verification results and a summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports deliverability status and reasons; recommends which addresses to exclude.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
