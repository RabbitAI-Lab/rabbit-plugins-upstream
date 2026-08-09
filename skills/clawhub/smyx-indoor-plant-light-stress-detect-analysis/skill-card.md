## Description:

Detects and analyzes indoor plant light stress from images, videos, URLs, and optional lux data, identifying low-light or excessive-light symptoms and suggesting care adjustments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Plant-care users, smart-planter operators, home gardeners, office plant caretakers, and developers can use this skill to analyze plant media for insufficient, excessive, or normal light conditions and receive structured adjustment guidance. The skill can also query cloud-hosted historical light-stress reports associated with the current internal identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or media URLs are sent to the LifeEmergence cloud service for analysis.

Mitigation: Use only media you are comfortable uploading to that service, and avoid sensitive images or videos.

Risk: Reports may be associated with an automatically resolved or created internal identity.

Mitigation: Review whether identity-linked cloud report history is acceptable before using analysis or list mode.

Risk: Service tokens and identity values may be stored in the workspace data directory.

Mitigation: Review and remove data/smyx-api-key.txt and related workspace data if the identity or token should not be reused.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-indoor-plant-light-stress-detect-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](artifact/references/api_doc.md)
- [Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text containing structured JSON analysis, care suggestions, report links, or historical report tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report export links and historical report records when list mode is used.]

## Skill Version(s):

1.0.6 (source: server release evidence; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
