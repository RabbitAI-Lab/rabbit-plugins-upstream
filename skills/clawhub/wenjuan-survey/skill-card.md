## Description:

问卷网 helps agents create, publish, edit, monitor, and export Wenjuan surveys, forms, votes, and assessments through documented Node.js workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wenjuanwang](https://clawhub.ai/user/wenjuanwang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create and manage Wenjuan survey, vote, form, and assessment projects, including publishing, reporting, response export, and high-level response statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup and update paths can run high-impact installation actions.

Mitigation: Install Node.js from trusted channels, use the locked npm dependencies, and review setup or update commands before running them, especially unattended setup.

Risk: The skill can receive Wenjuan account access and store local authentication tokens.

Mitigation: Store tokens in a private WENJUAN_TOKEN_DIR and remove ~/.wenjuan and the skill .wenjuan/auth.json when finished on shared systems.

Risk: Changing the Wenjuan host can direct authenticated actions to an unintended endpoint.

Mitigation: Keep WENJUAN_HOST unset unless intentionally using a trusted endpoint.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wenjuanwang/skills/wenjuan-survey)
- [Wenjuan homepage](https://www.wenjuan.com)
- [Skill overview](references/skill_overview.md)
- [Create survey workflow](references/create_survey.md)
- [Authentication](references/auth.md)
- [Project JSON structure guide](references/project_json_structure_guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON survey structures, Wenjuan URLs, and generated or downloaded files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update Wenjuan projects and local credential, poster, or export files after authentication and required user confirmation.]

## Skill Version(s):

1.0.15 (source: server release metadata, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
