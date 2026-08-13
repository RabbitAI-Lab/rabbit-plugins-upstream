## Description:

Helps developers, support teams, SaaS operators, and users design clearer error messages that explain what failed, why it failed, and what action to take next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, SaaS operators, and end users use this skill to turn vague product errors into actionable messages, troubleshooting checklists, workflow notes, or implementation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad debugging or support requests because implicit invocation is enabled with generic trigger terms.

Mitigation: Narrow the trigger terms or invoke the skill explicitly when routing precision matters.

Risk: Suggested error-message wording or troubleshooting guidance may not match the product's actual failure mode.

Mitigation: Review outputs against product behavior, logs, and support policy before publishing or applying them.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [False-Positive Type Errors in Register](https://github.com/UCSBarchlab/PyRTL/issues/511)
- [Cannot use Claude Code or OpenCode - all providers return 429 rate limit](https://github.com/diegosouzapw/OmniRoute/issues/9611)
- [SegmentFault error-messages tag](https://segmentfault.com/t/error-messages)
- [Assert(): A Modern How To](https://news.ycombinator.com/item?id=49229030)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text, with code blocks or command snippets when the user asks for implementation support.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include assumptions, limits, validation notes, and concise next steps when helpful.]

## Skill Version(s):

0.20260811.40534 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
