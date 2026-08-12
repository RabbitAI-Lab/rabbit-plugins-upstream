## Description:

代码审查与质量检测：检查代码规范、潜在Bug、性能问题、安全漏洞，输出审查报告与改进建议。Invoke when user asks 代码审查、Code Review、代码质量、代码检查、代码优化.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shiyan521](https://clawhub.ai/user/shiyan521)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review code for structure, quality, security risks, performance issues, and style problems before release. It produces prioritized findings and concrete remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Effective code review may require the agent to inspect source, configuration, and potential secrets.

Mitigation: Use the skill only on projects the user is comfortable letting the agent inspect, and remove or rotate exposed secrets found during review.

Risk: Review findings and suggested fixes can be incomplete or incorrect.

Mitigation: Have a developer validate P0/P1 findings and proposed changes before applying them to production code.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shiyan521/skills/07-code-reviewer)
- [Publisher profile](https://clawhub.ai/user/shiyan521)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown code review report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report is named for the reviewed project and organizes findings by P0, P1, and P2 severity.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
