## Description:

SkillGuard helps users audit third-party Agent Skills before installation by checking SKILL.md, scripts, and reference files for prompt injection, sensitive-data exposure, dangerous commands, and supply-chain risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use SkillGuard before installing or enabling third-party Agent Skills to submit selected skill materials for risk assessment and receive a verdict, findings, and recommended next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Skill materials are sent to a hosted external audit service.

Mitigation: Confirm hosted audit use is acceptable, submit only intended files, and redact secrets, personal data, and proprietary content before auditing.

Risk: The skill requires storing SKILLGUARD_API_KEY in OpenClaw configuration.

Mitigation: Scope the key to SkillGuard, keep it out of audited source, logs, and reports, and rotate or revoke it if exposed.

Risk: The documentation is currently Chinese-only.

Mitigation: Ensure operators can accurately follow the Chinese documentation or translate and review it before deployment.

## Reference(s):

- [ClawHub SkillGuard release](https://clawhub.ai/youteacher/skills/skillguard)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/skillguard/API-KEY.md)
- [Audit workflow](https://ai-skills.open-idea.net/skill-docs/skillguard/AUDIT-WORKFLOW.md)
- [HTTP requests and responses](https://ai-skills.open-idea.net/skill-docs/skillguard/HTTP-REQUESTS.md)
- [Behavior, errors, and decision rules](https://ai-skills.open-idea.net/skill-docs/skillguard/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown or text guidance with JSON API request and response details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SKILLGUARD_API_KEY; AI_SKILLS_API_URL is optional; audit inputs should be scoped and redacted before submission.]

## Skill Version(s):

1.5.0 (source: server release metadata and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
