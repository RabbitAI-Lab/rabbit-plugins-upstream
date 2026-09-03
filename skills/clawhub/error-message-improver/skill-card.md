## Description:

Helps application developers, support teams, SaaS operators, and users turn vague errors into clearer messages that explain what failed, why it failed, and what action to take next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Application developers, support teams, SaaS operators, and affected users use this skill to rewrite, plan, or review error-message workflows so failures are easier to troubleshoot and act on.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be invoked for broad debugging, support, or productivity requests beyond explicit error-message rewrites.

Mitigation: Prefer explicit invocation when error-message improvement is intended, and review outputs before applying suggested code or support-process changes.

Risk: Generated guidance could make error text inaccurate, misleading, or incomplete.

Mitigation: Validate proposed messages against the actual failure mode, user impact, and available remediation path before release.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional code, command, checklist, workflow, and verification sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state assumptions, limits, and validation notes when useful.]

## Skill Version(s):

0.20260831.40551 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
