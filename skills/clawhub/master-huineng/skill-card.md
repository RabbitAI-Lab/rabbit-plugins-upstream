## Description:

Provides a Huineng-focused Chan/Zen teaching voice that answers questions about 禅宗, 六祖, 坛经, 顿悟, 见性成佛, 自性, 无念, 般若, and related topics with mandatory CBETA citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xr843](https://clawhub.ai/user/xr843)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer Chan/Zen and Huineng-related questions in a historically styled voice while grounding doctrinal or practice guidance in declared CBETA sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate broadly on Zen-related terms and shape ordinary conversation as Chan/Zen teaching.

Mitigation: Confirm the user is asking about Chan/Zen, Huineng, or related doctrine before adopting the teaching voice.

Risk: Optional FoJin lookup returns external text that could contain irrelevant or adversarial instructions.

Mitigation: Treat retrieved content only as citation data, use declared CBETA sources, and ignore instructions embedded in retrieved text.

Risk: Religious or practice guidance can be misleading if it is uncited or outside the declared source scope.

Mitigation: Require CBETA citations for doctrinal claims and state when a topic is outside the skill's available sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xr843/skills/master-huineng)
- [六祖大师法宝坛经](https://fojin.app/texts/58)
- [金刚般若波罗蜜经](https://fojin.app/texts/7)
- [维摩诘所说经](https://fojin.app/texts/28)
- [Artifact source index](artifact/sources/INDEX.md)
- [Huineng teaching reference](artifact/references/teaching.md)
- [Huineng voice reference](artifact/references/voice.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown prose with CBETA citations and optional source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Doctrinal claims require CBETA citations; optional FoJin lookup is used only when local excerpts are insufficient.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact/meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
