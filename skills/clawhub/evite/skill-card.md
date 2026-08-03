## Description: <br>
This skill enables an agent to help with Evite events and invitations, including viewing events, guest lists, RSVP information, messages, and templates, plus confirm-gated RSVP, guest, message, invitation, and event actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to Evite so it can inspect event details, summarize invitations and guests, manage RSVPs, prepare guest messaging, and perform host-side event updates when explicitly confirmed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose private Evite event, guest, RSVP, and message data through authenticated access. <br>
Mitigation: Install only when the user accepts that access level, scope account credentials carefully, and avoid sharing sensitive event data outside the intended conversation. <br>
Risk: Persistent authentication through raw cookies or browser-session bootstrap can increase account access risk. <br>
Mitigation: Prefer EVITE_EMAIL and EVITE_PASSWORD configuration over copied raw cookies, and set EVITE_DISABLE_FETCHPROXY=1 when browser-cookie bootstrap is not needed. <br>
Risk: Write-capable tools can send messages, edit guests, send invitations, or change events. <br>
Mitigation: Require explicit user confirmation before any write action and use dry-run previews where available before making network changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite) <br>
- [Evite](https://www.evite.com) <br>
- [npm package: evite-mcp](https://www.npmjs.com/package/evite-mcp) <br>
- [Source: chrischall/evite-mcp](https://github.com/chrischall/evite-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe or propose authenticated Evite actions; write actions should require explicit confirmation.] <br>

## Skill Version(s): <br>
0.5.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
