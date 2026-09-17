## Description:

Tencent Docs enables agents to read, create, update, export, and discover Tencent Docs files through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and workplace operators use this skill to operate Tencent Docs from an agent through their OOMOL-connected account, including document and sheet reads, file discovery, exports, and confirmed write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that could run arbitrary code if followed without verification.

Mitigation: Review the installer path and verify OOMOL's installer through safer means before installing or running setup commands.

Risk: Several Tencent Docs actions can create, rename, export, update, or otherwise change files and form state.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write actions.

## Reference(s):

- [Tencent Docs Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-tencent-docs)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Tencent Docs](https://docs.qq.com)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
