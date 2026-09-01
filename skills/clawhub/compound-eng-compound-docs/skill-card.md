## Description:

Document solved problems for team reuse by capturing resolved issues, lessons learned, post-mortems, and searchable knowledge-base entries after debugging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn non-trivial resolved debugging sessions into structured troubleshooting documentation with validated YAML metadata, related issue links, and optional follow-up actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update repository troubleshooting documentation.

Mitigation: Review generated documentation before committing or publishing it.

Risk: Captured debugging context could include secrets, customer data, private URLs, or personal information.

Mitigation: Redact sensitive data before saving error context, symptoms, commands, or examples.

Risk: Follow-up actions such as adding to an existing skill or creating a new skill can change future agent behavior.

Mitigation: Treat those menu choices as explicit follow-up actions and review the resulting changes carefully.

## Reference(s):

- [Compound docs on ClawHub](https://clawhub.ai/iliaal/skills/compound-eng-compound-docs)
- [documentation-process.md](artifact/references/documentation-process.md)
- [yaml-schema.md](artifact/references/yaml-schema.md)
- [quality-guidelines.md](artifact/references/quality-guidelines.md)
- [example-scenario.md](artifact/references/example-scenario.md)
- [resolution-template.md](artifact/assets/resolution-template.md)
- [critical-pattern-template.md](artifact/assets/critical-pattern-template.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown troubleshooting documents with YAML frontmatter, inline code blocks, shell validation commands, and decision-menu guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one documentation file per resolved problem under docs/solutions/[category]/ and may propose follow-up linking or skill-update actions after user selection.]

## Skill Version(s):

4.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
