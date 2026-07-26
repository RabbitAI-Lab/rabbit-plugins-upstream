## Description: <br>
Slk lets agents use a macOS Slack CLI to read, search, draft, send, react to, and manage Slack channels, DMs, threads, saved items, and unread activity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[therohitdas](https://clawhub.ai/user/therohitdas) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an agent interact with their personal Slack workspace from the terminal. It is suited for checking unreads, reading channels and DMs, searching workspace history, preparing drafts for review, and sending or reacting to messages when the user intends that action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reuses and caches the logged-in desktop Slack session, allowing an agent to access DMs, private channels, and post as the user. <br>
Mitigation: Install only when that access is intended, use it on a trusted personal macOS machine, and clear ~/.local/slk/token-cache.json when cached Slack access should be removed. <br>
Risk: Granting persistent Keychain access can let processes running as the user trigger Slack credential extraction without a fresh prompt. <br>
Mitigation: Prefer one-time Keychain Allow over Always Allow unless persistent access is explicitly acceptable. <br>
Risk: Agent-driven Slack sends or reactions can affect real workspace conversations as the logged-in user. <br>
Mitigation: Use draft commands for sensitive replies when human review is desired, and reserve direct send/react commands for clearly authorized actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/therohitdas/skills/slack-personal) <br>
- [slkcli npm package](https://www.npmjs.com/package/slkcli) <br>
- [Slack Web API](https://slack.com/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and Slack CLI text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read Slack content and create messages, reactions, or drafts through the logged-in user's Slack session.] <br>

## Skill Version(s): <br>
0.1.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
