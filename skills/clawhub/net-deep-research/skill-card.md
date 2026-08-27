## Description:

Performs deep multi-source internet research for complex web truth-finding, cross-source fact checking, authenticity checks, and online verification tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[h4444433333](https://clawhub.ai/user/h4444433333)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and other external users use this skill when a task needs deeper online verification than a routine lookup, including multi-source research, conflict resolution, source scoring, and authenticity checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send research source metadata, claim summaries, conflicts, URL candidates, and usefulness signals to shoggoth.vip during web research.

Mitigation: Use it only when external processing is acceptable; avoid confidential investigations, private or internal URLs, and sensitive topics unless that data sharing is approved.

Risk: Deep web research can still produce incomplete or misleading conclusions when sources are stale, contradictory, or low quality.

Mitigation: Rely on the skill's multi-round, conflict-aware workflow, source scoring, uncertainty notes, and explicit counter-evidence checks before acting on findings.

Risk: Explicit Report Mode may generate a report file from collected research findings.

Mitigation: Review generated reports before sharing, especially when the research topic is sensitive or includes third-party claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/h4444433333/skills/net-deep-research)
- [Feedback Contract](references/feedback-contract.md)
- [Research Playbook](references/research-playbook.md)
- [Source Scoring](references/source-scoring.md)
- [Writing Rules](references/writing-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Structured Markdown answers, optional report files, and concise guidance with source notes and uncertainty.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a PDF or Markdown report in explicit Report Mode; default runs can send minimal structured research evidence to an external backend after using external sources.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact bundle version 1.1.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
