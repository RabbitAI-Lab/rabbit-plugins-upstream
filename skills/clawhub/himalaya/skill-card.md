## Description: <br>
Himalaya helps agents manage configured email accounts from the terminal with IMAP, SMTP, Notmuch, or Sendmail backends. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lamelas](https://clawhub.ai/user/lamelas) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to list, read, search, compose, reply to, forward, move, delete, and organize email through a configured Himalaya CLI account. It is useful for terminal-based email workflows that need multi-account support, attachments, structured output, and MML message composition. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access and change mail in configured email accounts. <br>
Mitigation: Install it only when an agent should operate that account, and require explicit approval before sending, reply-all, forwarding, deleting, moving, exporting full messages, or downloading attachments. <br>
Risk: Email credentials may be exposed if stored directly in the Himalaya configuration file. <br>
Mitigation: Prefer app passwords, OAuth, pass, or a system keyring instead of auth.raw, and protect the config file. <br>


## Reference(s): <br>
- [Himalaya ClawHub Skill](https://clawhub.ai/lamelas/skills/himalaya) <br>
- [Himalaya Project Homepage](https://github.com/pimalaya/himalaya) <br>
- [Himalaya Configuration Reference](references/configuration.md) <br>
- [Message Composition with MML](references/message-composition.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and TOML configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured Himalaya CLI output examples such as JSON or plain text.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
