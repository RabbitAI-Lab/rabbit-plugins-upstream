## Description:

Helps developers, support teams, and SaaS operators turn vague errors into clearer messages that explain what failed, why it failed, and what action to take next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, and SaaS operators use this skill to draft, review, and operationalize clearer error messages, support responses, troubleshooting checklists, or lightweight implementation changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording could route the skill into general support or debugging conversations where error-message rewriting is not the user's intent.

Mitigation: In sensitive environments, narrow the routing terms or invoke the skill explicitly only when the task is to improve error messages or troubleshooting communication.

Risk: Clearer wording can still be misleading if it is created without enough product, failure-mode, or support-policy context.

Mitigation: Review generated messages against known failure causes, user-safe next steps, and support escalation policy before publishing them.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/error-message-improver)
- [GitHub issue: invalid tab error handling](https://github.com/Ixotic27/The-Leetcode-City/issues/1329)
- [GitHub issue: enrichment provider proposal](https://github.com/srikanth235/centraid/issues/731)
- [SegmentFault tag: error-messages](https://segmentfault.com/t/error-messages)
- [Hacker News: Assert(): A Modern How To](https://news.ycombinator.com/item?id=49229030)
- [Hacker News: Eight Myths on Software Engineering and GenAI](https://news.ycombinator.com/item?id=49179820)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, plain text, code snippets, checklists, or implementation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, validation notes, and follow-up risks when helpful.]

## Skill Version(s):

0.20260810.40316 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
