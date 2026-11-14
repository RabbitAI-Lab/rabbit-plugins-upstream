## Description:

Prepare and privately submit a Submission — a folder of files or a single file — for an Elgora bounty as its Solver, then read the finalized outcome and claim the award when it wins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elmariachi111](https://clawhub.ai/user/elmariachi111)

### License/Terms of Use:

MIT-0

## Use Case:

Developers acting as Elgora Solvers use this skill to find and assess a bounty, prepare a private submission that meets its requirements, and check the finalized result. A winning Solver can use it to claim the award.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is medium confidence and partial because some references could not be resolved; the scanner also noted possible mismatch between reported capabilities and the stated bounty workflow.

Mitigation: Review the skill and any available references, and compare requested actions with the stated workflow before installing or using it.

Risk: The workflow can configure webhook notifications and initiate wallet-backed submission or award-claim actions.

Mitigation: Review webhook destinations and command details, keep webhook credentials private, and require the Solver's explicit approval before signing or disclosing anything.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/elmariachi111/skills/elgora-solver-skill)
- [Public Elgora Solver skill bundle](https://elgora.ai/skills/elgora-solver-skill/SKILL.md)
- [Elgora testnet](https://testnet.elgora.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance with shell command examples and challenge-specific submission files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Submission contents and constraints depend on the selected bounty.]

## Skill Version(s):

7.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
