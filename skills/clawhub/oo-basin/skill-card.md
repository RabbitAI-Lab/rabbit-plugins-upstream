## Description:

Basin lets an agent read, create, update, and delete Basin projects, forms, webhooks, and submissions through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Basin projects, forms, webhooks, and submissions from an agent workflow through the OOMOL-connected oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer scripts that are not independently verified in the evidence.

Mitigation: Prefer an official package manager or a downloaded installer with a verified version, signature, or checksum before installing the oo CLI.

Risk: Write and destructive Basin actions can modify or delete projects, forms, webhooks, and submissions.

Mitigation: Confirm the exact target, action, and payload before running write operations, and require explicit approval before destructive actions.

Risk: Connector action payloads may drift from the current Basin connector contract.

Mitigation: Inspect the live action schema with the oo CLI before constructing each action payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-basin)
- [Basin Homepage](https://usebasin.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, API calls, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing Basin action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
