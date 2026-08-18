## Description:

Generates podcast chapters, highlights, and show notes from user-provided audio or transcripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and automation teams use this skill to turn podcast audio or transcripts into chapter lists, highlights, show notes, and structured summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, API, and shell-command authority beyond its podcast chaptering purpose.

Mitigation: Review the skill before installing and require explicit confirmation before it reads or writes local files, calls external services, or runs shell commands.

Risk: Podcast audio and transcripts can contain sensitive personal, business, or unpublished content.

Mitigation: Use only user-provided inputs and remove sensitive material before processing when the resulting chapters, highlights, or show notes may be shared.

Risk: Copyright and API-key notes in the artifact are advisory and are not technical safeguards.

Mitigation: Confirm media rights separately and manage any required API keys through environment or secret-management controls before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/podcast-chaptering-highlights)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON podcast chapters, highlights, and show notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include processing status and metadata when JSON mode is requested.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
