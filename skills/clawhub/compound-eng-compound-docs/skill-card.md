## Description:

Document solved problems for team reuse by turning resolved debugging sessions into validated, searchable troubleshooting documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this workflow after non-trivial debugging or post-mortem resolution to create a validated Markdown knowledge-base entry under docs/solutions/ and choose follow-up actions such as cross-linking or critical pattern promotion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated troubleshooting documents may accidentally capture secrets, customer data, private URLs, or machine-specific paths from the debugging session.

Mitigation: Review generated docs before committing and redact sensitive or environment-specific details.

Risk: The frontmatter validator depends on Python 3 and PyYAML, so validation may fail or be unavailable in an unprepared environment.

Mitigation: Approve PyYAML only from a trusted or isolated Python environment, and report missing dependencies instead of claiming validation passed.

Risk: Optional skill-update and new-skill follow-up actions can broaden documentation into reusable agent behavior.

Mitigation: Treat those actions as explicit user choices after the documentation step, not as routine automatic changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-compound-docs)
- [Documentation Capture Process](references/documentation-process.md)
- [YAML Frontmatter Schema](references/yaml-schema.md)
- [Quality Guidelines & Error Handling](references/quality-guidelines.md)
- [Example Scenario](references/example-scenario.md)
- [Resolution Template](assets/resolution-template.md)
- [Critical Pattern Template](assets/critical-pattern-template.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration]

**Output Format:** [Markdown troubleshooting document with YAML frontmatter, validation command output, and a follow-up decision menu]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates one categorized docs/solutions/ Markdown file after validating frontmatter; optional follow-up actions may add cross-references, critical pattern entries, or skill updates with user confirmation.]

## Skill Version(s):

4.5.2 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
