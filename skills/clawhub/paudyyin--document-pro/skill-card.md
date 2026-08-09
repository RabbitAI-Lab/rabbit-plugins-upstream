## Description: <br>
Extract key information from PDF, DOCX, PPT and other documents <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use Document Pro to have an agent extract, summarize, and convert information from PDFs, Word documents, PowerPoint decks, Excel workbooks, text, and Markdown files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes local documents that may contain sensitive content. <br>
Mitigation: Use it only with documents the agent is permitted to inspect, and avoid confidential files unless the environment and model use are approved. <br>
Risk: The skill instructs the agent to update record.md after each task, which may persist details from sensitive documents. <br>
Mitigation: Ask the agent not to write record.md for sensitive work, or change the skill to require explicit permission before logging. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/document-pro) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with document summaries, bullet points, tables, and code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include extracted document metadata, 3-5 key points, suggested next actions, and dependency troubleshooting.] <br>

## Skill Version(s): <br>
1.1.0 (source: SKILL.md frontmatter and server release metadata; package.json and _meta.json report 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
