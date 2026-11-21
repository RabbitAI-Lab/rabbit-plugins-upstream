## Description:

从抖音公开数据中检索视频与图文、热榜、创作者作品和评论，并输出结构化结果以支持趋势与内容分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

面向内容运营、市场研究和数据分析人员，获取并分析抖音公开视频、创作者作品、评论与热榜数据，以支持选题、趋势观察和竞品分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied links or IDs may be sent to a third-party API, and the scan notes that this transfer is not disclosed in the workflow.

Mitigation: Review the external data transfer and only submit links or IDs you are comfortable sharing.

Risk: The security scan reports incomplete coverage: 31 of 53 components were fully scanned.

Mitigation: Review the partially inspected components before relying on the scan as a complete assessment.

Risk: Keyword-based account discovery may not fit every intended use.

Mitigation: Review whether account discovery is appropriate for the task before using it.

## Reference(s):

- [Release page](https://clawhub.ai/why20261/skills/douyin-trend-insights-v1)
- [Command options](references/options.md)
- [Output contract](references/contract.md)
- [Error handling](references/errors.md)
- [Service and token help](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [Structured JSON data, with concise trend or content analysis when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results vary by query and may contain public video, creator, work, comment, or trending data.]

## Skill Version(s):

1.5.0 (source: release evidence, package.json, changelog dated 2026-11-10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
