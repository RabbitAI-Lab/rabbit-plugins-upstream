## Description: <br>
知识学习管理帮助用户记录、分类、查询和复习知识点，并管理专项备考计划、每日学习建议、晚间回顾和快问快答。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[elle-yu](https://clawhub.ai/user/elle-yu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External learners and exam-prep users use this skill to maintain a local learning knowledge base, receive scheduled study and review prompts, and track special study projects with outlines and deadlines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad automatic triggers may route ordinary messages into the learning-review workflow. <br>
Mitigation: Review trigger phrases before installation and keep normal chat messages free of those phrases when you do not want the skill to act. <br>
Risk: The skill keeps persistent local learning records and review history. <br>
Mitigation: Avoid recording credentials, private unrelated notes, or regulated data, and inspect or delete the local JSON records when retention is no longer needed. <br>
Risk: Image-based knowledge entry may download and process screenshots or notes with local OCR tools. <br>
Mitigation: Send only images intended for study capture, review OCR results before confirming storage, and avoid screenshots containing secrets or unrelated personal information. <br>
Risk: Scheduled or recovered review prompts may be sent without a fresh user request. <br>
Mitigation: Confirm the desired schedule and notification behavior before enabling routine morning, quiz, or evening review flows. <br>
Risk: External motivational content fetching can introduce network calls outside the core learning workflow. <br>
Mitigation: Use the built-in fallback greetings or disable external fetching where network behavior is not acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/elle-yu/skills/knowledge-review) <br>
- [分类规则](artifact/references/classify-rules.md) <br>
- [专项管理规范](artifact/references/special-project-spec.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-style conversational responses with JSON file updates and occasional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores learning records, review statistics, and project state in local JSON files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
