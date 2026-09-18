## Description:

Helps agents perform read-only Anrok customer, product, filing, product mapping, tax category, and transaction lookups through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operations teams use this skill to query connected Anrok account data for tax operations and support workflows. The documented action set is read-only and is intended for lookups rather than arbitrary Anrok operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Review the installer path before installation and prefer a verified, versioned, or signed oo CLI installation method.

Risk: Anrok account reads are routed through OOMOL's connector service.

Mitigation: Use the skill only when OOMOL-mediated access is acceptable for the connected Anrok account.

Risk: The trigger wording is broader than the documented read-only action set.

Mitigation: Limit use to the listed get and list actions, and inspect the live action schema before running each connector command.

## Reference(s):

- [ClawHub Anrok Skill](https://clawhub.ai/oomol/skills/oo-anrok)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Anrok Homepage](https://www.anrok.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON; agents should inspect the live action schema before constructing payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
