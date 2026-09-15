## Description:

Operate Confluence through the OOMOL-connected oo CLI to read, create, update, search, and list Confluence content and spaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Confluence through an OOMOL-connected account, including page creation, retrieval, updates, content search, and space listing after checking live action schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confluence content and actions are routed through OOMOL-connected services.

Mitigation: Confirm that the organization permits routing Confluence data through OOMOL and use least-privilege Confluence credentials.

Risk: First-time setup includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Avoid pipe-to-shell installer use unless the installer source is independently trusted and verified.

Risk: Write actions can create or update Confluence pages.

Mitigation: Require explicit review of the exact payload and expected effect before running create or update actions.

## Reference(s):

- [ClawHub Confluence Skill Page](https://clawhub.ai/oomol/skills/oo-confluence)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Confluence Homepage](https://www.atlassian.com/software/confluence)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas and normalized connector responses with execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
