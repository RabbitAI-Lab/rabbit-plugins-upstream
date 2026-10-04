## Description:

Analyzes cat and dog vocalizations to suggest emotions and behavioral intentions and provide reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and their agents use audio, video, or media URLs to obtain suggested interpretations of cat and dog sounds and retrieve past analysis reports. Results are for interaction and entertainment, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet audio, video, or supplied media URLs may be sent to lifeemergence.com cloud services.

Mitigation: Review the service's data handling and obtain consent before submitting sensitive media or URLs.

Risk: The skill can silently create or reuse a persistent local identity and store authentication tokens in the workspace.

Mitigation: Avoid real phone numbers and personal identifiers until the publisher documents account, token storage, and deletion controls; protect and clear workspace credentials.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-vocal-emotion-analysis)
- [Pet vocal analysis API documentation](references/api_doc.md)
- [Analysis API error codes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis reports or report lists, with an optional saved text file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include suggested emotions, behavioral intentions, recommendations, and report links.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release; bundled frontmatter says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
