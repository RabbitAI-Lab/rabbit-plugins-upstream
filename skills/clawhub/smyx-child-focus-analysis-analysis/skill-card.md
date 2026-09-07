## Description:

Analyzes smart desk lamp or tabletop camera video of a child's study area to estimate per-minute focus scores, identify distraction events, and produce structured focus reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, teachers, and developers use this skill to process child study-area video files or URLs and review focus scores, distraction periods, alerts, report links, and historical analysis records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles children's study-area video, which may contain sensitive minor data.

Mitigation: Use only with explicit guardian or administrator consent and only after the publisher documents upload destination, retention, deletion, and protection practices.

Risk: Security evidence reports unsafe defaults, including unencrypted private-network API endpoints.

Mitigation: Do not use with real children's videos until the publisher removes packaged dev endpoints and enforces HTTPS to approved public services.

Risk: Security evidence reports local plaintext credential persistence and silent account creation.

Mitigation: Run in an isolated environment and avoid production use until the publisher protects or avoids persisted bearer tokens and stops silent account creation.

Risk: Security guidance flags a dependency naming issue.

Mitigation: Review and install dependencies in a sandbox, and require the publisher to correct the dependency metadata before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-focus-analysis-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Child focus analysis API documentation](references/api_doc.md)
- [Shared video analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown status text with JSON or structured report content, report links, and optional file output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file or URL input, basic/standard/json detail levels, and historical report listing.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
