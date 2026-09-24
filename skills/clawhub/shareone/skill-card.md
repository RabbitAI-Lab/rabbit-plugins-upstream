## Description:

Host HTML or Markdown pages and share PDF, Word, or PowerPoint documents as ShareOne short links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beep879](https://clawhub.ai/user/beep879)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to publish generated pages and supported documents to ShareOne short links, including password, watermark, comment, download, collaborator, and update workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing can expose selected files or chat content through public short links.

Mitigation: Review content for secrets or personal data before sharing, and use password or watermark options for sensitive material.

Risk: The skill can persist API credentials for ShareOne workflows.

Mitigation: Use trusted environments for credential setup and remove saved API keys when access is no longer needed.

Risk: Generic API helper and custom base URL support can send requests to unintended or untrusted endpoints.

Mitigation: Avoid generic API helper usage or custom base URLs unless the endpoint is known and trusted.

## Reference(s):

- [ClawHub ShareOne skill page](https://clawhub.ai/beep879/skills/shareone)
- [ShareOne website](https://shareone.vip)
- [Skill instructions](artifact/SKILL.md)
- [README](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and script output such as ShareOne URLs or status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce public share links and local downloaded files when requested.]

## Skill Version(s):

1.3.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
