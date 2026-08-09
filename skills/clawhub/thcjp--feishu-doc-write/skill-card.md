## Description: <br>
Converts Markdown content into Feishu/Lark document block structures and provides guidance for writing those blocks through the Feishu document API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to convert Markdown or document content into Feishu/Lark block JSON and to plan document-writing workflows. It is intended for ordinary document processing and explicitly excludes encrypted-file cracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for broad local read, write, and command execution authority. <br>
Mitigation: Run it in a restricted workspace, review proposed commands before execution, and disable command execution unless it is necessary for the document-writing task. <br>
Risk: Document content, API credentials, or local files could expose sensitive information during Feishu/Lark API workflows. <br>
Mitigation: Provide only the minimum necessary content, store credentials in environment variables, redact logs, and avoid passing sensitive local files unless explicitly required. <br>
Risk: The artifact includes unclear capabilities beyond Feishu/Lark document writing. <br>
Mitigation: Constrain use to Markdown-to-block conversion and Feishu/Lark document-writing guidance; review outputs before applying changes to external documents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/feishu-doc-write) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command snippets; agent results may be returned as JSON status objects.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require Feishu/Lark API credentials and user-provided document content.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
