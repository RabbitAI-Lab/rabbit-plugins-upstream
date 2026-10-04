## Description:

Inventories an agent's installed skills, estimates their context cost, detects duplicates, and offers conservative recommendations for reviewing skills before closing them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and administrators assess installed skills, estimated context use, usage records, and configuration dependencies to identify candidates for manual review or closure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Usage logs can miss indirect invocations, so an apparently unused skill may still be needed.

Mitigation: Review the read-only report, dependency references, and individual impact before confirming any closure; missing usage logs do not justify closing skills.

Risk: Applying skill overrides can disable listed skills and change agent behavior.

Mitigation: Inspect the candidates and dry run first; use the explicit apply and confirmation flags only after accepting the automatic backup and restoration path.

Risk: The inventory reads local skill folders and automation or hook configuration.

Mitigation: Install and run it only where inspection of those local files is acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/elisabeth15501/skills/agent-skill-inventory)
- [Skill trigger taxonomy and usage-log limitations](references/usage-triggers.en.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain-text inventory report or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports classify skills as used, protected, closeable candidates, or needing manual review; JSON keys remain in English.]

## Skill Version(s):

1.3.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
