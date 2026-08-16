## Description:

Brand mention and authority scanner for AI visibility. Analyzes brand presence across platforms that AI models rely on for entity recognition and citation decisions. Produces a Brand Authority Score (0-100) with platform-specific recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and SEO practitioners use this skill to research a brand's public visibility across platforms used by AI systems and produce a brand authority report with platform-specific recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs public web research and may surface incomplete, outdated, or misleading platform signals.

Mitigation: Review the generated findings, source dates, and recommendations before using the report for business decisions.

Risk: The workflow includes an optional Bash command for entity scanning.

Mitigation: Review or approve proposed shell commands before execution, especially commands that query external services or write local report files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/geo-brand-mentions)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with tables, findings, recommendations, and optional inline shell command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a local GEO-BRAND-MENTIONS.md brand authority report.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
