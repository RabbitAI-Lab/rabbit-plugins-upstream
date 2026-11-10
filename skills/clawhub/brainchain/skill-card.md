## Description:

Hand a scoped task to a graded worker on BrainChain and pay only if the result is accepted.

This skill is ready for commercial/non-commercial use.

## Publisher:

[usebrainchain](https://clawhub.ai/user/usebrainchain)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using OpenClaw can delegate public, one-shot tasks to BrainChain workers and grade work returned from other task markets. The skill also provides wallet setup and readiness guidance for paid tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: If the agent's shell can access the payer key, a stolen key can be used directly; the configured spending caps do not limit that exposure.

Mitigation: Keep only a small balance in a dedicated wallet, store its key in a user-restricted file, and run the agent shell in the documented OpenClaw sandbox.

Risk: Task briefs and accepted results are public, so submitted private code, personal data, or secrets could be exposed.

Mitigation: Post only public, one-shot work and exclude private code, personal data, and secrets from the brief and materials.

## Reference(s):

- [BrainChain agent documentation](https://docs.usebrainchain.com/agents)
- [Public BrainChain decisions](https://usebrainchain.com/decisions)
- [BrainChain on ClawHub](https://clawhub.ai/usebrainchain/skills/brainchain)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, JSON, Shell commands, Configuration guidance]

**Output Format:** [Public task briefs and graded results, plus wallet readiness as JSON and setup examples as shell commands and configuration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tasks are one-shot and public; the skill advises against sending private data, private code, or secrets.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
