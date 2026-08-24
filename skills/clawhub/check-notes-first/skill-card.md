## Description:

For novel, fiddly, or infrastructure-sensitive work, search prior notes and solved cases for a structurally similar problem. Reuse the method as a hypothesis, verify it against current state, test the real outcome falsifiably, and record only the reusable delta.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pinguy](https://clawhub.ai/user/pinguy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical agents use this skill before unfamiliar, fiddly, or infrastructure-sensitive work to retrieve structurally similar prior notes, treat them as hypotheses, verify against current state, and record only reusable new lessons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may rely on stale or mismatched prior notes when solving drift-sensitive tasks.

Mitigation: Use retrieved notes only as hypotheses, inspect current state before changes, and verify the real outcome with a falsifiable test.

Risk: The agent may consult local notes or memory that contain sensitive or irrelevant context.

Mitigation: Use only available and appropriate note sources, read the original context before reuse, and record only compact reusable deltas.

## Reference(s):

- [Server-resolved source import](https://github.com/pinguy/Skills/tree/main/skills/check-notes-first)
- [ClawHub skill page](https://clawhub.ai/pinguy/skills/check-notes-first)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Markdown guidance with an optional compact text note template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code; may guide the agent to consult available notes and optionally write a concise verified lesson.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
