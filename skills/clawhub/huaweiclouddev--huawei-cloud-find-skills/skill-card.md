## Description:

Searches, browses, and helps install Huawei Cloud agent skills from the Huawei Cloud skills index.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to discover Huawei Cloud-related agent skills by keyword or category, inspect matching skill details, and receive installation commands for the selected skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide installation of other skills, which may add new instructions to the local agent environment.

Mitigation: Review the matched skill name, source, and exact install command before approving installation.

Risk: The install flow may contact GitCode, GitHub, ClawHub, and a Huawei install-count endpoint.

Mitigation: Confirm network access and user consent before running search or installation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-find-skills)
- [Huawei Cloud skills repository](https://github.com/huaweicloud/huaweicloud-skills)
- [GitCode skills index API](https://gitcode.com/api/v5/repos/2501_91318609/skills-for-index/contents/skills-index/index.json?ref=main)
- [GitCode CN/EN keyword map API](https://gitcode.com/api/v5/repos/2501_91318609/skills-for-index/contents/skills-index/cn-en-map.json?ref=main)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with command examples and search-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include install commands and external skill-detail URLs for user review.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
