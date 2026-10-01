## Description:

Provides persistent memory for Claude Code by automatically recalling relevant context and saving conversation-derived facts in Qdrant across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neboy72](https://clawhub.ai/user/neboy72)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Claude Code can recall project context across sessions and save or delete memories through manual tools. Compatible agents can access the same Qdrant collection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic capture may retain sensitive conversation-derived facts without explicit per-turn consent.

Mitigation: Avoid secrets, credentials, regulated data, and sensitive client material unless capture can be disabled and stored memories can be reviewed and deleted.

Risk: A shared memory collection may expose saved facts to other compatible agents and reuse them in later sessions.

Mitigation: Set clear collection boundaries and access controls, and review recalled content before relying on it.

## Reference(s):

- [ClawHub release](https://clawhub.ai/neboy72/skills/nexus-memory)
- [Server-resolved source](https://github.com/Neboy72/nexus-memory/tree/main/plugins/claude-code/skills/nexus-memory)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recalls relevant memories as agent context; saved memories can be shared with compatible agents.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
