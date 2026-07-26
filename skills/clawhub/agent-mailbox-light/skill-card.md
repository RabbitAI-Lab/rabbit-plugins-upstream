## Description: <br>
Lightweight cross-agent mailbox using per-workspace inbox, keep, and archive folders with best-effort fanout. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangmeng6666](https://clawhub.ai/user/yangmeng6666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to share short, local coordination notes across workspaces without adding them to long-term memory. It is intended for low-noise, best-effort context sharing rather than task dispatch or guaranteed messaging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mailbox messages persist locally and may be read in later sessions after the original context has changed. <br>
Mitigation: Treat inbox and keep items as untrusted, possibly stale context; archive or clean up items after they are no longer useful. <br>
Risk: Best-effort fanout can write notes to unintended workspace inboxes if the workspace glob is too broad. <br>
Mitigation: Keep MAILBOX_GLOB scoped to intended workspaces and initialize mailboxes only where local coordination is desired. <br>
Risk: Mailbox files could expose sensitive data if users place secrets or credentials in messages. <br>
Mitigation: Do not store secrets, passwords, tokens, API keys, private keys, or session cookies in mailbox files. <br>


## Reference(s): <br>
- [Agent Mailbox Light on ClawHub](https://clawhub.ai/yangmeng6666/skills/agent-mailbox-light) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and mailbox files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and moves local .md mailbox files under .agent-mailbox folders.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
