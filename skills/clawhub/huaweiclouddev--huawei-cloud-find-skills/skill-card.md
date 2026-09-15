## Description:

Searches, browses, and helps install Huawei Cloud agent skills by querying public skill indexes and presenting matching skill details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to find Huawei Cloud skills by keyword or category, review matching skill details, and install the selected skill for follow-on Huawei Cloud tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security verdict is suspicious because the skill can search and install Huawei Cloud skills while using telemetry, local session or credential access, and unpinned installation paths.

Mitigation: Review before installing or executing, run in an isolated environment without ambient Huawei Cloud credentials or sensitive agent session stores, and verify exact installer package versions and immutable skill revisions.

Risk: Execution quality reporting may send run metadata unless disabled.

Mitigation: Set SKILL_QUALITY_DISABLE=1 when telemetry is not acceptable for the environment.

Risk: Installation commands use npx-based package execution and external repositories.

Mitigation: Use only reviewed installer versions and approved repository revisions before allowing installation in managed environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-find-skills)
- [IAM policies](references/iam-policies.md)
- [Verification method](references/verification-method.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Search script](scripts/search-skills.py)
- [KooCLI check script](scripts/check-koocli.py)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and search-result text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results include skill names, category/service paths, descriptions, trigger previews, and matched keywords.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
