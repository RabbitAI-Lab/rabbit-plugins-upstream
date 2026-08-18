## Description:

Helps agents prepare, validate, and publish local skills to ClawHub, Tencent SkillHub, and Lenovo Open Platform using platform-specific allowlists and release records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to prepare filtered release directories, check platform-specific allowlists, publish individual or multiple skills, and record publish status across supported public skill platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Lenovo batch uploader can upload or update many remote skills in one run.

Mitigation: Review the Lenovo allowlist and generated skill list before running the batch script, and run preparation or dry-run checks for individual skills first.

Risk: Publishing commands can expose credentials or publish unintended content if local configuration is copied or commands are reused carelessly.

Mitigation: Use platform login flows instead of embedding real tokens in shell history, keep real allowlist and sync-record files local, and inspect the filtered temporary publish directory before upload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cat-xierluo/skills/skill-publish-sync)
- [Publisher homepage](https://github.com/cat-xierluo/legal-skills)
- [ClawHub CLI documentation](https://docs.openclaw.ai/clawhub/cli)
- [ClawHub Skill Format documentation](https://docs.openclaw.ai/clawhub/skill-format)
- [Tencent SkillHub publish tutorial](https://skillhub.cn/tutorials#publish-via-cli)
- [Lenovo Open Platform](https://open.lenovomm.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with inline shell commands and YAML configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to create temporary publish directories and update local sync records when the user approves a publish workflow.]

## Skill Version(s):

1.7.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
