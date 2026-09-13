## Description:

Publish one generated HTML page through the Onimi Pages Remote MCP connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mariohazy](https://clawhub.ai/user/mariohazy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to publish a selected HTML artifact to an existing or explicitly created Onimi Pages project through browser-authorized Remote MCP, while preserving visibility unless the user asks to change it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing from an untrusted, unpinned, or unavailable channel could install an unexpected release.

Mitigation: Use a trusted channel, prefer verified direct downloads with SHA-256 checking or pinned marketplace releases, and check the verified channel manifest before registry installs.

Risk: Publishing is an external write that can expose the selected HTML page under the selected project's visibility.

Mitigation: Review the resolved HTML file, target project, and requested visibility before publishing, and preserve existing visibility unless the user explicitly asks to change it.

Risk: Browser OAuth grants account access to the remote publishing service.

Mitigation: Let the user complete consent in the browser, do not request tokens in chat, and avoid granting scopes the user does not understand.

Risk: The optional direct-download manager can update installed skill files.

Mitigation: Run update only for receipt-backed direct-download installations after verifying the displayed version and approving the exact update.

## Reference(s):

- [Installation Guide](references/installation.md)
- [Chinese Installation Guide](references/installation.zh-CN.md)
- [Remote MCP Definition](references/remote-mcp.json)
- [ClawHub Skill Listing](https://clawhub.ai/mariohazy/skills/onimi-pages-publish)
- [Verified Channel Manifest](https://downloads.onimi.ai/skills/manifest.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Publishing results normally include the stable URL, version URL, version number, actual visibility, and any uncertainty about publish state.]

## Skill Version(s):

0.2.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
