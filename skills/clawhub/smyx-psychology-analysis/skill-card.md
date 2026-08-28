## Description:

Analyzes human mental health and psychological behavior, supports identifying common psychological problem tendencies through video analysis, and provides structured mental health analysis reports and improvement suggestions. | 心理健康分析工具，针对人的心理健康和心理行为进行分析，支持通过视频分析识别常见心理问题倾向，提供结构化心理健康分析报告和改善建议

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to analyze a provided person video or video URL for mental-health tendency signals, then receive structured reports, risk indicators, improvement suggestions, and links to historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive mental-health videos or video URLs may be sent to configured cloud or private-network services.

Mitigation: Use the skill only with consent from anyone shown, verify the configured endpoints, and confirm provider privacy and retention terms before deployment.

Risk: The skill may create or reuse a local account record and persist service tokens in the workspace database.

Mitigation: Review local storage, credential handling, access controls, and deletion procedures before enabling the skill in shared or production environments.

Risk: Mental-health analysis output may be mistaken for professional diagnosis or treatment advice.

Mitigation: Present outputs as reference information only and direct users with psychological distress to qualified mental-health professionals.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychology-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown reports, Markdown tables, or JSON returned from CLI/API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include structured mental-health analysis results, risk prompts, improvement suggestions, report links, and historical report lists.]

## Skill Version(s):

1.0.18 (source: server release metadata; artifact frontmatter: 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
