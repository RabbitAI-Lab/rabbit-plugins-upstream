## Description:

Analyzes cat climbing frame or cat tree video from a local file or URL by calling remote APIs to estimate dwell time by layer, jump or transition counts, activity density, and a 2D activity heatmap without providing disease diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet-camera videos of cat trees or climbing frames, review activity distribution metrics, and retrieve related remote analysis reports. The results support exercise and enrichment observation, not medical diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-camera media and related metadata are uploaded or submitted to the publisher's remote service.

Mitigation: Use only media appropriate for sharing with that service and avoid private home footage unless the publisher's account creation, retention, and handling practices are acceptable.

Risk: The skill silently creates or reuses remote identities and stores tokens locally.

Mitigation: Review identity and token storage behavior before deployment, use isolated workspaces where appropriate, and prefer safer secret storage.

Risk: The release includes unsafe default HTTP development endpoints.

Mitigation: Use reviewed HTTPS production endpoints and remove development HTTP defaults before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-climbing-frame-heatmap-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Pet climbing frame API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, configuration]

**Output Format:** [JSON or Markdown report text with structured activity metrics and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local mp4, avi, or mov files up to 10MB or video URLs; history queries return remote report lists.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
