## Description:

Helps agents write, review, and fix HTML markup for semantic structure, forms, accessibility, document metadata, media, embeds, email, performance-sensitive markup, internationalization, parsing issues, and untrusted HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to produce and diagnose HTML for pages, forms, accessible components, metadata, tables, media, embedded content, HTML email, sanitizer guidance, and validation or audit review. It is most useful when the issue belongs to markup semantics, browser parsing, accessibility naming and focus behavior, or safe handling of untrusted HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads and writes persistent local and shared Clawic notes that can influence future sessions.

Mitigation: Install only if this local memory behavior is desired; keep ~/Clawic/data/ writable only by trusted users or tools, review unexpected ## Boxes entries, and check announced writes to project or domain notes.

Risk: Markup handled by the skill may contain API keys, verification tokens, signed URLs, session values, or email service credentials.

Mitigation: Before any memory write, strip secret values and keep only a pointer such as an environment variable, keychain, password manager, vault, or local credential file reference.

## Reference(s):

- [ClawHub HTML skill page](https://clawhub.ai/ivangdavila/skills/html)
- [Clawic HTML skill homepage](https://clawic.com/skills/html)
- [HTML skill source](artifact/SKILL.md)
- [Security guidance](artifact/security.md)
- [Working file templates](artifact/memory-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown responses with HTML snippets, focused reviews, checklists, and local configuration or memory note updates when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce HTML fragments or full documents according to user preferences and may update declared local Clawic note paths when durable HTML facts or decisions are created.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
