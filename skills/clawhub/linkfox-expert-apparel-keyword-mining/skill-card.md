## Description:

专为服装类目设计的关键词挖掘与语义打标一体化工具，从商品图提炼 product_context，用 Amazon Suggestions 挖出长尾词，通过 LLM 语义打标识别完整属性短语，并自动完成肯定词库、否定词库和待确认词库分流。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and listing/PPC specialists use this skill to mine apparel-specific long-tail keywords, classify them against product attributes, and prepare structured keyword libraries for listing optimization and advertising review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, media URLs, product context, mined keywords, and keyword-library data may be sent to LinkFox-configured services during normal use.

Mitigation: Use only with data that is approved for those services and confirm the configured LINKFOX_TOOL_GATEWAY before running workflows.

Risk: The bundled upload capability can create publicly accessible URLs for local files.

Mitigation: Upload only files intended for public sharing, and treat generated Excel, JSON, report files, and OSS URLs as potentially sensitive.

Risk: LLM tagging and keyword classification depend on accurate product_context and may misclassify ambiguous apparel attributes.

Mitigation: Extract product attributes before mining, pass product_context from a file, and review positive, negative, and review keyword sheets before using them for listings or PPC.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-apparel-keyword-mining)
- [Apparel keyword expert guide](skills/linkfox-apparel-keyword-expert/SKILL.md)
- [Apparel keyword expert CLI notes](skills/linkfox-apparel-keyword-expert/CLAUDE.md)
- [AI text generation API reference](skills/linkfox-aigc-textgen/references/api.md)
- [Keyword library API reference](skills/linkfox-keyword-library/references/api.md)
- [File upload API reference](skills/linkfox-file-upload/references/api.md)
- [Report layout reference](skills/linkfox-report-generator/references/analysis-layouts.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples, plus generated Excel, JSON, and optional HTML report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primary workflow produces a seven-sheet Excel workbook covering summary, tagged detail, positive keywords, negative keywords, review keywords, complete attribute phrases, and raw mined suggestions.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
