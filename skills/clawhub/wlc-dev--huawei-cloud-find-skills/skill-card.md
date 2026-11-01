## Description:

Finds Huawei Cloud agent skills by keyword or category, retrieves optional skill details, and provides commands for installing a match.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users use it to find Huawei Cloud skills for a service or task, review available details, and install a selected skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can lead to installing or executing a discovered skill without separate approval.

Mitigation: Require explicit approval for each installation or execution, and review the skill's source and instructions first.

Risk: Bundled reference instructions can expose cloud credentials.

Mitigation: Remove credential-printing commands and unrelated creator references; rotate any credentials already exposed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-find-skills)
- [GitCode skills index repository](https://gitcode.com/2501_91318609/skills-for-index)
- [Huawei Cloud skills repository referenced for details and installation](https://github.com/huaweicloud/huaweicloud-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown skill search results with optional skill details and shell installation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on an online index; details for selected skills may be retrieved from public repositories.]

## Skill Version(s):

1.0.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
