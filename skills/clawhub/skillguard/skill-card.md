## Description:

SkillGuard helps agents audit third-party Agent Skills before installation by submitting redacted skill source to a configured SkillGuard service and reporting pass, review, or block decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to review third-party skills, SKILL.md files, and installation candidates for prompt injection, sensitive data, dangerous commands, and supply-chain risks before trusting or enabling them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected skill source is sent to the configured SkillGuard service for audit.

Mitigation: Submit only selected, redacted skill files and verify SKILLGUARD_API_KEY plus any AI_SKILLS_API_URL override point to a trusted provider.

Risk: Secrets, credentials, personal information, or unrelated private files could be included in an audit submission.

Mitigation: Remove API keys, tokens, cookies, private keys, database passwords, personal information, and private repository credentials before submitting files.

Risk: An incomplete, missing, or risky audit response could be misread as approval to continue installation.

Mitigation: Continue only on a complete pass response; route review to a human and stop on block, timeout, empty response, parse failure, or missing fields.

## Reference(s):

- [SkillGuard homepage](https://ai-skills.open-idea.net)
- [SkillGuard ClawHub page](https://clawhub.ai/youteacher/skills/skillguard)
- [Publisher profile](https://clawhub.ai/user/youteacher)
- [API Key Configuration](references/API-KEY.md)
- [Audit Workflow](references/AUDIT-WORKFLOW.md)
- [HTTP Requests and Responses](references/HTTP-REQUESTS.md)
- [Behavior, Errors, and Decision Rules](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured audit summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prioritizes score, verdict, risk level, summary, high-risk findings, next actions, and billing headers when relevant; avoids reprinting complete source or secrets.]

## Skill Version(s):

1.0.0 (source: server release evidence and package metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
