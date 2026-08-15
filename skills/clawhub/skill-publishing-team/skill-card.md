## Description:

Coordinates skill authoring, testing, security auditing, documentation, and release management to publish installable skill packages to public registries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill publishing teams use this agent configuration bundle to coordinate role-based skill authoring, testing, security review, documentation, and release preparation for installable skill packages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill-publishing workflow may read or write workspace files, run shell commands for tests and scans, coordinate agents, and store or reuse memory.

Mitigation: Use it in a controlled repository, review proposed file changes and release actions before execution, and provide only the access needed for the publishing task.

Risk: Generated skill documentation, tests, scan results, or release guidance may be incomplete or misleading if accepted without review.

Mitigation: Run the bundled evaluations and independently review security findings, documentation, changelog content, and publish readiness before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/t3ratech/skills/skill-publishing-team)
- [Publisher profile](https://clawhub.ai/user/t3ratech)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, code snippets, shell commands, configuration edits, and release guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify workspace files and coordinate role-specific agent work during skill publishing workflows.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
