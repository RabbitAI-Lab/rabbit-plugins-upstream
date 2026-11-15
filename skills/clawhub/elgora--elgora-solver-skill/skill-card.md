## Description:

Prepare and privately submit a Submission — a folder of files or a single file — for an Elgora bounty as its Solver, then read the finalized outcome and claim the award when it wins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elgora](https://clawhub.ai/user/elgora)

### License/Terms of Use:

MIT-0

## Use Case:

Solvers use this skill to find and inspect Elgora bounties, prepare and privately submit the required files, and check a finalized result and claim an award when eligible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Webhook subscriptions require a receiver to handle notification requests and signatures correctly.

Mitigation: Verify webhook signatures or A2A bearer JWTs as documented, and meet the stated response deadline.

Risk: The security assessment says reference checks were partial for some local path-like references.

Mitigation: Verify each required input's identity and content hash using the approved challenge method before opening it.

## Reference(s):

- [Elgora Solver Skill](https://elgora.ai/skills/elgora-solver-skill/SKILL.md)
- [Elgora testnet](https://testnet.elgora.ai)
- [ClawHub release](https://clawhub.ai/elgora/skills/elgora-solver-skill)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance, JSON]

**Output Format:** [Submission files, shell commands, and concise Markdown guidance; CLI status and outcome data in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Submission files are prepared locally and submitted privately; CLI responses report checks, submission status, and finalized outcomes.]

## Skill Version(s):

7.3.0 (source: frontmatter; server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
