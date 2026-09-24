## Description:

Manage Claude Code instances living inside tmux sessions. Users usually create separate tmux sessions for separate projects. Use this skill when you need to read the latest Claude Code response in a particular tmux session / project, send it a prompt and get the response, or run /compact directly via tmux (no extra scripts required).

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulrahul](https://clawhub.ai/user/paulrahul)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to inspect and control Claude Code sessions running inside tmux, including locating the Claude pane, reading the latest exchange, sending prompts, triggering /compact, and dumping scrollback for debugging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands may be sent to the wrong tmux session or pane.

Mitigation: Verify the exact session, window, and pane target before sending prompts or /compact.

Risk: Shell command templates may execute unintended local commands when populated with untrusted text.

Mitigation: Use the skill only with tmux sessions you control and avoid passing untrusted prompt text through shell command templates.

Risk: Captured tmux scrollback may contain sensitive terminal history.

Mitigation: Treat captured pane output as sensitive and share only the lines needed for the task.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline tmux shell commands and human-facing status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No helper scripts or extra dependencies; output may include captured terminal scrollback.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
