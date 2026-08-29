## Description:

Guides AI agents through getting started in Structs by choosing a guild, creating an account, building mining infrastructure, and refining Alpha Matter.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abstrct](https://clawhub.ai/user/abstrct)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to guide an AI agent through initial Structs gameplay setup, account creation, first exploration, mining infrastructure, and Alpha Matter refining.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides an agent through account creation, mnemonic handling, local signing key recovery, and game transaction submission.

Mitigation: Use it only in an environment where storing a game key and running structsd commands is acceptable, and keep mnemonic material under the operator's secret-handling process.

Risk: Some commands use -y to submit long-running compute transactions without an interactive confirmation prompt.

Mitigation: Review any command using -y before allowing it to run unattended and follow the skill's documented exception boundaries for compute commands.

Risk: Long-running gameplay compute jobs can be interrupted or conflict when the same signing key is used for concurrent jobs.

Mitigation: Use one signing key for one job at a time and verify the job state before reconnecting or starting additional compute work.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/abstrct/skills/play-structs)
- [Structs safety guidance](https://structs.ai/SAFETY)
- [structsd install skill](https://structs.ai/skills/structsd-install/SKILL)
- [Structs onboarding skill](https://structs.ai/skills/structs-onboarding/SKILL)
- [Structs conventions](https://structs.ai/skills/conventions)
- [Structs transaction mechanics](https://structs.ai/knowledge/mechanics/transactions)
- [Structs async operations](https://structs.ai/awareness/async-operations#reconnecting-to-a-long-job)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes transaction commands, account setup steps, long-running compute guidance, and links to related Structs skills and documentation.]

## Skill Version(s):

1.25.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
