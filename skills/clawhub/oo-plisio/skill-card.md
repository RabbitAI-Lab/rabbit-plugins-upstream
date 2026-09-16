## Description:

Plisio (plisio.net) supports reading, creating, and updating Plisio data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Plisio payment workflows from an agent, including invoice creation, balance checks, and operation lookup or listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to a financial and cryptocurrency service and can create Plisio invoices.

Mitigation: Require explicit user confirmation for invoice-creation payloads before running write actions.

Risk: Setup guidance includes remote installer commands for the oo CLI.

Mitigation: Prefer a verified or manually inspected oo CLI installation path instead of running remote installer commands blindly.

Risk: The release security verdict is suspicious because of the financial-service scope and installer guidance.

Mitigation: Review the skill and security guidance before installation or deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-plisio)
- [Plisio Homepage](https://plisio.net)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector responses, commonly JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
