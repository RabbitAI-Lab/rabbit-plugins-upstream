## Description:

Analyzes HD succulent images or videos to identify black rot, melting, and stretching, then returns anomaly type, severity, confidence, and report links for growers and plant-care operators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and plant-care operators use this skill to submit succulent media or URLs for special-state detection and to retrieve prior cloud reports linked to the current identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media and URLs are sent to external lifeemergence services for analysis.

Mitigation: Use the skill only with images, videos, and URLs that the user is willing to process through those cloud services.

Risk: The skill may create or reuse a local account identity and store authentication tokens in the workspace data directory.

Mitigation: Review the workspace data directory permissions before use and clear stored identity or token data when it is no longer needed.

Risk: History retrieval may fetch prior cloud reports for the resolved identity.

Mitigation: Confirm that the active identity is appropriate before listing reports and avoid sharing report history beyond the intended user or workspace.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-succulent-special-state-detection-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON analysis output with report links and optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file or URL inputs, history-list retrieval, and basic, standard, or JSON detail levels.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
