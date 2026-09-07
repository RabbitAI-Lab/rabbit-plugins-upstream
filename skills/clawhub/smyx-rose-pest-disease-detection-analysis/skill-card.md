## Description:

Analyzes rose or Chinese rose images, videos, or URLs to identify common pests and diseases, estimate severity, and return general control guidance and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External gardeners, rose growers, and agents supporting horticulture workflows use this skill to assess rose leaf, shoot, and bud media for likely pest or disease symptoms, severity, and general care recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded rose images, videos, or URLs are sent to an external service for analysis.

Mitigation: Use only non-sensitive media and public or otherwise approved URLs after accepting the external processing flow.

Risk: The skill may create or reuse an internal identity and store account tokens locally.

Mitigation: Run the skill only in workspaces where local account-token storage is acceptable, and review or clear local state before sharing the workspace.

Risk: History queries can retrieve account-linked cloud reports.

Mitigation: Enable history lookup only where account-linked report access is expected and authorized.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-rose-pest-disease-detection-analysis)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include severity labels, general control suggestions, progress text, and links to exported reports.]

## Skill Version(s):

1.0.5 (source: server release evidence; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
