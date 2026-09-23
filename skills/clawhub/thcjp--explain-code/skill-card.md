## Description:

代码 helps an agent explain code with visual diagrams, analogies, architecture overviews, and review-oriented summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to understand code snippets, functions, modules, or codebases through explanation, visual structure, and analogies. It is most relevant for code review, onboarding, debugging, and teaching code behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests write and command-execution authority that is broader than needed for code explanation.

Mitigation: Run it in a constrained workspace and prefer read-only operation unless file edits or command execution are explicitly intended.

Risk: The skill may call external services or process large codebases when explaining code.

Mitigation: Review inputs for sensitive data, limit workspace scope, and confirm external-service use before processing proprietary code.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/explain-code)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Artifact homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or structured text, with optional JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include diagrams, analogies, review summaries, troubleshooting steps, and suggested follow-up actions.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
