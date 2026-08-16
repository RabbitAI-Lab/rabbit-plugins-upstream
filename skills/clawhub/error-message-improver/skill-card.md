## Description:

Helps developers, support teams, SaaS operators, and users turn vague errors into clearer messages that explain what failed, why it failed, and what to do next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, SaaS operators, and end users use this skill to rewrite unclear errors, build reusable troubleshooting workflows, and create checklists or implementation support for clearer user feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording may activate the skill for adjacent debugging or support requests where error-message work is not intended.

Mitigation: Invoke the skill explicitly for error-message improvement tasks and ignore it for unrelated debugging or support work.

Risk: Incomplete error context can lead to rewritten messages that overstate the cause or next action.

Mitigation: Keep assumptions, limits, required inputs, and validation criteria visible in the generated output.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver)
- [False-Positive Type Errors in Register](https://github.com/UCSBarchlab/PyRTL/issues/511)
- [Clearer error message feature request](https://github.com/alexta69/metube/issues/1047)
- [Improve error messages in services](https://github.com/yrn-dev/Operator/issues/4153)
- [error-messages topic](https://segmentfault.com/t/error-messages)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional code, command, checklist, or configuration blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a tailored artifact, reusable workflow, checklist, analysis, code change, decision aid, and verification note.]

## Skill Version(s):

0.20260816.40342 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
