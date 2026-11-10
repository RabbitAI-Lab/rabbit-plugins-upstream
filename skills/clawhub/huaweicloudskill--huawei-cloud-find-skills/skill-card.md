## Description:

Helps users find Huawei Cloud agent skills by keyword or category, review skill details, and install a selected skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud users can search the Huawei Cloud skill catalog, inspect matching skill details, and install a chosen skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search and installation workflows report usage telemetry to external endpoints.

Mitigation: Review the disclosed telemetry and destinations; the skill documents SKILL_QUALITY_REPORT=0 as the opt-out setting.

Risk: The documented flow includes automatic CLI setup and can continue from search to installing and executing a matching skill.

Mitigation: Review the setup and subsequent skill instructions before allowing those steps, and keep actions within the user's requested scope.

Risk: The security scan was partial, leaving some installer behavior unassessed.

Mitigation: Inspect the installer behavior and dependencies before deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-find-skills)
- [Huawei Cloud KooCLI installation guide](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud skills index repository](https://gitcode.com/developer-skill/skills-group-contribution)
- [CLI installation guide](references/cli-installation-guide.md)
- [IAM policies and access requirements](references/iam-policies.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown search results, skill details, and installation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may include skill names, categories, services, descriptions, and matching terms.]

## Skill Version(s):

1.0.12 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
