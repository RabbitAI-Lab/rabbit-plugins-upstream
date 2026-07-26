## Description: <br>
简历全流程助手：传一份旧简历拆解为永久素材库，后续任意 JD 一键匹配生成定制简历 + 干净 PDF + 模拟面试。不是每次重写，是从素材库中挑最优组合投递岗位。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[antiwork-lab](https://clawhub.ai/user/antiwork-lab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Job seekers and career-support agents use this skill to turn an existing resume into a reusable material library, analyze job descriptions, generate tailored resume content and PDF files, run mock interviews, and track applications. It is aimed at Chinese-language resume and job-search workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may store sensitive resume details, job descriptions, application history, and interview notes in persistent documents, including Feishu. <br>
Mitigation: Confirm with the user before creating or updating external documents, and establish how stored records can be viewed, edited, and deleted. <br>
Risk: JD links and fetched content can expose sensitive or untrusted destinations. <br>
Mitigation: Avoid sending sensitive links unless the destination and fetch behavior are trusted; ask the user to paste text or provide screenshots when link extraction is uncertain. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/antiwork-lab/skills/offer-assistant) <br>
- [Resume parsing methodology](artifact/references/resume-parsing.md) <br>
- [JD analysis and matching methodology](artifact/references/jd-methodology.md) <br>
- [Resume writing methodology](artifact/references/resume-methodology.md) <br>
- [Mock interview methodology](artifact/references/mock-interview.md) <br>
- [Application tracking methodology](artifact/references/tracking.md) <br>
- [PDF generation methodology](artifact/references/pdf-generation.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, structured text reports, HTML resume content, PDF files, and shell or Node.js command invocations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Node.js, Chrome/Chromium, Tesseract OCR, optional CHROME_PATH and TESSERACT_LANG settings, and the ws package for PDF generation workflows.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
