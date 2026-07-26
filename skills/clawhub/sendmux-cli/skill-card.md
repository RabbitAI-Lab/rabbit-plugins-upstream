## Description: <br>
Use the Sendmux CLI for terminal-driven Management, Mailbox, and Sending workflows with JSON output and scoped credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sendmux.ai](https://clawhub.ai/user/sendmux.ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate Sendmux from the terminal for account management, mailbox, and sending workflows. It is intended for exact CLI mechanics with JSON output and scoped credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents to read mailboxes, send email, and manage account resources when credentials allow it. <br>
Mitigation: Install only for agents intended to operate Sendmux from a terminal, prefer scoped agent or mailbox tokens over root keys, keep destructive or sending actions user-confirmed, and avoid storing broad credentials in shared environments. <br>


## Reference(s): <br>
- [Sendmux CLI skill on ClawHub](https://clawhub.ai/sendmux.ai/skills/sendmux-cli) <br>
- [Sendmux skills homepage](https://github.com/Sendmux/skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON-oriented CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prefers --json for agent-readable output and relies on Sendmux environment variables or CLI profiles for credentials.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter says 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
