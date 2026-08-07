## Description: <br>
天台研究 helps agents answer Tiantai Buddhist doctrine questions and produce structured research reports grounded in specified knowledge bases with CBETA citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gouchunlei2-png](https://clawhub.ai/user/gouchunlei2-png) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and researchers use this skill to investigate Tiantai Buddhist concepts, patriarch texts, doctrinal comparisons, and practice systems. It supports quick cited answers and deeper structured reports with source tables, CBETA links, and coverage limitations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional online CBETA searches and Tencent Docs editing can send query terms or document content to external services. <br>
Mitigation: Use online lookup or document editing only for non-sensitive research material and only when the user clearly requests it. <br>
Risk: Research answers can be incomplete when the configured knowledge bases do not cover a requested doctrine, text, or passage. <br>
Mitigation: State coverage limitations explicitly and keep claims tied to cited CBETA or knowledge-base sources. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gouchunlei2-png/skills/ttyj-skill) <br>
- [CBETA Online Reader](https://cbetaonline.dila.edu.tw/zh/{work_id}_{juan}) <br>
- [CBETA Development Search API](https://cbdata.dila.edu.tw/dev/search?q=關鍵詞) <br>
- [CBETA Stable Search API](https://cbdata.dila.edu.tw/stable/search?q=關鍵詞) <br>
- [CBETA Backup Search API](https://api.cbetaonline.cn/search?q=關鍵詞) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown answers and structured reports with citations, source tables, and CBETA links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include explicit statements when available materials do not cover part of the question.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
