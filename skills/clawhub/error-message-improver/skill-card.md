## Description:

Helps developers, support teams, SaaS operators, and users turn vague error messages into clearer guidance that explains what failed, why it failed, and what action to take next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Application developers, support teams, SaaS operators, and users use this skill to produce clearer error-message copy, troubleshooting workflows, checklists, analysis, code changes, and verification notes for support or debugging situations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit triggers may activate the skill during general debugging or support conversations.

Mitigation: Prefer explicit invocation when the desired task is specifically error-message improvement.

Risk: Generated error-message guidance may be incomplete or misleading if the underlying failure context is missing.

Mitigation: Check the output against the stated outcome, constraints, available inputs, and success criteria before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/error-message-improver)
- [Requirement Plan](references/requirement-plan.md)
- [Water Furnace Error](https://github.com/home-assistant/core/issues/181810)
- [External PDF viewer error messages](https://github.com/texstudio-org/texstudio/issues/4661)
- [error-messages topic](https://segmentfault.com/t/error-messages)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with optional code blocks, command snippets, checklists, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include visible assumptions, limits, validation notes, and follow-up work when helpful.]

## Skill Version(s):

0.20260916.221748 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
