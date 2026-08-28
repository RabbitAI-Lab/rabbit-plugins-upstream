## Description:

依托全球企业数据库调取人员对应的院校详细资料，获取完整教育档案，梳理目标人员就读院校及整体教育背景，辅助开展客户尽调与人脉分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, researchers, analysts, and external business users use this skill to retrieve detailed school records by school ID for education verification, institution research, academic network analysis, and customer due diligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores the UPKUAJING API key in a local plaintext file.

Mitigation: Use the skill only on trusted machines, restrict local file access, and rotate the API key if the host or account may have been exposed.

Risk: The school detail lookup is a paid API call.

Mitigation: Tell the user that the query may incur charges and wait for explicit confirmation before running paid requests.

Risk: Error reports may include request context.

Mitigation: Review the error-report context with the user before submission and avoid sending unnecessary personal, credential, or sensitive business data.

Risk: Version checks and diagnostic calls contact the UPKUAJING service in addition to the primary lookup.

Mitigation: Install and run the skill only when this network behavior is acceptable for the environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-person-school-detail-zh)
- [upkuajing publisher profile](https://clawhub.ai/user/upkuajing)
- [Upkuajing homepage](https://www.upkuajing.com)
- [School detail API reference](references/school-detail-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid API calls return school details, fee information, and request identifiers when successful.]

## Skill Version(s):

1.0.3 (source: evidence release and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
