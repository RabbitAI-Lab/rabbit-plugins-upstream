## Description:

Control tmux sessions/panes for interactive CLIs: list, capture output, send keys, paste text, monitor prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect and control existing interactive tmux sessions, including listing sessions and panes, capturing pane output, sending input, and waiting for prompt text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can type into live tmux panes and includes examples for interrupting, ending input, and killing sessions.

Mitigation: Confirm the exact session, window, and pane target before sending input, and use C-c, C-d, or kill-session only when that action is explicitly intended.

Risk: Pane capture and the wait helper can expose terminal contents, including timeout logs from panes that may contain sensitive text.

Mitigation: Avoid capturing or polling panes that may contain secrets, limit inspected history where practical, and review whether timeout output is acceptable before using the helper.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/tmux)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline bash code blocks and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tmux target identifiers, captured terminal output, command examples, and helper-script usage.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
