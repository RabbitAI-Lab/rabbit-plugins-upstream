## Description: <br>
从简历到纯标签矩阵的完整流程。接受简历文本/文件，使用 LLM 提取原子标签并扩展近义词，创建飞书多维表格，批量录入候选人，清理空白行列，并输出可搜索的人才标签库。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tuobadaidai](https://clawhub.ai/user/tuobadaidai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
HR, recruiting, and talent operations users can use this skill to turn resume text or files into normalized candidate tag records for search, matching, and Feishu Bitable entry. Developers and operators can also use its helper script to prepare an LLM extraction prompt and JSON metadata for the workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Resume inputs can contain sensitive personal data, and the helper script may extract phone and email details. <br>
Mitigation: Use the skill only with permission to process the resumes, review generated prompt and JSON outputs before sharing or storing them, and modify or avoid the helper script output when contact details are not needed. <br>
Risk: Resume content may be prepared for LLM processing and Feishu storage. <br>
Mitigation: Confirm the chosen LLM and Feishu workspace are approved for the data being processed, and avoid sending or storing resumes that exceed the user's authorization or retention requirements. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tuobadaidai/skills/resume-to-tags) <br>
- [references/synonyms.json](references/synonyms.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown workflow guidance with shell command examples and JSON extraction structures; the helper script emits JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The helper script prepares a prompt from up to 5000 characters of resume text and may include extracted phone and email fields in its JSON output.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
