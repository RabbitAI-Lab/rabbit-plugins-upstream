## Description:

Converts local or online videos into cleaned transcripts and structured copy, with optional prompts for summaries, rewrites, highlights, storyboards, and Chinese-English translation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

External users, content teams, and developers use this skill to turn video files or public video links into transcripts, summaries, meeting notes, short-form copy, quotes, translations, and other reusable written content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads selected videos, prompts, token, and task metadata to the GuaiKei service and a presigned storage endpoint.

Mitigation: Use it only with media and prompts approved for third-party processing, and avoid confidential meetings, interviews, customer data, or unreleased business media without separate contractual or policy assurance.

Risk: The artifact makes deletion and non-retention claims that the security evidence says are unverified and partly contradictory.

Mitigation: Treat deletion and retention guarantees as unverified unless confirmed through provider terms, audit evidence, or an internal vendor review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/um-why/skills/video2text-ai)
- [GuaiKei service website](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Plain text or Markdown-style generated copy on stdout, with progress and logs on stderr.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0 or newer and GUAIKEI_API_TOKEN; accepts a video file or task ID plus an optional prompt.]

## Skill Version(s):

1.0.1 (source: package.json and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
