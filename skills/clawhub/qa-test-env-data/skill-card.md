## Description:

Guides QA teams through test-environment setup, health checks, troubleshooting, and test-data preparation and cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this skill to plan and check authorized test environments, troubleshoot environment issues, and prepare and maintain test data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes or cleanup may affect the wrong environment or disrupt shared test services.

Mitigation: Confirm the exact target is an authorized non-production environment; obtain human approval for restarts, configuration changes, or data modifications and coordinate shared-environment changes.

Risk: Test-data cleanup may remove needed data.

Mitigation: Confirm a usable backup before cleanup and trial bulk operations on a limited scope first.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/kokxi/skills/qa-test-env-data)

## Skill Output:

**Output Type(s):** [Markdown, Configuration guidance, Checklists]

**Output Format:** [Markdown with environment health and data-preparation checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Environment configurations use unique ENV-XXXX identifiers; guidance includes environment requirements, design, configuration, and maintenance plans.]

## Skill Version(s):

1.7.7 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
