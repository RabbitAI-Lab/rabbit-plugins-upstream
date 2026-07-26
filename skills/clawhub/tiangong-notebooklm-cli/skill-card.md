## Description: <br>
NotebookLM CLI wrapper via `node {baseDir}/scripts/notebooklm.mjs`. Use for auth, notebooks, chat, sources, notes, sharing, research, and artifact generation/download. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fadeloo](https://clawhub.ai/user/fadeloo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to operate NotebookLM through a local CLI for notebook management, source handling, chat, notes, sharing, research, and generated artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can act on the user's authenticated NotebookLM account, including deleting notebooks, sources, artifacts, or notes and changing sharing settings. <br>
Mitigation: Require explicit confirmation before destructive, sharing, export, language-change, or `--yes` commands, and verify target notebook, source, artifact, and collaborator identifiers before execution. <br>
Risk: The wrapper delegates to the local `notebooklm` executable, so account actions depend on the installed CLI and active session. <br>
Mitigation: Use only a trusted `notebooklm` CLI, check authentication status before account operations, prefer `--json` for machine-readable results, and set bounded execution timeouts for long-running commands. <br>


## Reference(s): <br>
- [NotebookLM CLI command catalog](references/cli-commands.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands require Node.js, a trusted notebooklm CLI on PATH, and an authenticated NotebookLM session.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
