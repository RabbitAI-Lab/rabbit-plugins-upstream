## Description:

Formats agent messages for WhatsApp by applying platform-specific text styling rules and avoiding Markdown patterns that render poorly in WhatsApp.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to compose or rewrite messages for WhatsApp so bold, italics, lists, quotes, and code-like text use WhatsApp-compatible syntax instead of generic Markdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The metadata uses broad trigger words and may activate for ordinary messages that mention WhatsApp or styling.

Mitigation: Narrow triggers to requests that explicitly ask for WhatsApp message formatting.

Risk: The artifact includes an execution-related availability claim even though the skill is a text-formatting guide.

Mitigation: Remove execution-related boilerplate and deploy it as a Markdown-only guidance skill.

Risk: Complex Markdown, long messages, or special characters may not convert cleanly to WhatsApp syntax.

Mitigation: Keep formatting simple and review generated messages in WhatsApp before sending.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/whatsapp-styling-guide)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [WhatsApp-compatible plain text with lightweight formatting markers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No file output; messages should avoid Markdown headers, tables, horizontal rules, and double-asterisk bold syntax.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
