## Description:

Helps developers, support teams, and SaaS operators turn vague errors into clearer messages that explain what failed, why it failed, and what action to take next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, SaaS operators, and users use this skill to improve unclear error messages, troubleshooting workflows, checklists, analysis, or implementation guidance. It helps produce concise artifacts that make failures, causes, and next actions easier to understand.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for broad support or debugging requests.

Mitigation: Invoke it explicitly when the desired task is improving error messages or related troubleshooting artifacts.

Risk: Generated wording for errors may omit context or suggest the wrong next action if the input error details are incomplete.

Mitigation: Review the final message against the actual failure mode, known causes, and supported remediation steps before publishing it to users.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver)
- [Improve Form Validation UX](https://github.com/Stellar-Veriphy/Stellar-Veriphy/issues/415)
- [Return better error messages due to Azure.RequestFailedExceptions](https://github.com/microsoft/mcp/issues/3394)
- [iOS Tunnel setup for local BrowserStack runs is undocumented](https://github.com/cybersemics/em/issues/5111)
- [Authentication failure on login invalid_code](https://github.com/filcdev/filc/issues/283)
- [Error messages topic](https://segmentfault.com/t/error-messages)
- [Python's pre-declared constants are kinda weird](https://news.ycombinator.com/item?id=49443186)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text, with code blocks or configuration snippets when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tailored artifacts, reusable checklists, workflows, analysis, implementation support, and a short verification note.]

## Skill Version(s):

0.20260827.40448 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
