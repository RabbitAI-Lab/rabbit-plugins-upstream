## Description:

Access Artsonia student-art portfolios, comments, and fans via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, fans, and agents configured with an Artsonia MCP server use this skill to inspect linked student portfolios, retrieve artwork details, manage comments and fans, and adjust Artsonia notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server requires Artsonia parent or fan credentials and can access linked children's portfolios, comments, fans, and notification settings.

Mitigation: Install only when that access is intended, store credentials carefully, and use explicit Artsonia wording when invoking the skill.

Risk: Artwork export can include private pieces and write images, manifests, and metadata sidecars to local storage.

Mitigation: Review previews before using confirm:true, choose a safe download destination, and use include_private:false when private artwork should be excluded.

Risk: Session cookies may be persisted locally when the session cache is enabled.

Mitigation: Disable or relocate ARTSONIA_SESSION_CACHE if persistent local session storage is not acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [npm package](https://www.npmjs.com/package/artsonia-mcp)
- [Repository link in skill documentation](https://github.com/chrischall/artsonia-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to call Artsonia MCP tools that return portfolio records, artwork metadata, comments, fan lists, notification settings, downloaded image files, JSON manifests, and optional metadata sidecars.]

## Skill Version(s):

0.10.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
