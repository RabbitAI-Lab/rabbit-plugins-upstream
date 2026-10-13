## Description:

Turns a reference short-video transcript and structural breakdown into an original spoken-video script for the user's topic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and marketers use this skill to study the hook and pacing of a Douyin, Xiaohongshu, or TikTok video and draft a new spoken script for their own topic without copying its wording.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference links or share text are sent to LinkDigest for processing.

Mitigation: Share only reference material you are authorized to submit; omit sensitive information from share text.

Risk: Reading a video with an API key can consume metered credits.

Mitigation: Check expected usage and set a per-request credit limit before running paid reads.

Risk: Missing helper functions may cause some success or error paths to fail at runtime.

Mitigation: Test the included helper before relying on it, and review failures rather than assuming a complete result.

Risk: A rewritten script could reproduce protected wording from the reference video.

Mitigation: Reuse the structure, not the original lines, and review the final script for copied language.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest API key setup](https://linkdigest.dev/app/keys)
- [ClawHub skill release](https://clawhub.ai/jackchew7143/skills/linkdigest-script-rewrite)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown script with title options, timed sections, and a beat-by-beat comparison table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Distinguishes source material from new writing and flags unavailable source details.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
