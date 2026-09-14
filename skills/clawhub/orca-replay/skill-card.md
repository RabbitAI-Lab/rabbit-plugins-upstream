## Description:

Answers questions about a past agent run from its recording rather than from memory, and replays or forks that run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xizhuomengcontin](https://clawhub.ai/user/xizhuomengcontin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect recorded agent traces, explain prior behavior from evidence, reproduce recorded failures, and compare model behavior from a checkpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the required orcareplay npm package can change the user's machine.

Mitigation: Confirm trust in the package before installation and prefer a pinned or isolated install where practical.

Risk: Replay or comparison can repeat shell commands and external side effects from the recorded run.

Mitigation: Review the original run before replay or compare, use worktree or container isolation where appropriate, and obtain specific approval for external side effects.

Risk: Comparing models or sharing traces can disclose source, prompts, configuration, credentials, or other sensitive run context.

Mitigation: Inspect and scrub traces before sharing or uploading them, and confirm disclosure to each provider explicitly.

## Reference(s):

- [OrcaReplay homepage](https://github.com/Continuum-AI-Corp/OrcaReplay)
- [ClawHub skill page](https://clawhub.ai/xizhuomengcontin/skills/orca-replay)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline tool and shell command references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May distinguish recorded trace evidence from inferred causal links.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
