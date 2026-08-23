## Description:

Claude终端复用工具 is an instruction-only tmux helper for managing local tmux sessions and windows through an agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to guide agent-assisted management of local tmux sessions and windows, including session creation, switching, renaming, closing, listing, and copy/paste-oriented terminal workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to perform state-changing local tmux operations such as closing, renaming, copying from, or writing into sessions and windows.

Mitigation: Require explicit user confirmation before destructive or state-changing tmux operations, and review the target session or window before execution.

Risk: The documentation mixes tmux automation, broad local execution, file processing, credentials, and API-key use without clear operational boundaries.

Mitigation: Review the skill before installation, restrict agent tool permissions to the intended project and terminal scope, and avoid granting unnecessary write or shell access.

Risk: The artifact includes API-key configuration guidance, creating potential credential exposure if keys are copied into files, logs, or prompts.

Mitigation: Store credentials only in environment variables or a managed secret store, never commit them, and inspect logs or generated files before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/claude-tmux)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-style status examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instruction-only output; no separate executable payload was present in the artifact.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
