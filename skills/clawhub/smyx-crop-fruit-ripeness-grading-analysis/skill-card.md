## Description:

Identifies fruit ripeness stages (green / turning / ripe / over-ripe) based on color, size and gloss features to output a standardized ripeness grade.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External growers, agronomy teams, and agents use this skill to analyze fruit images or videos for ripeness grading, harvest-window guidance, and cloud report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media files or URLs are sent to a remote analysis service.

Mitigation: Review the service endpoint, data-handling terms, and input sensitivity before submitting crop media.

Risk: The skill manages identity, account tokens, report history, and persistent local state.

Mitigation: Confirm token storage, token-retention controls, and local state cleanup requirements before deployment.

Risk: Cloud report history can be queried automatically for the current identity.

Mitigation: Verify access controls and report-retention policy before enabling history lookup workflows.

Risk: The security evidence flags dev/private endpoint configuration and unclear token-retention controls.

Mitigation: Resolve endpoint configuration and token-retention controls with the publisher before production use.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files]

**Output Format:** [Markdown report or JSON analysis, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ripeness grades, harvest-window guidance, report links, and history tables from the remote service.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
