## Description:

Adobe Commerce connector skill for searching and reading catalog data through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Adobe Commerce product and category data through an OOMOL-connected account. It supports schema-first execution for read-only product and category lookup or listing tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path may run remote installer scripts for the oo CLI.

Mitigation: Install the oo CLI only from a verified, versioned, checksum-checked source, and avoid letting an agent execute curl or PowerShell installer pipelines automatically.

Risk: Future connector actions could change Adobe Commerce state if write or destructive operations are added.

Mitigation: Keep routine use to the listed read-only get and list actions, and require explicit user confirmation for any documented write or destructive action.

## Reference(s):

- [Adobe Commerce homepage](https://business.adobe.com/products/magento/magento-commerce.html)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-adobe-commerce)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
