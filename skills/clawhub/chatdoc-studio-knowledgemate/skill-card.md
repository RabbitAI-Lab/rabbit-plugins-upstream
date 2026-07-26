## Description: <br>
ChatDOC Studio--KnowledgeMate uploads PDF, DOC, and DOCX files to ChatDOC Studio through PDRouter, creates knowledge bases from successful uploads, and supports document retrieval and reading commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paodingai](https://clawhub.ai/user/paodingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create ChatDOC Studio knowledge bases from local PDF, DOC, or DOCX files and then query, search, inspect, or read documents in those knowledge bases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected PDF, DOC, and DOCX files are uploaded to ChatDOC Studio through PDRouter and may contain sensitive or regulated content. <br>
Mitigation: Upload only files the user intends to send to ChatDOC Studio and confirm the user is authorized to process those documents with the service. <br>
Risk: Recursive directory scans can include more documents than intended before the helper reaches its 300-file limit. <br>
Mitigation: Prefer explicit file paths or narrow directories, review the selected input scope, and keep broad folders below the documented 300 supported-file limit. <br>
Risk: The skill requires a PAODINGAI_API_KEY bearer token for API access. <br>
Mitigation: Keep the token in the environment, avoid printing it in prompts or logs, and rotate it if it is exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paodingai/skills/chatdoc-studio-knowledgemate) <br>
- [PDRouter platform](https://platform.paodingai.com) <br>
- [KnowledgeMate helper script](scripts/knowledge-mate.mjs) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, json, guidance] <br>
**Output Format:** [Markdown or text guidance with shell commands; the helper script prints JSON results and JSON-formatted errors.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and PAODINGAI_API_KEY; uploads supported PDF/DOC/DOCX files with fixed concurrency 5 and a 300-file limit.] <br>

## Skill Version(s): <br>
1.3.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
