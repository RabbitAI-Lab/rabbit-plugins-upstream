## Description:

Helps application developers, support teams, SaaS operators, and users turn vague error messages into clearer guidance that explains what failed, why it failed, and what to do next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, SaaS operators, and affected users use this skill to rewrite or plan clearer error messages, troubleshooting workflows, checklists, and implementation guidance for blocked workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for broad debugging or support requests where the user does not specifically need error-message improvement.

Mitigation: Use it when the requested outcome is to make an error clearer, more actionable, or easier to troubleshoot; otherwise confirm the intended support task before relying on its workflow.

Risk: Suggested wording or troubleshooting steps could misstate the cause of an error when the available context is incomplete.

Mitigation: Preserve visible assumptions, distinguish known facts from likely causes, and validate the final message against the provided logs, user impact, and next action.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [Skill page](https://clawhub.ai/kyro-ma/skills/error-message-improver)
- [Create or update the affected functions to be accessible in main.js](https://github.com/tadanobutubutu/screeps/issues/108000)
- [Add comprehensive error types](https://github.com/ChainLearnOfficial/chainlearn-contracts/issues/218)
- [Missing Signed-off-by trailer causing DCO check failure on PR submissions](https://github.com/Ikalus1988/MisakaNet/issues/1381)
- [Optimize automation scripts for performance](https://github.com/lightspeedwp/.github/issues/2390)
- [SegmentFault error-messages tag](https://segmentfault.com/t/error-messages)
- [Python's pre-declared constants are kinda weird](https://news.ycombinator.com/item?id=49443186)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Markdown with optional code snippets, checklists, and workflow notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, validation notes, and follow-up risks when useful.]

## Skill Version(s):

0.20260830.92238 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
