## Description:

Searches and browses the Huawei Cloud skill catalog, retrieves skill details, and guides users through installing selected skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Huawei Cloud users and developers use the skill to find skills by keyword or category, review skill descriptions, and install a selected skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A discovery request can lead to installing and executing another skill.

Mitigation: For search-only requests, stop after presenting results. Before installation or execution, review the selected skill at a fixed revision.

Risk: Telemetry is sent during search and installation, and the documented opt-out does not stop installation-count requests as written.

Mitigation: Disclose telemetry before use and do not treat SKILL_QUALITY_REPORT=0 as a complete opt-out; review outbound requests before installation.

Risk: The externally downloaded telemetry CLI and skills installed by this skill are outside the supplied security review.

Mitigation: Review the telemetry CLI and each selected skill separately before installing or running them.

## Reference(s):

- [Acceptance criteria](artifact/references/acceptance-criteria.md)
- [CLI installation and telemetry guide](artifact/references/cli-installation-guide.md)
- [IAM policies and permissions](artifact/references/iam-policies.md)
- [Verification method](artifact/references/verification-method.md)
- [Huawei Cloud KooCLI documentation](https://support.huaweicloud.com/cli/index.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with search results, skill descriptions, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results, skill descriptions, and optional installation commands]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
