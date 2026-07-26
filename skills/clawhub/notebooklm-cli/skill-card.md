## Description: <br>
Comprehensive CLI for Google NotebookLM including notebooks, sources, audio podcasts, reports, quizzes, flashcards, mind maps, slides, infographics, videos, and data tables. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oconnell-carl](https://clawhub.ai/user/oconnell-carl) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to manage Google NotebookLM notebooks, sources, authentication profiles, generated artifacts, research imports, and chat workflows from an agent-assisted command-line workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The login flow uses authenticated Chrome session cookies for NotebookLM, and the available evidence does not provide enough detail about credential storage or deletion. <br>
Mitigation: Use an isolated Chrome profile or test Google account, verify where credentials are stored, and confirm how to delete them before running `nlm login`. <br>


## Reference(s): <br>
- [Command Reference](references/commands.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Workflows](references/workflows.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/oconnell-carl/skills/notebooklm-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown, Text] <br>
**Output Format:** [Markdown with inline shell commands and command-output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce NotebookLM-generated artifacts such as audio overviews, reports, quizzes, flashcards, mind maps, slides, infographics, videos, and data tables.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
