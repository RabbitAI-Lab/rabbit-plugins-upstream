## Description:

亚马逊 ABA 新词挖掘专家，用于发现季节性爆发词、趋势词、排名跃升词、长尾联想词和 Widget 类目卡关键词，并导出 CSV/Excel 结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and marketplace analysts use this agent to mine emerging search demand from ABA data, Amazon suggestions, and Widget category cards, then translate and export keyword sets for review. It is intended for keyword discovery workflows, not general listing writing, image generation, or unrelated product analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Amazon keyword queries and LinkFox API credentials to LinkFox-controlled services through configurable gateway URLs.

Mitigation: Install only if you trust LinkFox with these queries and credentials, and confirm gateway environment variables point to expected LinkFox HTTPS hosts before use.

Risk: The bundle includes account, billing, and public upload flows that can affect a LinkFox account or expose chosen files.

Mitigation: Do not provide SMS codes, start payment orders, or upload/share files unless those actions are intentional for the task.

Risk: Keyword results, translations, reports, and caches are written to local LinkFox output directories.

Mitigation: Review and clean local output and cache directories after sensitive work.

## Reference(s):

- [ABA New Keyword Miner API](skills/linkfox-aba-new-keyword-miner/references/api.md)
- [ABA Intelligent Query API](skills/linkfox-aba-intelligent-query/references/api.md)
- [Amazon Suggestion Miner API](skills/linkfox-amazon-suggestion-miner/references/api.md)
- [Amazon Widget Miner API](skills/linkfox-amazon-widget-miner/references/api.md)
- [AIGC Text Generation API](skills/linkfox-aigc-textgen/references/api.md)
- [Report Generator Layouts](skills/linkfox-report-generator/references/analysis-layouts.md)
- [File Upload API](skills/linkfox-file-upload/references/api.md)

## Skill Output:

**Output Type(s):** [guidance, API calls, shell commands, files]

**Output Format:** [Conversational guidance plus JSON, CSV, Excel, and HTML files produced by invoked LinkFox subskills.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include keyword previews in conversation and saved artifacts under the local LinkFox session output directory.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact nested metadata lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
