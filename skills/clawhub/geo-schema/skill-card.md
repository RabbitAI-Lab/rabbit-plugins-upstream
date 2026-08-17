## Description:

Schema.org structured data audit and generation optimized for AI discoverability - detect, validate, and generate JSON-LD markup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO practitioners, and site operators use this skill to audit structured data on web pages, identify Schema.org gaps, and generate ready-to-use JSON-LD for AI discoverability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may fetch target web pages and write a local GEO-SCHEMA-REPORT.md.

Mitigation: Confirm target URLs before fetching and ask before overwriting an existing report when preservation matters.

Risk: Generated structured data can be incomplete or inaccurate for the target entity.

Mitigation: Review generated JSON-LD against the source site and validate it with Schema.org or rich result testing tools before deployment.

## Reference(s):

- [Schema.org full hierarchy](https://schema.org/docs/full.html)
- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/geo-schema)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown report with JSON-LD code blocks and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a local GEO-SCHEMA-REPORT.md unless the agent is directed otherwise.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
