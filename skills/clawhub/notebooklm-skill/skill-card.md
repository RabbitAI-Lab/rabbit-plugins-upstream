## Description: <br>
Use this skill to query Google NotebookLM notebooks directly from Claude Code for source-grounded, citation-backed answers from Gemini. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guccidgi](https://clawhub.ai/user/guccidgi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers using local Claude Code installations use this skill to authenticate with Google NotebookLM, manage a saved notebook library, query notebooks, and synthesize source-grounded answers from uploaded documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automates a logged-in Google NotebookLM browser session and stores reusable session data locally. <br>
Mitigation: Use a dedicated Google account when possible, protect or delete stored browser state after use, and avoid notebooks that contain confidential material. <br>
Risk: Notebook sharing settings and uploaded source material may expose sensitive information outside the intended environment. <br>
Mitigation: Use non-sensitive notebooks for this workflow and avoid public or anyone-with-link notebook access for confidential content. <br>
Risk: Browser automation may conflict with Google service limits or enterprise data-handling requirements. <br>
Mitigation: Confirm that the workflow fits applicable service limits and organizational policies before relying on it for regulated or enterprise use. <br>


## Reference(s): <br>
- [NotebookLM Skill API Reference](references/api_reference.md) <br>
- [NotebookLM Skill Usage Patterns](references/usage_patterns.md) <br>
- [NotebookLM Skill Troubleshooting](references/troubleshooting.md) <br>
- [Authentication Architecture](AUTHENTICATION.md) <br>
- [Google NotebookLM](https://notebooklm.google.com) <br>
- [Claude Code](https://github.com/anthropics/claude-code) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and source-grounded answer text from NotebookLM] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on a local Claude Code environment, a Google-authenticated browser session, and the user's NotebookLM notebooks.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
