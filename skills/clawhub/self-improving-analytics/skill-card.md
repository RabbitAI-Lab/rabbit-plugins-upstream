## Description:

Captures analytics learnings about data quality issues, metric drift, pipeline failures, misleading visualizations, metric definition mismatches, and data freshness problems so teams can improve analytics workflows over time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Data practitioners, analytics engineers, and agent users use this skill to record pipeline incidents, data quality findings, metric-definition conflicts, and analytics feature requests in local learning files. Teams can later review those entries and promote recurring patterns into data dictionaries, runbooks, dashboard standards, or data quality SLAs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local .learnings files may capture sensitive analytics details if users paste raw query output, credentials, or personal data.

Mitigation: Use redacted summaries, avoid connection strings, database credentials, API keys, and PII, and review entries before sharing or promoting them.

Risk: Hooks can persist across sessions and may be too broad if enabled outside the intended project.

Mitigation: Keep hooks project-scoped, prefer the lightweight prompt reminder by default, and avoid global hook installation.

Risk: PostToolUse error detection inspects command output and may surface sensitive pipeline or query context.

Mitigation: Enable PostToolUse only when command-output inspection is desired and avoid logging SQL results or transcripts verbatim.

Risk: Promoting analytics learnings into agent files, runbooks, or generated skills can preserve incorrect guidance if not reviewed.

Mitigation: Review proposed edits and generated skills before applying them, and promote only recurring or broadly applicable patterns.

## Reference(s):

- [OpenClaw Integration](references/openclaw-integration.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [Entry Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell, SQL, JSON, and YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local .learnings markdown entries, optional hook reminder text, and reviewable skill scaffolds.]

## Skill Version(s):

1.1.1 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
