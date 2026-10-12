## Description:

Helps agents turn documents, images, audio, video, and web content into readable text or Markdown through Cue Omni Reader.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to extract readable text, tables, and transcripts from files or URLs for document processing, OCR, and media analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local files and URLs submitted for parsing may expose sensitive content to Cue services despite privacy claims.

Mitigation: Only submit content approved for Cue processing and narrowly restrict the local directories the connector can access.

Risk: API keys could be exposed if an agent reads or reuses credentials outside an approved configuration path.

Mitigation: Have the user configure the key through an explicitly approved path; do not let the agent read or reuse the key elsewhere.

Risk: Unpinned package installation commands may fetch changed or unreviewed code.

Mitigation: Review installation commands and pin a trusted package version instead of using @latest.

## Reference(s):

- [ClawHub release](https://clawhub.ai/panting09266-ai/skills/cue-omni-reader)
- [Cue Omni Reader product page](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Markdown or plain text, with optional configuration and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include OCR text, structured tables, and audio or video transcripts.]

## Skill Version(s):

1.2.14 (source: ClawHub release; bundled SKILL.md frontmatter: 1.8.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
