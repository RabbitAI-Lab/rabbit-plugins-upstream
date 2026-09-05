## Description:

Answers questions about a past agent run from its recording rather than from memory, and replays or forks that run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xizhuomengcontin](https://clawhub.ai/user/xizhuomengcontin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to investigate previous agent runs from recorded traces, reproduce failures, and compare model behavior from a shared checkpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Replay can re-execute shell commands and mutate resources outside the working tree.

Mitigation: Review recorded commands before replay, use worktree or container isolation, and get explicit approval for actions outside the repository.

Risk: Model comparison can upload recorded context to external providers and spend real money.

Mitigation: Confirm disclosure scope, provider targets, side effects, and cost before running comparisons.

Risk: Recorded traces may contain secrets, private source, prompts, or other confidential data when shared.

Mitigation: Scrub exported traces, manually review what remains, and get user agreement before sending a trace outside the local environment.

## Reference(s):

- [OrcaReplay GitHub Repository](https://github.com/Continuum-AI-Corp/OrcaReplay)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown guidance with inline tool names and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Distinguishes recorded trace evidence from inferred causal edges and emphasizes approval before replay, model comparison, or external disclosure.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
