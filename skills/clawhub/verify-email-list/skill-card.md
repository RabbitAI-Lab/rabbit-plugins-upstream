## Description:

Verifies email addresses through Cargo's waterfall provider to help reduce email bounces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, sales development, and revenue operations teams use this skill to check email lists before campaigns and identify invalid or risky addresses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact lists may include data the user is not authorized to share, and verification uses credits.

Mitigation: Use only authorized lists; run a small sample first, report its cost and results, then get approval for the full run after reviewing the credit estimate.

Risk: Downloaded CLI versions and optional skill packs have implementations outside this release's security assessment.

Mitigation: Review the CLI version and any optional skill pack separately before use.

Risk: GitHub starring changes the user's account state.

Mitigation: Ask once and star only after the user gives explicit approval.

## Reference(s):

- [Cargo GTM Skills project page](https://github.com/getcargohq/gtm-skills)
- [Outreach activation recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/outreach-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Per-address verification statuses in a Markdown table with a concise summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.4 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
