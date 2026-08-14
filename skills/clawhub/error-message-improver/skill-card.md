## Description:

Helps users turn vague error messages into clearer guidance that explains what failed, why it failed, and what action to take next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Application developers, support teams, SaaS operators, and affected users use this skill to turn vague error reports into actionable messages, checklists, workflows, analysis, or code-level fixes that explain failure, cause, and next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers may cause this skill to be selected for general debugging or support requests where a narrower skill is more appropriate.

Mitigation: Use the skill when the request specifically needs clearer error messages or a reusable troubleshooting workflow, and confirm the target outcome before applying its checklist or templates.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [Error messages evidence tag](https://segmentfault.com/t/error-messages)
- [Tool errors are unactionable for programmatic callers](https://github.com/The-40-Thieves/obsidian-tc/issues/784)
- [Null guard issue in blockchainMonitor.js](https://github.com/KanishJebaMathewM/Truxify/issues/13247)
- [Null guard issue in alertRouter.js](https://github.com/KanishJebaMathewM/Truxify/issues/13246)
- [Sonic Pi v5 discussion](https://news.ycombinator.com/item?id=49248771)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Markdown or plain text with optional code snippets, checklists, and workflow steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should expose assumptions, limits, validation notes, and remaining follow-up risks.]

## Skill Version(s):

0.20260814.40500 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
