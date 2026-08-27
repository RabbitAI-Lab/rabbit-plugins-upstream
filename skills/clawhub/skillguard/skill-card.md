## Description:

SkillGuard audits third-party Agent Skill files before installation to identify prompt injection, sensitive data exposure, dangerous commands, and supply-chain risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill users use SkillGuard to scan third-party Agent Skill source, SKILL.md files, scripts, configuration, and references before installation or automation. It helps evaluate prompt injection, secret-handling, dangerous command, and supply-chain risks and returns risk conclusions that support pass, review, or block decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected skill contents and metadata are sent to the remote SkillGuard API.

Mitigation: Send only files needed for the audit and redact API keys, tokens, cookies, private keys, personal data, private repository credentials, and unrelated private files before submission.

Risk: Incomplete, malformed, timed-out, or missing audit responses could be mistaken for a successful safety result.

Mitigation: Treat only complete and parseable pass responses as eligible for follow-on automation; fail closed on review, block, timeout, empty response, or missing fields.

Risk: Repeated audit submissions can create duplicate work or unclear billing state.

Mitigation: Use an Idempotency-Key for each audit request, reuse it for retries of the same input, and generate a new key only when the submitted input changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/skillguard)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/skillguard/references/API-KEY.md)
- [Audit Workflow](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/skillguard/references/AUDIT-WORKFLOW.md)
- [HTTP Requests and Responses](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/skillguard/references/HTTP-REQUESTS.md)
- [Behavior, Errors, and Decision Rules](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/skillguard/references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [guidance, text, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with shell command examples and JSON API request and response details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SKILLGUARD_API_KEY and sends selected, redacted skill contents and metadata to the SkillGuard audit API.]

## Skill Version(s):

1.3.0 (source: server-resolved release metadata and artifact metadata.packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
