## Description: <br>
Delegates coding, repository analysis, file edits, test runs, and code review to the local Codex CLI using existing ChatGPT/Codex CLI authentication instead of embedded API keys. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to delegate coding, repository analysis, debugging, refactoring, file-editing, and code-review tasks to a locally authenticated Codex CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can invoke an already-authenticated local Codex CLI session. <br>
Mitigation: Install only in trusted local operator setups, avoid public or untrusted chat channels, and do not pass secrets or production data unless that exact data flow is explicitly approved. <br>
Risk: Delegated tasks may read or modify repository files depending on the selected sandbox. <br>
Mitigation: Use read-only for analysis and review, workspace-write only when edits are intended, and reserve danger-full-access for isolated environments with explicit approval. <br>
Risk: Delegated agent output can contain incorrect claims or unsuitable code changes. <br>
Mitigation: Treat Codex output as another agent report, verify important claims locally, and inspect relevant diffs before reporting edited files as complete. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jlacroix82/skills/agent-codex-delegate) <br>
- [README](artifact/README.md) <br>
- [Skill Definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text final responses, with optional JSONL event logs and output files when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local codex binary on PATH and an already-authenticated Codex CLI session.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release evidence and clawhub.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
