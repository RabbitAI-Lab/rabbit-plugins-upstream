## Description: <br>
Book To Learn Check turns books in PDF, DOCX, HTML, EPUB, TXT, or RTF formats into daily learning cards with optional bilingual terminology review, translation, and delivery through IMA or Feishu. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sedey999](https://clawhub.ai/user/sedey999) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, educators, and self-directed learners use this skill to decompose books into structured knowledge points, generate study-card artifacts, and run daily push workflows. It is suited to recurring book study, bilingual review, and prompt-driven learning variants built from the same extracted book data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installation guidance includes optional sudo pip commands and an optional download/copy flow for the IMA skill. <br>
Mitigation: Review commands before execution, install dependencies in a controlled environment, and only install the IMA skill from a trusted source. <br>
Risk: Generated book content, cards, images, and failure messages can be sent to configured IMA, Feishu, webhook, or push-service destinations. <br>
Mitigation: Use only trusted destinations and avoid processing confidential books unless the selected push channel is approved for that content. <br>
Risk: Optional push workflows depend on local IMA, Feishu, or webhook credentials. <br>
Mitigation: Configure credentials only for trusted accounts, store them locally as documented, and rotate or remove them if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sedey999/skills/book-to-learn) <br>
- [IMA agent interface](https://ima.qq.com/agent-interface) <br>
- [Feishu Open Platform](https://open.feishu.cn/app) <br>
- [Open Music Theory example source](https://viva.pressbooks.pub/openmusictheory) <br>
- [book-to-skill reference project](https://github.com/virgiliojr94/book-to-skill) <br>
- [react-paper-memo design reference](https://github.com/JustinChia/react-paper-memo) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration, shell commands, and generated PDF, HTML, PNG, or Feishu card artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Progress is recorded only after successful delivery; optional push workflows can send generated book content to configured IMA, Feishu, or webhook destinations.] <br>

## Skill Version(s): <br>
1.3.0 (source: SKILL.md frontmatter and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
