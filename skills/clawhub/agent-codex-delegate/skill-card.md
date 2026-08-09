## Description: <br>
Delegates coding, repository analysis, file edits, test runs, and code review to a locally authenticated Codex CLI without embedding an OpenAI API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and trusted local operators use CodexDelegate to delegate repository analysis, code review, test debugging, and code-editing tasks to a locally authenticated Codex CLI while keeping API keys out of prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Delegated Codex runs can read or modify local repository files depending on the selected sandbox. <br>
Mitigation: Start with read-only, use workspace-write only for intended edits, and reserve danger-full-access for isolated environments after explicit approval. <br>
Risk: Sensitive data could be exposed if secrets, credentials, private keys, or production data are included in delegated tasks. <br>
Mitigation: Avoid sending secrets or production data unless that exact data flow is intentional and approved. <br>
Risk: Codex output may contain incorrect guidance or edits that do not match the repository's intent. <br>
Mitigation: Treat Codex output as another agent's report; review important claims locally and inspect diffs and tests before accepting changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/agent-codex-delegate) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text final responses, with optional JSONL event logs and Markdown output files when configured.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a locally installed and authenticated codex binary.] <br>

## Skill Version(s): <br>
0.1.3 (source: frontmatter, clawhub metadata, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
