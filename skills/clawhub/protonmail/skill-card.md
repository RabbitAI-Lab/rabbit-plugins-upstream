## Description: <br>
Read, search, and scan ProtonMail via IMAP bridge (Proton Bridge or hydroxide). Includes daily digest for important emails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[durchblick-nl](https://clawhub.ai/user/durchblick-nl) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to access ProtonMail through a local IMAP bridge, inspect mailbox state, search messages, read selected emails, and generate a daily digest of important unread mail. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose private mailbox metadata and email contents to the agent through list, search, unread, read, and daily digest operations. <br>
Mitigation: Use it only with a ProtonMail account whose contents you are comfortable exposing to the agent, and avoid reading messages that are outside the intended task. <br>
Risk: Bridge credentials may be stored in environment variables or a local config file. <br>
Mitigation: Protect credential files with restrictive permissions such as 600, avoid committing or sharing config files, and rotate bridge credentials if they may have been exposed. <br>
Risk: A local IMAP bridge can broaden mailbox access if it is reachable beyond the local host or comes from an untrusted build. <br>
Mitigation: Prefer trusted and pinned bridge software and bind bridge ports to 127.0.0.1 only. <br>


## Reference(s): <br>
- [hydroxide IMAP bridge](https://github.com/emersion/hydroxide.git) <br>
- [ClawHub ProtonMail skill page](https://clawhub.ai/durchblick-nl/skills/protonmail) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal text and Markdown digest output, with setup commands and configuration snippets in the skill documentation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a local ProtonMail IMAP bridge; reads credentials from environment variables or a user config file.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
