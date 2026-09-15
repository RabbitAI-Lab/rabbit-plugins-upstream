## Description:

Operates CraftMyPDF through an OOMOL-connected account so agents can read account and template data and generate PDFs via the oo CLI without handling raw API tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect CraftMyPDF schemas, list or retrieve account and template details, and generate PDFs from templates through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer commands that execute downloaded scripts without verification.

Mitigation: Review before installing; prefer an official signed, version-pinned installer or inspect and verify the download before execution.

Risk: State-changing CraftMyPDF actions can generate documents or consume account resources if run with an unintended payload.

Mitigation: Fetch the live action schema, review the exact payload and effect with the user, and require confirmation before running write actions.

## Reference(s):

- [CraftMyPDF homepage](https://craftmypdf.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-craftmypdf)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions can return JSON data from the oo connector, including hosted PDF URLs, account details, template data, and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata, target metadata, and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
