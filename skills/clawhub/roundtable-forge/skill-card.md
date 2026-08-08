## Description:

Roundtable Forge routes a user's question into a structured, cross-disciplinary multi-agent roundtable with independent character perspectives, shared Memory, synthesis, and traceable outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fxbin](https://clawhub.ai/user/fxbin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent builders use this skill to convene structured discussions among real, historical, or fictional character-lanes for broad analysis, deliberation, and synthesis. It is suited to exploratory questions that benefit from multiple perspectives, visible disagreement, continuation state, and traceable argument artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create local Memory and transcript files that preserve user-provided discussion context.

Mitigation: Avoid sensitive private content unless it is intended to be saved, and review generated Memory or transcript files before sharing or retaining them.

Risk: Broad auto-routing can orchestrate multiple persona-style responses and may make simulated viewpoints feel authoritative.

Mitigation: Use explicit roundtable prompts, keep the AI simulation disclaimer visible, and treat character responses as analytical simulation rather than official statements.

Risk: Discussions involving real people or recognizable fictional characters can be mistaken for endorsed or authentic speech.

Mitigation: Preserve the provided disclaimer and avoid presenting generated character dialogue as the real person's, institution's, or rights holder's position.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fxbin/skills/roundtable-forge)
- [Server-resolved GitHub provenance](https://github.com/fxbin/skills/tree/main/roundtable-forge)
- [Roundtable Protocol](references/roundtable-protocol.md)
- [Multi-Agent Runtime Protocol](references/multi-agent-runtime-protocol.md)
- [Output Template Contract](references/output-template-contract.md)
- [Memory Schema](references/memory-schema.md)
- [Argument Graph Protocol](references/argument-graph-protocol.md)
- [Sources & Citations Protocol](references/sources-and-citations.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown transcripts, podcast scripts, Mermaid argument graphs, and JSON Memory files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be rendered from a validated Memory JSON source and include the AI simulation disclaimer when representing real people or recognizable fictional characters.]

## Skill Version(s):

v2.9.0 (source: artifact/VERSION); release 0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
