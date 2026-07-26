## Description: <br>
投标技术方案编写。当用户输入"投标方案##"或"写投标方案"时触发。提供结构化协作式投标方案编写流程：需求分析→大纲推荐→逐章生成→Word输出。适用于安全服务、产品交付、等保测评、综合安全等投标场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[elle-yu](https://clawhub.ai/user/elle-yu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and proposal teams use this skill to convert tender technical requirements into scoring-aligned bid proposal outlines, chapter drafts, and Word-ready deliverables for security-service, product-delivery, equal-protection assessment, and integrated security bids. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes tender documents and optional material-library files that may contain confidential or unrelated information. <br>
Mitigation: Confirm before processing .docx uploads and avoid importing unrelated, confidential, or third-party material into the material library. <br>
Risk: Generated proposal language may describe penetration testing, incident response, or operational security work without enough authorization or scope context. <br>
Mitigation: Review generated security-testing and incident-response sections so they require written authorization, approved scope, change control, rollback planning, and business-impact review. <br>
Risk: Proposal drafts can contain inaccurate commitments, inflated metrics, or reused template claims that do not fit the tender. <br>
Mitigation: Review generated chapters against the tender requirements, scoring criteria, and approved company capabilities before submission. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/elle-yu/skills/bid-proposal) <br>
- [Scene mapping](artifact/references/scene-mapping.json) <br>
- [Chapter templates](artifact/references/chapter-templates.md) <br>
- [Material library guide](artifact/material-lib/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown drafts, JSON analysis and state, generated writing prompts, and .docx proposal files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses optional local material-library references and python-docx for Word document output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
