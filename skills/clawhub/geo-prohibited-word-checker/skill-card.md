## Description: <br>
GEO/SEO内容违禁词检测与智能替换，用于检测文章中的广告法违禁词、夸大宣传词、违法内容词和误导性词汇，并根据上下文生成保留原意的替换方案。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lijian2017](https://clawhub.ai/user/lijian2017) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content authors, SEO/GEO operators, and agents use this skill to scan Chinese article drafts for prohibited terms, review detected matches by category, and produce compliant replacement text or cleaned files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automated content rewriting can alter draft meaning or save changes before the user has reviewed them. <br>
Mitigation: Require confirmation before saving rewritten files and review the comparison table for meaning changes. <br>
Risk: Paid mode sends API-key-bearing verification requests to the configured endpoint. <br>
Mitigation: Set GEO_API_ENDPOINT only to a trusted HTTPS service and use local/free mode for sensitive drafts. <br>
Risk: Administrative deployment examples include credential-bearing requests. <br>
Mitigation: Avoid putting admin tokens in URLs and keep deployment/admin operations separate from normal agent use. <br>
Risk: The prohibited-word list may not match every moderation or legal requirement. <br>
Mitigation: Review the word list and treat results as screening support rather than a final compliance decision. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lijian2017/skills/geo-prohibited-word-checker) <br>
- [Replacement guide](artifact/references/replacement_guide.md) <br>
- [Paid-mode deployment guide](artifact/references/deploy_guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with comparison tables, shell command examples, JSON detection results, and cleaned text file outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Free mode reports only the first three unique prohibited words; paid mode uses an API key and endpoint to request full detection.] <br>

## Skill Version(s): <br>
1.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
