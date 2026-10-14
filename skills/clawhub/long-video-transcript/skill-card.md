## Description:

Turns supported public video links into transcript segments, on-screen text where available, and key points for a readable summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

People reviewing public lectures, courses, podcasts, and social videos use this skill to obtain transcripts, key points, and available on-screen text without downloading the video locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video links and an optional API key are sent to LinkDigest; text from public links may be cached for other users.

Mitigation: Use only links appropriate for external processing; avoid private links and keep the API key out of chat and source control.

Risk: The script may select a more expensive processing mode than the skill instructions promise.

Mitigation: Pass --depth transcript explicitly and set --max-credits before paid requests.

Risk: The optional npx mcp-remote integration introduces an additional executable dependency.

Mitigation: Avoid that integration or pin and review the dependency before use.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest OpenAPI specification](https://linkdigest.dev/openapi.json)
- [ClawHub skill listing](https://clawhub.ai/jackchew7143/skills/long-video-transcript)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript timestamps are segment-level; on-screen text coverage varies by mode and platform. Without an API key, output is summary-only.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
