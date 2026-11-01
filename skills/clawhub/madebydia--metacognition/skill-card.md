## Description:

A self-reflection engine for AI agents that extracts patterns from session transcripts into a weighted insight graph with Hebbian learning and time decay, then compiles a token-budgeted lens of active self-knowledge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[madebydia](https://clawhub.ai/user/madebydia)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Metacognition to capture recurring lessons from session transcripts or notes, reinforce and decay insights over time, and compile a compact memory lens for future agent guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Memory-derived text may be sent to an embeddings endpoint if embeddings are enabled.

Mitigation: Fix or disable embeddings unless the configured endpoint is strictly loopback and approved for the workspace data.

Risk: The skill creates persistent agent guidance from session transcripts or notes, which can preserve sensitive or misleading content.

Mitigation: Review generated memory entries and the compiled lens before loading them into an agent.

Risk: Scheduled extraction can process transcripts or notes that contain quoted instructions or sensitive material.

Mitigation: Avoid cron integration on untrusted or sensitive transcripts, and run extraction only on reviewed inputs.

Risk: Security claims in the artifact metadata conflict with the authoritative security summary.

Mitigation: Audit the implementation and metadata before relying on no-network, no-subprocess, or localhost-only claims.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/madebydia/skills/metacognition)
- [Project Homepage](https://github.com/madebydia/metacognition)
- [OpenClaw](https://openclaw.app)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-backed memory files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a token-budgeted metacognition lens and persists an insight graph in memory/metacognition.json.]

## Skill Version(s):

1.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
