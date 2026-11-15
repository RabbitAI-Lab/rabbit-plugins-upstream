## Description:

Summarize or transcribe URLs, YouTube/videos, podcasts, articles, transcripts, PDFs, and local files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huipan1973](https://clawhub.ai/user/huipan1973)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can summarize or transcribe web links, video and podcast sources, PDFs, and local files with the summarize CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local file contents may be sent to the configured external model provider during summarization.

Mitigation: Review the provider and file contents before summarizing; use --extract when you only need extracted content without a model summary.

Risk: The security review is incomplete because a local path-like reference could not be resolved.

Mitigation: Resolve and review that reference before relying on the scan verdict.

## Reference(s):

- [Summarize website](https://summarize.sh)
- [ClawHub skill page](https://clawhub.ai/huipan1973/skills/summarize)
- [Publisher profile](https://clawhub.ai/user/huipan1973)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text or JSON; extracted content or a best-effort transcript when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summary length and maximum output tokens are configurable.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
