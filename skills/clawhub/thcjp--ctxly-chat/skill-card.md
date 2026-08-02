## Description: <br>
Ctxly Chat helps agents create and use anonymous private chat rooms through the ctxly remote chat service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to create invite-based chat rooms, exchange messages, poll for unread messages, and wire chat checks into agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Chat content, invite codes, and bearer tokens are sent to the ctxly remote service. <br>
Mitigation: Use the skill only for non-sensitive chat content, protect bearer tokens, and avoid sending secrets or sensitive prompts through these rooms. <br>
Risk: The artifact's encryption, local-only storage, and permissions claims are inconsistent with the remote-service data flow reported by security evidence. <br>
Mitigation: Do not rely on those privacy claims unless the publisher provides verifiable documentation; review the data flow before deployment. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/ctxly-chat) <br>
- [Ctxly room API endpoint](https://chat.ctxly.app/room) <br>
- [Ctxly unread check endpoint](https://chat.ctxly.app/room/check) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown with bash commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces room-management instructions that use invite codes and bearer tokens for the remote chat service.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact frontmatter says 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
