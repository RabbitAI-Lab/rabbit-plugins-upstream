## Description:

SumUp (sumup.com). Use this skill for ANY SumUp request: reading, creating, updating, and deleting data through OOMOL's SumUp connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate SumUp checkouts, customers, and saved payment instruments from an OOMOL-connected account. It supports inspecting live action schemas before running JSON payloads for read, write, and checkout deactivation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes pipe-to-shell installer commands for a payment-related integration.

Mitigation: Review the installer path before installing, and prefer a verified package manager, pinned release, or separately downloaded and inspected installer.

Risk: Write and destructive actions can create checkouts, update customer data, or deactivate checkouts.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running state-changing commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-sumup)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [SumUp Homepage](https://www.sumup.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; command responses are JSON when run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
