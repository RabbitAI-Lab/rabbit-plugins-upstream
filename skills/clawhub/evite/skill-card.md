## Description:

This skill should be used when the user asks about Evite events or invitations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to let an agent inspect and manage Evite invitations and hosted events, including guest lists, RSVP summaries, messages, and event updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Evite credentials or reusable sessions to access event and invitation data.

Mitigation: Install only for accounts where this access is acceptable, keep credentials scoped to Evite use, and remove stored sessions when access is no longer needed.

Risk: Broad triggering could route unrelated event or invitation requests into Evite account actions.

Mitigation: Use explicit Evite-only prompts and review the agent's selected action before allowing account changes.

Risk: Confirm-gated write tools can RSVP, message guests, edit events, send invitations, cancel events, or otherwise make high-impact changes.

Mitigation: Review dry-run previews carefully and use confirm:true only after the requested change is correct.

Risk: Fetchproxy bootstrap can reuse a signed-in browser tab unless disabled.

Mitigation: Set EVITE_DISABLE_FETCHPROXY=1 when browser-session bootstrap is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite)
- [Publisher profile](https://clawhub.ai/user/chrischall)
- [npm package](https://www.npmjs.com/package/evite-mcp)
- [Evite](https://www.evite.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run previews for confirm-gated Evite write actions.]

## Skill Version(s):

0.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
