## Description:

Retrieves Baidu's current hot-search rankings through Qinghu AI for users asking what is trending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Users and agents use this skill to check Baidu's current hot-search rankings and summarize trending topics, with an exported table for larger results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may install qhkit or Node and modify the local environment.

Mitigation: Prefer a preinstalled or pinned qhkit version; approve installation and avoid shell-profile changes unless needed.

Risk: Calls require a Qinghu API token and may consume paid credits.

Mitigation: Keep the token private, check the credit estimate, and obtain user approval before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-baidu-hot-search)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise response with a preview; tabular file for ten or more records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports Qinghu credits used for paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
