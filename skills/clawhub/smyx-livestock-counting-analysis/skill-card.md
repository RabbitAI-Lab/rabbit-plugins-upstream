## Description:

Automatically detects and counts livestock or poultry individuals from barn or passage camera images/videos, outputting total headcount with confidence for fast inventory. | 自动识别并统计畜禽数量，实现快速存栏盘点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to count livestock or poultry from barn, pen, or passage camera images and videos. It returns inventory counts, partition counts, confidence, and report links for fast livestock inventory workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends barn images or videos and identity-linked requests to external lifeemergence.com services.

Mitigation: Use only media approved for external processing and confirm that users understand the cloud-service dependency before deployment.

Risk: The skill can create or reuse a local default identity and query cloud report history automatically.

Mitigation: Review identity handling and report-access behavior in the target environment, and restrict execution to users authorized to view the associated reports.

Risk: Service tokens may be stored in a local workspace database.

Mitigation: Run the skill in a controlled workspace, protect local storage, and rotate or revoke tokens according to the service operator's policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-counting-analysis)
- [API 接口文档](references/api_doc.md)
- [API接口文档](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include total livestock count, partition counts, confidence, analysis time, and report links.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
