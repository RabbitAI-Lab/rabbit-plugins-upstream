## Description:

Helps developers, support teams, SaaS operators, and users turn vague error messages into clearer explanations of what failed, why it failed, and what action to take next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, SaaS operators, and end users use this skill to rewrite or structure unclear error-message guidance into actionable troubleshooting information. It can produce tailored guidance, reusable checklists, workflows, analysis, code-oriented suggestions, and verification notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for general debugging or support requests where a narrower error-message helper was intended.

Mitigation: Use it for error-message rewriting, troubleshooting workflows, support checklists, or related guidance, and confirm the user's context before applying broad recommendations.

Risk: Generated guidance could describe an incorrect failure cause or remediation if the available logs or reproduction details are incomplete.

Mitigation: Validate proposed messages and next steps against observed behavior, logs, reproduction steps, and product support policy before publishing them.

## Reference(s):

- [Requirement Plan](artifact/references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver)
- [Autosubmit API issue on performance endpoint errors](https://github.com/BSC-ES/autosubmit-api/issues/321)
- [Swiz issue on session prefix collision](https://github.com/mherod/swiz/issues/824)
- [HerLedger issue on auth form protections](https://github.com/Stellar-Deejah/HerLedger/issues/30)
- [SegmentFault error-messages topic](https://segmentfault.com/t/error-messages)
- [Hacker News discussion signal](https://news.ycombinator.com/item?id=49248771)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with optional checklists, code blocks, templates, workflow steps, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state assumptions, visible limits, and any remaining risks or follow-up work when helpful.]

## Skill Version(s):

0.20260818.40417 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
