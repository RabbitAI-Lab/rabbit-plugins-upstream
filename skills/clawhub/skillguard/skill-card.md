## Description:

SkillGuard helps users audit third-party Agent Skills, SKILL.md files, and install-time security risks involving prompt injection, sensitive data, dangerous commands, and supply-chain concerns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill before installing or trusting third-party Agent Skills to submit selected, redacted skill files for remote security analysis and review the returned verdict, risk level, findings, and next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected skill text and file contents are uploaded to the SkillGuard service for analysis and may include sensitive information if users submit raw files.

Mitigation: Redact API keys, tokens, cookies, private keys, database passwords, personal information, and private repository credentials before submitting audit input.

Risk: Remote analysis may incur usage-based billing when LLM evaluation is used.

Mitigation: Review billing headers and usage fields, and do not assume a fixed price for audits.

Risk: Incomplete, missing, or non-pass audit responses can leave installation risk unresolved.

Mitigation: Proceed with automatic installation only when the response is complete, parseable, and returns a pass verdict; fail closed on review, block, timeout, empty response, or missing fields.

## Reference(s):

- [SkillGuard homepage](https://ai-skills.open-idea.net)
- [ClawHub skill listing](https://clawhub.ai/youteacher/skills/skillguard)
- [API Key configuration](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/skillguard/references/API-KEY.md)
- [Audit workflow](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/skillguard/references/AUDIT-WORKFLOW.md)
- [HTTP requests and responses](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/skillguard/references/HTTP-REQUESTS.md)
- [Behavior, errors, and decision rules](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/skillguard/references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, text]

**Output Format:** [Markdown with inline shell commands and JSON-oriented API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes verdict, risk level, findings, next actions, and billing headers without reprinting full source files or secrets.]

## Skill Version(s):

1.2.0 (source: server release metadata and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
