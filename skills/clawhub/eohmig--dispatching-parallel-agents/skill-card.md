## Description:

Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to decide when independent failures or workstreams should be delegated to separate subagents in parallel, and how to scope each subagent prompt so results can be reviewed and integrated.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Parallel subagents can make concurrent code changes that conflict or introduce incorrect fixes.

Mitigation: Keep each subagent prompt tightly scoped, review returned changes for conflicts, and run the full test suite before integration.

Risk: Dispatching agents on related failures or shared state can duplicate work or cause interference.

Mitigation: Use the skill only after grouping independent problem domains; handle related failures or shared-state work sequentially or in a single investigation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eohmig/skills/dispatching-parallel-agents)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown guidance with workflow steps and prompt examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advises on parallel subagent dispatch; it does not execute tools by itself.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
