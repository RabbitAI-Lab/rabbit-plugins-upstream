## Description:

Automatically detects and counts livestock or poultry individuals from barn or passage camera images/videos, outputting total headcount with confidence for fast inventory. | 自动识别并统计畜禽数量，实现快速存栏盘点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and livestock managers can use the skill to count animals in barn or passage images and videos, review confidence and area counts, and look up previous inventory reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and videos are uploaded for cloud analysis.

Mitigation: Submit only footage authorized for external processing and avoid including unrelated sensitive material.

Risk: Persisted account and token state can mix users’ reports in a shared workspace.

Mitigation: Use an isolated workspace per user and review or clear persisted account credentials and state.

Risk: The export-only option may submit media unexpectedly, and configured API secrets may be copied into identity fields.

Mitigation: Avoid the export-only option until its behavior is corrected, and keep API secrets out of identity settings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-counting-analysis)
- [Skill introduction video](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Report links]

**Output Format:** [Structured counting reports and Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include total and area counts, confidence, and links to historical reports.]

## Skill Version(s):

1.0.13 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
