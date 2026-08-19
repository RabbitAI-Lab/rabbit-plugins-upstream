## Description:

Unifies text, code, vision labels, and tool-state observations into a grounded state for cross-modal consistency checks, deterministic state transitions, forward simulation, counterfactual analysis, and uncertainty reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to merge heterogeneous observations into a shared grounded state, detect contradictions across modalities, and simulate or compare possible action paths before acting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learning subsystem can persist local usage records, error notes, and preferences across sessions.

Mitigation: Review the skill before installation, make learning opt-in where possible, scope records to this skill, and provide a clear way to inspect and clear the local learning file.

Risk: The world-model script relies on explicitly registered state transitions and label-level vision facts, so unknown actions or richer visual evidence may not be modeled accurately.

Mitigation: Treat unknown actions as high-uncertainty outputs, review contradiction and groundedness fields before acting, and connect an external multimodal model when pixel-level grounding is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/unified-world-model)

## Skill Output:

**Output Type(s):** [analysis, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or text with Python examples, JSON state snapshots, and shell commands when invoking scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce grounded state summaries, contradiction lists, simulated trajectories, counterfactual differences, uncertainty values, and local learning insights.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
