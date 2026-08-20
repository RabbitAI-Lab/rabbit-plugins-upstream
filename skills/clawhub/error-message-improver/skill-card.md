## Description:

Helps application developers, support teams, SaaS operators, and users turn vague error messages into clearer guidance that explains what failed, why it failed, and what action to take next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, SaaS operators, and end users use this skill to draft, review, or implement clearer error messages and troubleshooting workflows. It produces actionable wording, checklists, workflows, analysis, code changes, or decision support for error-message improvement tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger language may activate the skill for general debugging or support requests.

Mitigation: Narrow invocation keywords or review activation policy before deployment when predictable routing is required.

Risk: Generated error-message guidance could be inaccurate if the user provides incomplete product behavior, logs, or support-policy context.

Mitigation: Review proposed wording or code changes against actual failure modes, logs, and escalation paths before publishing.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [Split v3/performance/expid into multiple performance endpoints](https://github.com/BSC-ES/autosubmit-api/issues/321)
- [Custom Provider Fails with HTTP 404 Despite Correct Configuration](https://github.com/NousResearch/hermes-agent/issues/89334)
- [SegmentFault error-messages topic](https://segmentfault.com/t/error-messages)
- [The Benchmarkpocalypse](https://news.ycombinator.com/item?id=49342677)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text, optionally including checklists, code blocks, shell commands, or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include stated assumptions, validation notes, remaining risks, and next-step guidance.]

## Skill Version(s):

0.20260819.45504 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
