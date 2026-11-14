## Description:

Use when needed functionality may already exist online: search, quality-check, harvest data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blueboyzx](https://clawhub.ai/user/blueboyzx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find and compare community skills or domain knowledge before building a new capability. It produces an attributed harvest report and asks for explicit approval before any candidate is installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation and request-derived search terms sent to an external registry may expose information from a user's request.

Mitigation: Use the skill only for clear search or comparison requests, and remove confidential details from search terms before sending them to the registry.

Risk: The security scan is partial because some local references were unresolved, leaving referenced behavior uncovered.

Mitigation: Review the unresolved referenced behavior and the skill's proposed candidates before relying on the harvest report.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/blueboyzx/skills/skill-import-harvest)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Markdown report with a comparison matrix and attributed findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Candidate findings include source attribution and a recommendation; installation requires fresh explicit user approval.]

## Skill Version(s):

1.0.1 (source: frontmatter; server release evidence: 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
