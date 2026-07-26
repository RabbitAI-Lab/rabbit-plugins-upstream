## Description: <br>
Let an OpenClaw agent read, search, count, sync, triage, file, delete, thread, and reply from one Sendmux mailbox efficiently. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sendmux.ai](https://clawhub.ai/user/sendmux.ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent operate within a single Sendmux mailbox: search and read selected messages, manage threads and folders, sync mailbox changes, triage messages, and send replies when the credential allows it. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access mailbox contents and sync state when provided Sendmux credentials. <br>
Mitigation: Install it only for intended mailbox workflows and use scoped mailbox or agent tokens rather than a root key. <br>
Risk: Send, delete, or update actions can change mailbox state or transmit email. <br>
Mitigation: Require explicit user confirmation before destructive or send-capable operations, and re-read state before mutations when needed. <br>
Risk: Using credentials with broader mailbox access can expose or affect more messages than intended. <br>
Mitigation: Use mailbox-scoped credentials when possible and include a mailbox_id when credentials grant access to more than one mailbox. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-mailbox-agent) <br>
- [Sendmux skills homepage](https://github.com/Sendmux/skills) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions] <br>
**Output Format:** [Markdown with bash, TypeScript, JSON, and text examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Sendmux credentials for live mailbox operations; examples favor scoped mailbox or agent tokens.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
