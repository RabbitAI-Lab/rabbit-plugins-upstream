## Description:

Performs special video analysis on behavioral characteristics of children with autism, identifies core symptom features, provides structured analysis reports and intervention recommendations. | 孤独症谱系障碍行为分析工具，针对儿童孤独症行为特征进行专项视频分析，识别核心症状特征，提供结构化分析报告和干预建议

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as parents, educators, and relevant professionals use this agent to submit child behavior videos or URLs for ASD-oriented screening analysis, structured reports, and intervention suggestions. The agent can also return cloud-sourced historical report lists associated with the user's identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child-health videos, URLs, and identity-linked report requests are sent to the publisher's cloud service.

Mitigation: Use only with appropriate consent and after reviewing the publisher's retention, deletion, and access practices.

Risk: The skill may create or reuse local workspace state containing identifiers and tokens.

Mitigation: Install in a controlled workspace, restrict file access, and remove local state or tokens when no longer needed.

Risk: ASD-oriented analysis output may be mistaken for a clinical diagnosis.

Mitigation: Present outputs as screening support only and route concerning findings to qualified medical professionals for evaluation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-autism-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Structured analysis reports, Markdown tables, report links, and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk or recognition results, intervention suggestions, and cloud-sourced historical report listings.]

## Skill Version(s):

1.0.12 (source: server release metadata, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
