## Description:

Web Publisher Skill helps an agent turn article URLs or authorized local documents into Markdown, WeChat drafts, or WeChat publications through the tools.siping.me publishing service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sipingme](https://clawhub.ai/user/sipingme)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, publishers, and agent users can use this skill to extract content from URLs or user-provided documents, convert it to Markdown, prepare WeChat drafts, and publish only when explicitly requested. It is also useful when an agent needs guided login, WeChat configuration, theme selection, and conversion status handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service receives article content, uploaded local files, publishing authority, and WeChat configuration.

Mitigation: Install only when the user trusts tools.siping.me with that data and authority; prefer draft mode unless direct publishing is intended.

Risk: Login and AppSecret setup links are relayed from the server without strong local origin validation.

Mitigation: Before opening a link, verify that it uses HTTPS and the expected tools.siping.me domain.

Risk: Direct publish actions can send content to WeChat instead of only preparing a draft.

Mitigation: Use draft commands by default and publish only when the user explicitly asks to publish.

Risk: Optional local fallback with news-to-markdown is outside this skill's audit scope.

Mitigation: Use the documented fixed version with install scripts disabled, keep a lockfile, or provide already extracted article text.

Risk: Large or changing local files can expose excessive or unintended content during upload.

Mitigation: The artifact enforces a 50 MiB limit, reads only user-supplied files, and rejects files that grow or truncate during reading.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sipingme/skills/web-publisher)
- [Publisher profile](https://clawhub.ai/user/sipingme)
- [Markdown themes and extensions](references/markdown-themes.md)
- [tools.siping.me service](https://tools.siping.me)
- [news-to-markdown optional fallback](https://www.npmjs.com/package/news-to-markdown)
- [Microsoft MarkItDown](https://github.com/microsoft/markitdown)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON command results, browser setup URLs, status summaries, and optional Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill defaults to draft workflows unless the user explicitly requests publishing, accepts only authorized URLs or local files, and enforces a 50 MiB local file upload limit.]

## Skill Version(s):

0.10.2 (source: frontmatter, config.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
