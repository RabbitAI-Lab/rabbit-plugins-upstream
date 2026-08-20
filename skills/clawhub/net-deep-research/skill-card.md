## Description:

Performs deep multi-source internet research for complex truth-finding tasks that need online verification, cross-source fact checking, authenticity checks, or conflict-aware web research beyond routine lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[h4444433333](https://clawhub.ai/user/h4444433333)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when a question needs deep web research, cross-source verification, source authenticity checks, or conflict-aware synthesis instead of a routine lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research-source metadata, candidate URLs, query classification, and structured evidence records may be sent to shoggoth.vip during deep research.

Mitigation: Avoid sensitive internal URLs or private investigations unless external backend use is intended; use the documented fallback path when backend calls are unavailable or inappropriate.

Risk: Explicit high-sensitivity diagnostics can include raw query text or full answer text.

Mitigation: Use high-sensitivity diagnostic paths only when the user explicitly requests them and the additional data sharing is acceptable.

Risk: Cross-source research can still produce incomplete or misleading conclusions when sources are stale, conflicting, or insufficient.

Mitigation: Apply the documented multi-round, multi-angle, conflict-aware workflow and state unresolved uncertainty in the user-facing answer.

## Reference(s):

- [Research Playbook](artifact/references/research-playbook.md)
- [Feedback Contract](artifact/references/feedback-contract.md)
- [Source Scoring](artifact/references/source-scoring.md)
- [Writing Rules](artifact/references/writing-rules.md)
- [ClawHub Skill Page](https://clawhub.ai/h4444433333/skills/net-deep-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown research answers with structured JSON evidence records when external sources are used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source summaries, cross-source notes, uncertainty statements, and optional structured research-feedback records.]

## Skill Version(s):

1.0.9 (source: server release metadata and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
