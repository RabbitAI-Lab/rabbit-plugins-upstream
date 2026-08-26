## Description:

Ingest, organize, and query your personal Second Brain database. Automatically handles note creation, article metadata extraction, video frame analysis, and Step 2.5 security screening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ideabib](https://clawhub.ai/user/ideabib)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to help agents ingest links, videos, and notes into a local personal knowledge base with summaries, categories, tags, and retrieval metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch and process remote article or video content, including through yt-dlp and ffmpeg.

Mitigation: Review before installing, ingest only trusted URLs, and constrain network and external tool execution where possible.

Risk: The skill persists provided notes and URLs in local knowledge files.

Mitigation: Avoid sensitive private links or personal data unless local storage permissions and access controls are appropriate.

Risk: The advertised Step 2.5 screening may not be reliable.

Mitigation: Do not rely on the screening claim unless the processor is corrected or independently verified; manually review untrusted content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ideabib/skills/second-brain)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown/text guidance with JSON entry records and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores local knowledge entries and an index; video ingestion may produce extracted frame files.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact skill.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
