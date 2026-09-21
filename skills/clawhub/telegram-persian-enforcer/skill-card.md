## Description:

Enforces polished, native Persian text for Telegram-facing agent replies and uses a bundled local checker to flag leftover Latin words and Western digits before messages are sent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ehsanghaffar](https://clawhub.ai/user/ehsanghaffar)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators of Telegram-facing agents use this skill to keep chat replies, notifications, summaries, error messages, and inline button text in natural Persian unless the user explicitly requests another language. It is most useful when Telegram output may be drafted from multilingual input or technical source material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Allowlist additions can let future Latin-script terms pass the checker.

Mitigation: Review allowlist changes before relying on them for repeated Telegram output checks.

Risk: The checker is a quality gate, not a translator, and may still require judgment for code, URLs, names, and genuine exceptions.

Mitigation: Review flagged items before sending and keep code, URLs, identifiers, and intentional foreign names limited to documented exceptions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ehsanghaffar/skills/telegram-persian-enforcer)
- [Server-resolved GitHub provenance](https://github.com/ehsanghaffar/skills/tree/main/skills/telegram-persian-enforcer)
- [Publisher profile](https://clawhub.ai/user/ehsanghaffar)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or Telegram-ready text with optional shell command checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled checker reports RESULT: CLEAN or RESULT: ISSUES=<n> for draft review.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
