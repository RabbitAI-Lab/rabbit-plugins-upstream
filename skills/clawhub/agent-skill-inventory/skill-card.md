## Description:

Inventories local agent skills, estimates their context cost, and recommends which skills to keep, review, or consider closing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and administrators assess installed skills, context footprint, duplicates, and usage or configuration dependencies before deciding whether to disable any skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory reads local skill files, usage logs, and automation or hook configurations that may contain sensitive information.

Mitigation: Review the selected directories and logs before running the local report; share its results only where appropriate.

Risk: Applying close recommendations can disable skills needed by an agent or its workflows.

Mitigation: Start with the report or dry-run, review every candidate and dependency, and use --overrides --apply --yes only after explicit approval.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/elisabeth15501/skills/agent-skill-inventory)
- [ClawHub publisher profile](https://clawhub.ai/user/elisabeth15501)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain-text inventory report or machine-readable JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports usage and dependency buckets, duplicate hints, and estimated context cost; JSON keys remain in English.]

## Skill Version(s):

1.4.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
