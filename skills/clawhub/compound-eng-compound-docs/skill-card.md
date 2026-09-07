## Description:

Document solved problems for team reuse by capturing resolved issues, lessons learned, post-mortems, and searchable debugging knowledge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill after resolving non-trivial issues to create validated troubleshooting records, preserve root-cause analysis, and make future debugging work searchable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or modify repository troubleshooting documents and offers follow-up options that may alter skills or required-reading material.

Mitigation: Invoke it intentionally, review generated documentation and menu choices before committing, and confirm any skill-modifying follow-up action before allowing changes.

Risk: Troubleshooting writeups can become misleading or expose sensitive context if they capture incomplete, unverifiable, private, or machine-specific details.

Mitigation: Validate exact errors, root causes, file references, and YAML frontmatter before saving; remove secrets, private URLs, customer data, and local machine paths.

## Reference(s):

- [Documentation Capture Process](references/documentation-process.md)
- [YAML Frontmatter Schema](references/yaml-schema.md)
- [Quality Guidelines & Error Handling](references/quality-guidelines.md)
- [Example Scenario](references/example-scenario.md)
- [Resolution Template](assets/resolution-template.md)
- [Critical Pattern Template](assets/critical-pattern-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown documentation with YAML frontmatter and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates repository documentation after gathering context and validating frontmatter.]

## Skill Version(s):

4.5.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
