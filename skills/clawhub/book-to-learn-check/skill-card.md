## Description: <br>
Book To Learn Check helps an agent turn books in common document formats into daily learning cards, with bilingual handling for English and Chinese books and delivery through PDF, IMA, or Feishu workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sedey999](https://clawhub.ai/user/sedey999) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to break a book into reusable knowledge-point data, generate daily study cards, and push those cards into a knowledge base or messaging workflow. It is suited for self-study, team learning, and configurable study variants such as bilingual cards, review prompts, or visual learning outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated study PDFs, card images, or Feishu card content may be uploaded to external services selected by the user. <br>
Mitigation: Use the skill only with books and notes that are acceptable for the chosen IMA or Feishu workflow, and review upload destinations before enabling delivery. <br>
Risk: Feishu image mode can send embedded images to catbox.moe for URL hosting. <br>
Mitigation: Avoid Feishu image mode for private or sensitive images, or choose a PDF or Feishu card workflow that does not require external image hosting. <br>
Risk: Dependency installation commands and local credential setup affect the user's runtime environment. <br>
Mitigation: Review package installation commands, configure IMA and webhook credentials yourself, and keep credentials out of shared skill artifacts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sedey999/skills/book-to-learn-check) <br>
- [IMA agent interface](https://ima.qq.com/agent-interface) <br>
- [Open Music Theory example source](https://viva.pressbooks.pub/openmusictheory) <br>
- [book-to-skill reference project](https://github.com/virgiliojr94/book-to-skill) <br>
- [react-paper-memo design reference](https://github.com/JustinChia/react-paper-memo) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration, generated study-card files, PDFs, images, and status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local book data, card indexes, PDF or image study cards, optional Feishu payloads, and progress updates only after successful delivery.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
