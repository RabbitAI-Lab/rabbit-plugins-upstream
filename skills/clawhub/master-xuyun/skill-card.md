## Description:

Provides Chinese-language Chan Buddhist guidance in a Xuyun-inspired voice, using declared CBETA and FoJin sources for meditation, huatou practice, monastic discipline, and related questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xr843](https://clawhub.ai/user/xr843)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer questions about Xuyun, Chan meditation practice, huatou, Chan retreats, monastic discipline, and Chan/Pure Land topics in Chinese with source citations and scope limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad meditation or monastic-discipline questions may be routed into a specialized Xuyun-inspired religious voice.

Mitigation: Review outputs for fit to the user's intent and clearly state when a question falls outside the skill's Chan/Xuyun source scope.

Risk: Live FoJin lookups may send user query text to fojin.app when local excerpts are insufficient.

Mitigation: Prefer local cited excerpts when sufficient, and avoid live lookup for sensitive user-provided details unless the user accepts that retrieval behavior.

Risk: The skill gives practice-oriented religious guidance that may be mistaken for personal instruction.

Mitigation: Keep answers educational, preserve the disclaimer that formal practice guidance should come from a qualified teacher, and cite declared sources for doctrinal or practice claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xr843/skills/master-xuyun)
- [xr843 publisher profile](https://clawhub.ai/user/xr843)
- [Teaching reference](artifact/references/teaching.md)
- [Voice reference](artifact/references/voice.md)
- [Sources index](artifact/sources/INDEX.md)
- [FoJin: 大佛頂首楞嚴經](https://fojin.app/texts/65)
- [FoJin: 金剛般若波羅蜜經](https://fojin.app/texts/7)
- [FoJin: 六祖大師法寶壇經](https://fojin.app/texts/58)
- [FoJin: 大方廣圓覺修多羅了義經](https://fojin.app/texts/64)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Chinese-language Markdown with inline source citations and relevant links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers should stay within declared Chan/Xuyun scope, avoid sectarian ranking, and use FoJin retrieval only when local cited material is insufficient.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
