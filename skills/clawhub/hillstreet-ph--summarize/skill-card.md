## Description:

Summarize or transcribe URLs, YouTube/videos, podcasts, articles, transcripts, PDFs, and local files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can use the summarize CLI to turn URLs, articles, videos, podcasts, transcripts, PDFs, and local files into concise summaries or best-effort transcripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When summarizing local files, their contents may be sent to the configured model provider.

Mitigation: Before using the skill on a local file, consider whether its contents may be shared with the configured provider and choose the file and provider accordingly.

## Reference(s):

- [Summarize project homepage](https://summarize.sh)
- [Summarize on ClawHub](https://clawhub.ai/hillstreet-ph/skills/summarize)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text summaries or transcripts; JSON when the --json option is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output length can be selected with --length or --max-output-tokens; transcript extraction is best effort.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
