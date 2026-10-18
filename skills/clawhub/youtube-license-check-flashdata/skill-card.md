## Description:

Checks a YouTube video's Creative Commons license label through FlashData for recording or rights review, without determining training or reuse permission.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Video researchers and rights reviewers use this skill to record a known video's Creative Commons license-label classification and retrieval time, or to explain a returned classification. They review the actual license and intended use separately before deciding whether reuse is allowed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A FlashData API key and requested video identifiers are sent to FlashData for a query.

Mitigation: Use protected secret configuration and run queries only if you trust the service.

Risk: Data queries spend FlashData Credits, including submissions with uncertain outcomes after a timeout.

Mitigation: Confirm pricing and the approved budget before querying; check the existing job or console instead of automatically resubmitting after a timeout.

Risk: A Creative Commons license-label match may be mistaken for permission to train on or reuse a video.

Mitigation: Treat the result as metadata for review and inspect the actual license and intended use before making a rights decision.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/rocosen/skills/youtube-license-check-flashdata)
- [FlashData YouTube trainability documentation](https://flashdata.dev/docs/sources/youtube_trainability?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_trainability-task)
- [FlashData MCP documentation](https://flashdata.dev/mcp)
- [Query example](references/query.json)
- [Input schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-language interpretation or JSON classification for a video record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Record the video ID, raw classification, and retrieval time; the label is not legal clearance.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
