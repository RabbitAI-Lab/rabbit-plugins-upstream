## Description:

天台宗教理研究与结构化报告生成，支持简单问答和深度研究两种模式，并要求所有论断标注 CBETA 出处。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gouchunlei2-png](https://clawhub.ai/user/gouchunlei2-png)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, practitioners, and developers use this skill to answer Tiantai Buddhist doctrine questions, compare doctrinal systems, interpret patriarchal writings, and produce sourced structured research reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms may be sent to configured knowledge-base or CBETA services.

Mitigation: Avoid submitting sensitive or confidential search terms unless those services are approved for the intended use.

Risk: Online document editing may use Tencent Docs when explicitly requested.

Mitigation: Use local document handling for sensitive drafts unless Tencent Docs is an acceptable destination.

## Reference(s):

- [CBETA Online Reader](https://cbetaonline.dila.edu.tw/zh/{work_id}_{juan})
- [CBETA Search API (Stable)](https://cbdata.dila.edu.tw/stable/search?q=關鍵詞)
- [CBETA Search API (Dev)](https://cbdata.dila.edu.tw/dev/search?q=關鍵詞)
- [CBETA Online Search API](https://api.cbetaonline.cn/search?q=關鍵詞)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with source citations and structured sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include definitions, original-source excerpts, supplemental notes, chaptered reports, source tables, CBETA links, and limitations when source coverage is incomplete.]

## Skill Version(s):

1.1.1 (source: server release metadata; artifact frontmatter shows 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
