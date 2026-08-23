## Description:

ABA搜索词周快照速查（SFR+Top ASIN点击/转化份额）与Amazon关键词挖掘扩展（搜索建议词扩展+Widget分类卡片挖掘），批量产出长尾词库并导出。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to look up weekly ABA search-frequency rank and Top ASIN click/conversion share, expand Amazon search suggestions, mine widget category terms, and export keyword libraries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses LinkFox API credentials and may send keyword or prompt data to external services.

Mitigation: Install only in environments approved for those credentials and data; avoid sending confidential prompts or keyword lists.

Risk: The bundled file-upload behavior can create public OSS links.

Mitigation: Disable or remove the upload subskill when it is not needed, and upload only files intended for public access.

Risk: The package writes session data and generated exports or reports locally.

Mitigation: Run it in a workspace where local data retention is acceptable, and review or remove generated session files after use.

Risk: The package includes broader AIGC, feedback-reporting, onboarding-install, and skill-editing behaviors beyond ABA lookup and mining.

Mitigation: Review or remove bundled behaviors that are unnecessary for the intended ABA keyword workflow before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-aba-keyword-lookup-mining)
- [ABA snapshot API reference](skills/amazon-aba-kw-snapshot/references/api.md)
- [ABA snapshot contract](skills/amazon-aba-kw-snapshot/references/contract.json)
- [ABA intelligent query API reference](skills/linkfox-aba-intelligent-query/references/api.md)
- [Amazon suggestion miner API reference](skills/linkfox-amazon-suggestion-miner/references/api.md)
- [Amazon widget miner API reference](skills/linkfox-amazon-widget-miner/references/api.md)
- [File upload API reference](skills/linkfox-file-upload/references/api.md)
- [Report component library](skills/linkfox-report-generator/references/analysis-layouts.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, files]

**Output Format:** [Markdown tables, JSON responses, Excel or CSV exports, shell command guidance, and HTML report file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write JSON, xlsx, CSV, HTML, and session metadata files locally; may return public download or upload URLs when requested.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
