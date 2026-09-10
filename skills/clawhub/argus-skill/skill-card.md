## Description:

Preserve durable context from conversations and completed work by routing commitments, evidence, decisions, preferences, and project state to their canonical Git-backed records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers and repository-aware agent users use Argus to preserve decisions, commitments, evidence, preferences, and project state in the correct Git-backed Archivum record after meaningful work milestones.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Argus can write lasting private records when an agent applies a checkpoint.

Mitigation: Require the agent to show the exact records it will change before writing, preserve only durable deltas, and keep secrets only in authorized stores.

Risk: Backlink validation can read outside an archive when used with a crafted registry.

Mitigation: Do not run backlink validation against registries from untrusted repositories until the path-containment issue is fixed.

Risk: A checkpoint can be mistaken for authority to publish, send, spend, or create new archives.

Mitigation: Keep those actions behind separate user or repository authorization and use the configured commitment or budget authority where applicable.

Risk: Unsupported or tentative conversation content could be promoted into durable knowledge.

Mitigation: Record evidence, uncertainty, and whether an item was proposed or completed; leave unselected brainstorming and duplicated summaries out of the checkpoint.

## Reference(s):

- [Argus Skill Page](https://clawhub.ai/antreasantoniou/skills/argus-skill)
- [README](README.md)
- [Routing Durable Context](references/routing.md)
- [Home-Anchor and Backlink Contract](references/backlink-contract.md)
- [Recommended Agent Checkpoint](references/checkpoint-prompt.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell command snippets and file-change reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead the agent to make authorized edits to Git-backed Archivum records; bundled helper scripts are read-only.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
