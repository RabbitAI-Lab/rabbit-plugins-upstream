## Description:

A Chinese-language personalized learning assistant that helps agents generate project tutorials, language-learning practice, writing feedback, visual-learning explanations, study guides, and concept walkthroughs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Students, developers, and lifelong learners use this skill to request tailored tutoring, study materials, language practice, writing review, code-learning walkthroughs, and structured explanations. The skill is appropriate for educational assistance where users can review results and is not suited for decisions that require guaranteed correctness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags broad read, write, command, API, and callback capabilities without tight scope or clear user-control boundaries.

Mitigation: Require explicit user confirmation before reading files, writing files, installing packages, running shell commands, invoking external APIs, or using callback URLs.

Risk: Learning inputs may include private essays, proprietary materials, credentials, or other sensitive content.

Mitigation: Avoid sending private or proprietary content through API or callback flows unless the destination is trusted, and redact secrets from prompts and logs.

Risk: Generated tutoring, writing, study, code, or troubleshooting guidance may be incomplete or incorrect.

Mitigation: Have users review outputs before relying on them, especially for advanced academic, legal, medical, financial, or production software contexts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/learn-cog)
- [Artifact skill definition](artifact/SKILL.md)
- [SkillHub homepage from artifact metadata](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or structured JSON with explanatory text, examples, code snippets, and optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the user's learning goal, current level, preferred learning style, and any provided content.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
