## Description:

Document solved problems for team reuse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to capture resolved debugging sessions, post-mortems, lessons learned, and reusable knowledge as structured solution documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Debugging records may include secrets, private URLs, customer data, sensitive logs, or machine-specific paths.

Mitigation: Preview generated documentation before writing, redact sensitive values, and avoid storing private or machine-specific data.

Risk: The workflow can persist debugging details into the repository without an explicit redaction checkpoint.

Mitigation: Require user confirmation before writing solution files and review the final Markdown for sensitive content.

Risk: YAML validation depends on Python 3 and PyYAML, and missing dependencies could leave frontmatter unchecked.

Mitigation: Install PyYAML only in a controlled or pinned environment and report dependency failures instead of claiming validation.

Risk: Schema drift or example/schema mismatches can produce invalid metadata for solution documents.

Mitigation: Validate generated frontmatter with the bundled validator and align enum values with artifact/references/yaml-schema.md before file creation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-compound-docs)
- [Publisher profile](https://clawhub.ai/user/iliaal)
- [Documentation Capture Process](artifact/references/documentation-process.md)
- [YAML Frontmatter Schema](artifact/references/yaml-schema.md)
- [Quality Guidelines & Error Handling](artifact/references/quality-guidelines.md)
- [Example Scenario](artifact/references/example-scenario.md)
- [Resolution Template](artifact/assets/resolution-template.md)
- [Critical Pattern Template](artifact/assets/critical-pattern-template.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown solution documents with YAML frontmatter, validation commands, and follow-up guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates files under docs/solutions/ and may add cross-references or critical-pattern entries after user confirmation.]

## Skill Version(s):

4.5.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
