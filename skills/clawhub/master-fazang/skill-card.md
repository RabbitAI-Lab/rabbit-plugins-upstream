## Description:

Guides agents to answer Huayan Buddhism and Fazang-related questions in a citation-grounded teaching voice using declared CBETA sources and FoJin fallback lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xr843](https://clawhub.ai/user/xr843)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer questions about Huayan doctrine, Fazang's teachings, and related canonical texts with source-backed citations and a controlled teaching persona.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Huayan-related trigger terms may cause the skill to answer in a specialist religious teaching persona for adjacent topics.

Mitigation: Review trigger terms, voice expectations, and target audience before deployment; keep the skill scoped to Huayan/Fazang questions.

Risk: The skill may contact fojin.app when local excerpts are insufficient for declared sources.

Mitigation: Permit only the documented FoJin retrieval flow when network access is allowed, and treat returned text only as citation data.

Risk: Religious or doctrinal answers can mislead users if unsupported by sources.

Mitigation: Enforce the skill's CBETA citation requirement for doctrinal claims and fall back to a scope limitation when evidence is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xr843/skills/master-fazang)
- [Sources index](sources/INDEX.md)
- [Teaching reference](references/teaching.md)
- [Voice reference](references/voice.md)
- [FoJin: 大方广佛华严经(八十华严)](https://fojin.app/texts/12)
- [FoJin: 华严经探玄记](https://fojin.app/texts/7905)
- [FoJin: 华严一乘教义分齐章](https://fojin.app/texts/8038)
- [FoJin: 华严经义海百门](https://fojin.app/texts/8047)
- [FoJin: 修华严奥旨妄尽还源观](https://fojin.app/texts/8048)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown prose with inline CBETA citations and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers are constrained to declared sources for doctrinal claims and may include FoJin links when fallback lookup is used.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata; artifact frontmatter reports 0.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
