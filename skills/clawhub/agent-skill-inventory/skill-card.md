## Description:

Inventories agent skills, estimates their context footprint, checks dependencies, and suggests which skills merit review before disabling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

People managing office-agent skill libraries use this skill to identify duplicates, estimate context-token overhead, inspect dependencies, and review candidates for disabling without accidentally removing needed skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local inventory reads skill directories, usage logs, and automation or configuration files.

Mitigation: Install only if this local access is acceptable; start with the default report-only mode.

Risk: Applying proposed closures can persistently disable WorkBuddy skills, and usage logs may miss indirect invocations.

Mitigation: Review each candidate and its dependency impact before explicitly using --overrides --apply --yes; restore disabled skills through the host's skill controls if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/elisabeth15501/skills/agent-skill-inventory)
- [English usage documentation](artifact/README.en.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Human-readable inventory report or machine-readable JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Four review categories, dependency-impact previews, and English-keyed JSON; report language can be Chinese or English.]

## Skill Version(s):

1.3.3 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
