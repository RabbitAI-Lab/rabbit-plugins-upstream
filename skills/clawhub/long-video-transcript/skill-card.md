## Description:

Turns supported public video links into transcripts, on-screen text, key points, and summaries through LinkDigest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content researchers use this skill to turn public video links into readable transcripts, on-screen text, notes, and summaries. A LinkDigest API key is needed for full results; keyless use provides a limited summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted media links are sent to LinkDigest for processing and may reveal sensitive content.

Mitigation: Submit only public links you are comfortable sharing with linkdigest.dev; do not submit private or access-controlled content.

Risk: Exposing the API key can allow unauthorized use of the LinkDigest account.

Mitigation: Keep LINKDIGEST_API_KEY in environment or configuration, not in chat, code, or source control.

Risk: The optional unpinned npx MCP bridge may execute an untrusted package.

Mitigation: Prefer the bundled Python client; pin and review the MCP bridge package before using it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/jackchew7143/skills/long-video-transcript)
- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest OpenAPI specification](https://linkdigest.dev/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown by default or structured JSON on request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes transcript segments, approximate timestamps, on-screen text, and key points when available; keyless results are summaries only.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
