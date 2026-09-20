## Description:

Bouncer (usebouncer.com) lets an agent verify emails, domains, batches, toxicity-list jobs, and credit balance through the OOMOL-connected Bouncer connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Bouncer from an agent workflow for email validation, domain checks, batch verification, toxicity-list jobs, and account credit lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes a remote installer for the oo CLI.

Mitigation: Review the installer path before use and prefer a verified package or documented installer with integrity checks.

Risk: Some Bouncer actions create jobs, finish batches early, or delete stored results.

Mitigation: Confirm the exact payload, target, and expected effect with the user before approving write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-bouncer)
- [Bouncer Homepage](https://www.usebouncer.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
