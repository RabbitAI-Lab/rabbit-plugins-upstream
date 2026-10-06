## Description:

Extracts the spoken transcript and structure of a user-supplied Douyin, Xiaohongshu, or TikTok video, then drafts an original script for the user's topic using a similar structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and marketing teams use a reference video to identify its spoken script and pacing, then create an original voiceover script for their own topic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the service requires a LinkDigest API key and sends the reference video link or share text to linkdigest.dev; credit charges may apply.

Mitigation: Use only links you are comfortable sharing, keep the key private, and review the credit cost before requesting a digest.

Risk: Private or login-only videos may not be accessible.

Mitigation: Provide an accessible public video rather than private or login-only content.

Risk: A structural rewrite may still resemble the source too closely.

Mitigation: Review the draft for originality and replace any copied wording before publication.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown with timestamped script segments and a structure comparison table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes title and cover-text suggestions, missing-information caveats, and a distinction between source material, analysis, and new writing.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
