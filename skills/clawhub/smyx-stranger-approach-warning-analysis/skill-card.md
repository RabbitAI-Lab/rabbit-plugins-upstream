## Description:

Detects the appearance of strangers near minors and issues safety reminder alerts for homes, schools, childcare centers, and similar environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to analyze authorized monitoring images or videos for possible strangers near minors, receive structured risk results, and retrieve prior cloud analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child-monitoring media and report history may be sent to and stored by remote LifeEmergence/Open API services.

Mitigation: Use only media the operator is authorized to upload, review privacy and compliance requirements before deployment, and avoid submitting unnecessary footage.

Risk: The skill can silently create or reuse persistent identity and authentication state for analysis and broad report-history retrieval.

Mitigation: Run it in a controlled environment, confirm identity handling is acceptable, restrict access to report-history commands, and clear local identity or token state when no longer needed.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stranger-approach-warning-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown or JSON text with structured analysis results, risk guidance, report links, and optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local media inputs are validated for supported formats and a 10 MB size cap; history queries return cloud report records.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
