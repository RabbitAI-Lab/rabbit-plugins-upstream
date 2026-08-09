## Description:

Adds selectable Chinese flattery and persona overlays for agent conversations, including a Liu Bowen divination-style companion mode intended for entertainment and emotional support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[william22820785-cmyk](https://clawhub.ai/user/william22820785-cmyk)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to add persistent Chinese persona styles, praise-heavy tone, and entertainment-focused divination responses to supported agent environments. It is best suited for casual roleplay, encouragement, and companion-style interactions rather than objective professional advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent persona behavior may be added to OpenClaw SOUL.md or generated IDE/agent configuration.

Mitigation: Install only when that behavior is intended, and review SOUL.md, Cursor rules, and generated configuration before applying or sharing them.

Risk: The Claude Code adapter includes an unsafe permission-bypass launch flag.

Mitigation: Remove the permission-bypass flag before using the Claude Code adapter.

Risk: Corpus-upgrader and daily-upgrade scripts can use credentials, call network APIs, and modify local source files.

Mitigation: Do not run those scripts until credential use, network effects, and file modifications have been reviewed.

Risk: Divination-style responses can be mistaken for real predictions.

Mitigation: Treat Liu Bowen outputs as entertainment and emotional support, not as medical, legal, financial, or life-decision advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/william22820785-cmyk/skills/xinling-bushou-v2)
- [Publisher profile](https://clawhub.ai/user/william22820785-cmyk)
- [Skill README](artifact/SKILL.md)
- [FAQ](artifact/FAQ.md)
- [Antipatterns and usage guidance](artifact/ANTIPATTERNS.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, generated configuration fragments, and JSON-backed persona data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist selected persona behavior into local agent or IDE configuration when installation or injection scripts are run.]

## Skill Version(s):

3.5.1 (source: ClawHub release metadata; artifact frontmatter reports 3.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
