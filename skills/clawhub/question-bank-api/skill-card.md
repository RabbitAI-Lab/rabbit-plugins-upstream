## Description: <br>
Helps users with a purchased API key retrieve K12 questions, papers, answer explanations, and Word exports from the Xuekubao question-bank API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[e953962json](https://clawhub.ai/user/e953962json) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External education users and developers use this skill to call a third-party K12 question-bank API for question retrieval by knowledge point, chapter, paper, or keyword, then optionally fetch answers or export structured question data to Word. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends requests to a third-party question-bank API using a user-supplied API key. <br>
Mitigation: Install only when the user intends to use the Xuekubao API and keep QB_API_KEY protected like a password. <br>
Risk: Changing QB_API_BASE can redirect API requests to a non-official gateway. <br>
Mitigation: Keep QB_API_BASE set to the official HTTPS provider URL unless the alternate gateway is explicitly trusted. <br>
Risk: Word export can write a local file path chosen by the user. <br>
Mitigation: Choose output filenames carefully to avoid overwriting existing files. <br>


## Reference(s): <br>
- [API endpoint and field reference](artifact/references/api_docs.md) <br>
- [Xuekubao API portal](https://api.xuekubao.com) <br>
- [ClawHub skill release](https://clawhub.ai/e953962json/skills/question-bank-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API responses when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save Word docx files when the API returns an export.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
