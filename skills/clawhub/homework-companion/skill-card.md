## Description: <br>
AI 伴学助手帮助 K12 孩子通过拍照、截图、语音或文本提交作业问题，进行题目识别、苏格拉底式引导讲解、错题本整理和家长报告生成。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wukongmazi](https://clawhub.ai/user/wukongmazi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, especially parents and learners, use this skill to guide K12 homework practice without simply giving answers. It can recognize homework from images or voice, support step-by-step tutoring, and produce review artifacts such as wrong-question notebooks and parent-facing learning reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Children's homework images, voices, text, and learning summaries may be sent to Tencent Cloud services. <br>
Mitigation: Use the skill only with parent or authorized-adult approval, minimize submitted content, and avoid including names, schools, addresses, or other identifiers. <br>
Risk: Wrong-question notebooks, Excel files, and parent reports may persist sensitive learning records locally. <br>
Mitigation: Restrict access to generated files, delete records that are no longer needed, and avoid storing unnecessary personal details. <br>
Risk: Optional sharing through enterprise messaging or Tencent Docs could expose child learning records beyond the intended audience. <br>
Mitigation: Review recipients, permissions, and document-sharing settings before enabling any report delivery or shared-document workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wukongmazi/skills/homework-companion) <br>
- [学科引导式讲解 Playbook](references/subject-playbooks.md) <br>
- [儿童内容安全规范](references/safety-rules.md) <br>
- [错题本规范与 Excel 生成模板](references/wrong-question-notebook.md) <br>
- [家长报告模板](references/parent-report.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and text guidance with optional shell commands, Excel files, reports, and generated MP3 audio paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call Tencent Cloud OCR, ASR, and TTS through local scripts when credentials are configured.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
