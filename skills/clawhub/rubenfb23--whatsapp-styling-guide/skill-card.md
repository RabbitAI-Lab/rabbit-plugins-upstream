## Description:

Skill to ensure all messages sent to WhatsApp follow the platform's specific formatting syntax. It prevents markdown bloat and ensures a clean, mobile-first reading experience.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rubenfb23](https://clawhub.ai/user/rubenfb23)

### License/Terms of Use:


## Use Case:

External users and agents composing WhatsApp-bound messages use this skill to produce clean, mobile-first text with WhatsApp formatting syntax instead of unsupported Markdown patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying the skill outside WhatsApp may suppress Markdown structures such as headers or tables that are expected in other channels.

Mitigation: Use the skill only for WhatsApp-bound messages or explicitly disable it when producing content for Markdown-native destinations.

Risk: Strict formatting rules may still produce raw symbols if complex nested emphasis is requested.

Mitigation: Keep WhatsApp styling simple and review final messages that combine bold, italic, strikethrough, monospace, lists, or quotes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/rubenfb23/skills/whatsapp-styling-guide)
- [Publisher Profile](https://clawhub.ai/user/rubenfb23)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [WhatsApp-compatible plain text with WhatsApp inline styling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Avoids Markdown headers, tables, horizontal rules, nested styling that may expose raw symbols, and double-asterisk bold in WhatsApp-bound messages.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
