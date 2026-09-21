## Description:

SkillGuard helps agents audit third-party Agent Skills before installation by checking skill files for prompt injection, sensitive data exposure, dangerous commands, and supply-chain risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to submit selected, redacted Skill files to the SkillGuard API and interpret pass, review, or block audit results before installing or enabling another skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected skill files are sent to the SkillGuard service for analysis.

Mitigation: Submit only necessary, redacted files and do not include secrets, private personal data, or unrelated local files.

Risk: The skill depends on a SkillGuard API key stored in OpenClaw configuration.

Mitigation: Store the key only in the configured environment variable, avoid pasting full keys into chat or logs, and rotate keys if exposure is suspected.

Risk: A non-pass or incomplete audit response may require human judgment before installation.

Mitigation: Treat review, block, timeout, empty, truncated, or unparsable responses as stop conditions until a human reviews the findings.

Risk: Changing the API root could send audit content to an untrusted endpoint.

Mitigation: Keep AI_SKILLS_API_URL pointed at a trusted SkillGuard endpoint unless the operator has explicitly approved another endpoint.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/skillguard)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/skillguard/API-KEY.md)
- [Audit Workflow](https://ai-skills.open-idea.net/skill-docs/skillguard/AUDIT-WORKFLOW.md)
- [HTTP Requests and Responses](https://ai-skills.open-idea.net/skill-docs/skillguard/HTTP-REQUESTS.md)
- [Behavior, Errors, and Decision Rules](https://ai-skills.open-idea.net/skill-docs/skillguard/BEHAVIOR-RULES.md)
- [Local API Key Reference](references/API-KEY.md)
- [Local Audit Workflow Reference](references/AUDIT-WORKFLOW.md)
- [Local HTTP Requests Reference](references/HTTP-REQUESTS.md)
- [Local Behavior Rules Reference](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with JSON and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SKILLGUARD_API_KEY; optional AI_SKILLS_API_URL overrides the default API root.]

## Skill Version(s):

1.5.2 (source: release metadata and packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
