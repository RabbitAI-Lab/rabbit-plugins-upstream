## Description:

Gives Claude Code persistent memory across sessions by recalling relevant stored facts and automatically capturing new ones.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neboy72](https://clawhub.ai/user/neboy72)

### License/Terms of Use:

MIT-0

## Use Case:

Claude Code users can retain useful conversation facts across sessions and recall or correct them when earlier context is needed. Memories can also be shared with other agents using the same collection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conversation facts may be retained automatically, including sensitive information.

Mitigation: Avoid sessions with secrets, regulated data, or client material unless retention is approved; review and delete stored facts or disable automatic capture.

Risk: A shared collection can expose memories to other connected agents or projects.

Mitigation: Use separate collections for projects or agents that should not share context.

Risk: Choosing a cloud embedding provider sends memory text to that provider.

Mitigation: Keep the default local embedding provider if memory text must remain on the machine.

## Reference(s):

- [Nexus Memory on ClawHub](https://clawhub.ai/neboy72/skills/nexus-memory)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Relevant memories can appear in agent context; users can store, recall, update, and delete memories.]

## Skill Version(s):

0.1.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
