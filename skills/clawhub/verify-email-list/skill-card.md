## Description:

Verify a list of email addresses so teams can reduce bounces before sending outreach.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and go-to-market operators use this skill to verify email lists with Cargo before outreach, sample costs, and avoid sending to risky addresses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email addresses are sent to Cargo and the waterfall verification provider for processing.

Mitigation: Install and run the skill only when that data sharing is acceptable for the target list.

Risk: Batch verification consumes credits and cost scales with record count.

Mitigation: Run the documented 10-20 record sample first, report observed cost and hit rate, then get explicit approval before a full run.

Risk: The install metadata uses @cargo-ai/cli@latest, which may not satisfy stricter supply-chain controls.

Mitigation: Pin the Cargo CLI version when a controlled or reproducible installation is required.

Risk: The skill includes a Cargo attribution session command.

Mitigation: Review that command before execution in environments where session metadata disclosure matters.

## Reference(s):

- [Cargo GTM Skills Homepage](https://github.com/getcargohq/gtm-skills)
- [verify-email-list on ClawHub](https://clawhub.ai/cargo-ai/skills/verify-email-list)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces CLI setup and batch execution guidance; the Cargo workflow returns deliverability status per email address.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
