## Description:

Analyzes cat scratch post videos or video URLs to estimate scratching frequency, session duration, and relative intensity, then returns structured behavioral observations for stress and claw-health monitoring without disease diagnosis or behavior-correction advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to analyze cat scratch post footage, produce structured scratch behavior reports, and query historical reports for smart scratch post or multi-cat household monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or video URLs are sent to external Life Emergence services for analysis.

Mitigation: Use only footage that is acceptable to share with that service, and review the service's retention and access controls before deployment.

Risk: Reports can be associated with an internal user identity that is created or reused automatically.

Mitigation: Deploy only in environments where automatic identity association is expected, documented, and covered by user consent or internal policy.

Risk: Account or session tokens may be persisted in the workspace data area.

Mitigation: Restrict workspace access, rotate credentials when removing the skill, and inspect local data storage before sharing the workspace.

## Reference(s):

- [Pet health analysis API documentation](artifact/references/api_doc.md)
- [Shared analysis API error reference](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-style structured report text, with optional CLI commands and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis output to a file when an output path is provided; historical report queries are returned as Markdown tables.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
