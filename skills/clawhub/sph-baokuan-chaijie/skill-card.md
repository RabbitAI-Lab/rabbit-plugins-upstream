## Description:

Processes one or more WeChat Channels share links into downloaded media, Whisper transcripts, extracted metadata, and an HTML report that breaks down viral content patterns and reusable marketing tactics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mikogeyu-cell](https://clawhub.ai/user/mikogeyu-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Content marketers and operators use this skill to analyze public WeChat Channels videos, compare viral patterns across one or more links, and produce practical recommendations for titles, tags, structure, and promotion strategy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a logged-in Tencent Yuanbao browser session to access WeChat Channels content.

Mitigation: Confirm the account session is appropriate for the intended use and run the workflow only in an environment where that browser session can be used.

Risk: The workflow stores downloaded videos, extracted audio, transcripts, and metadata locally, which may include sensitive or copyrighted content.

Mitigation: Use a dedicated output directory, limit access to retained files, and delete media and transcripts when they are no longer needed.

Risk: Generated transcripts and content-performance analysis can contain transcription errors or misleading marketing conclusions.

Mitigation: Review transcripts, extracted metrics, and recommendations before using the report for publication, strategy, or client-facing decisions.

## Reference(s):

- [视频号爆款拆解分析框架](references/analysis_framework.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, JSON metadata, transcript text files, downloaded media files, and an HTML analysis report.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local video, audio, transcript, metadata, and report files in the selected output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
