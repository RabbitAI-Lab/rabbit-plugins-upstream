## Description:

Publish one HTML page through browser-authorized Onimi Pages Remote MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mariohazy](https://clawhub.ai/user/mariohazy)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and external users use this skill to publish a selected HTML artifact to an Onimi Pages one-page project through Remote MCP, then receive the stable URL, version URL, version number, and actual visibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing writes an HTML page to an externally reachable service depending on project visibility.

Mitigation: Confirm the resolved artifact and project before publishing when inferred, preserve existing visibility unless explicitly changed, and report the actual visibility with the returned URLs.

Risk: Unexpected OAuth scopes or pasted credentials could expose user access.

Mitigation: Use browser OAuth through the MCP client, never request tokens in chat, and approve only the expected Onimi Pages scopes.

Risk: Installing from an unverified channel can increase supply-chain risk.

Mitigation: Install from trusted channels, prefer verified or pinned tooling, and verify direct-download archive size and SHA-256 against the stable manifest.

## Reference(s):

- [Install Onimi Pages](references/installation.md)
- [Install Onimi Pages (Chinese)](references/installation.zh-CN.md)
- [Onimi Pages Remote MCP](references/remote-mcp.json)
- [ClawHub listing](https://clawhub.ai/mariohazy/skills/onimi-pages-publish)
- [Onimi Pages dashboard](https://onimi.ai/dashboard)
- [Stable skill manifest](https://downloads.onimi.ai/skills/manifest.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with URLs and inline shell or configuration snippets when setup guidance is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Publishing responses include the stable URL, version URL, version number, and actual visibility.]

## Skill Version(s):

0.2.1 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
