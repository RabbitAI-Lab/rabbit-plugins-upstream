## Description: <br>
Use NotebookLM CLI to manage notebooks, add text or URL sources, ask questions, summarize content, and generate learning materials such as slides, quizzes, and flashcards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chunkitcn](https://clawhub.ai/user/chunkitcn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, students, and knowledge workers use this skill to operate the NotebookLM CLI from an agent workflow: creating notebooks, adding sources, asking questions, summarizing notebooks, and generating study or presentation artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Notebook sources, pasted text, URLs, and questions may be sent to a cloud service. <br>
Mitigation: Avoid uploading confidential or regulated material unless authorized for the NotebookLM account and service. <br>
Risk: The skill uses an authenticated third-party CLI and can download generated files. <br>
Mitigation: Review the NotebookLM CLI before authentication and confirm where downloaded artifacts are saved. <br>


## Reference(s): <br>
- [NotebookLM CLI Quick Reference](references/quick-ref.md) <br>
- [NotebookLM CLI repository](https://github.com/tiangong-ai/notebooklm-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include JSON-oriented CLI flags and commands for downloading NotebookLM-generated artifacts.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
