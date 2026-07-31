## Description: <br>
天台宗教理研究与结构化报告生成。支持简单问答和深度研究两种模式。遵循两步工作流（检索→审核标注），所有论断标注CBETA出处。当用户提问天台宗教义、判教、观心、止观、祖师著作等相关问题时使用。触发词：天台宗、天台、教观、止观、法华、蕅益、智者大师、四教、一念三千、三谛圆融、六即、四种三昧、法华三昧等。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gouchunlei2-png](https://clawhub.ai/user/gouchunlei2-png) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and researchers use this skill to answer Tiantai Buddhism questions and produce structured research reports with CBETA-cited claims. It supports quick definitions as well as deeper comparative analysis across doctrine, practice systems, and patriarchal texts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Document actions may expose or modify local DOC/DOCX files or online Tencent Docs if delegated without clear user intent. <br>
Mitigation: Keep document reading, creation, and editing explicitly user-directed and review proposed document actions before execution. <br>
Risk: Search terms sent to external CBETA endpoints or connected knowledge tools could disclose sensitive private notes. <br>
Mitigation: Avoid sending sensitive private notes as search terms and sanitize queries before using external search endpoints. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gouchunlei2-png/skills/ttyj-sikll) <br>
- [Publisher profile](https://clawhub.ai/user/gouchunlei2-png) <br>
- [CBETA Online](https://cbetaonline.dila.edu.tw/zh/{work_id}_{juan}) <br>
- [CBETA development search API](https://cbdata.dila.edu.tw/dev/search?q=關鍵詞) <br>
- [CBETA stable search API](https://cbdata.dila.edu.tw/stable/search?q=關鍵詞) <br>
- [CBETA alternate search API](https://api.cbetaonline.cn/search?q=關鍵詞) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown research answers and structured reports with citations and reference tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should cite CBETA or knowledge-base sources for claims and state when available materials do not cover a topic.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
