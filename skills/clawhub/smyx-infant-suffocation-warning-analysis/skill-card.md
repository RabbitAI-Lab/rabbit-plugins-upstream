## Description:

Identifies prone sleeping positions, head covering, and mouth or nose occlusion in infant sleep media and returns risk alerts, structured findings, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze infant sleep monitoring videos or URLs for prone sleeping, head covering, and mouth or nose occlusion risks. The output is intended as an auxiliary monitoring report and does not replace adult supervision or medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant sleep media or URLs may be sent to configured Life Emergence/Open API services for analysis.

Mitigation: Use only authorized media and deploy only where the configured service endpoints, retention practices, and privacy requirements are acceptable.

Risk: The skill silently creates or reuses an internal identity and stores tokens in local workspace state.

Mitigation: Run in a dedicated workspace, protect the workspace data directory, and clear local state when the identity or stored tokens should not persist.

Risk: Historical report queries are sent to cloud APIs and may return prior report data associated with the resolved identity.

Mitigation: Limit use to trusted environments and verify the resolved identity context before querying history.

Risk: Bundled API documentation is partially mismatched with the infant suffocation use case.

Mitigation: Verify endpoint behavior and response fields against the live service before relying on the reports operationally.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-infant-suffocation-warning-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON or Markdown report text with structured findings, safety recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local video files or video URLs, supports sensitivity 1-5, can save results to a file, and can return a cloud history list.]

## Skill Version(s):

1.0.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
