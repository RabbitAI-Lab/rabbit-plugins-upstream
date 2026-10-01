## Description:

Verifies lists of email addresses through Cargo so users can identify risky or invalid addresses before sending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, sales development, and revenue operations teams use this skill to check email lists, identify risky or invalid addresses, and estimate verification credits before a larger run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup records session attribution with Cargo and checks a local Claude plugin file.

Mitigation: Review these steps before running and decide whether the associated metadata sharing and local file access are acceptable.

Risk: Installing the latest Cargo CLI can introduce changes between runs.

Mitigation: Review the package and its version before installation.

Risk: Verifying an entire list consumes credits proportional to its size.

Mitigation: Sample 10–20 records, report observed cost, and obtain approval with a full-run credit estimate.

Risk: The optional GitHub star uses the user's account and is unrelated to email verification.

Mitigation: Only ask after successful delivery and star the repository if the user explicitly approves.

## Reference(s):

- [Verify Email List on ClawHub](https://clawhub.ai/cargo-ai/skills/verify-email-list)
- [Cargo GTM Skills homepage (listed in release metadata)](https://github.com/getcargohq/gtm-skills)
- [Cargo outreach activation recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/outreach-activation.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown with an email-status table and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-address status and reason, summary counts, and estimated verification credits.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
