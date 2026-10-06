## Description:

Summarizes YouTube videos and extracts timestamped transcripts and on-screen text, with optional Chinese translation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents use this skill to summarize YouTube links, locate moments in timestamped transcripts, read on-screen text, and optionally translate results into Chinese without relying on existing captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted video links are processed remotely and text results may be cached by link.

Mitigation: Do not submit private or sensitive links unless remote processing and caching are acceptable.

Risk: Video processing and optional translation may incur credits.

Mitigation: Set --max-credits when cost matters and review reported credit usage.

Risk: Model-generated transcripts can misstate names or numbers, and long translations may cover only part of a video.

Mitigation: Check important claims against the original video and disclose any reported coverage gaps.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/jackchew7143/skills/linkdigest-youtube-summary)
- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest API key setup](https://linkdigest.dev/app/keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown by default; JSON on request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include timestamped transcripts, on-screen text, key points, translations, coverage, and credit usage.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
