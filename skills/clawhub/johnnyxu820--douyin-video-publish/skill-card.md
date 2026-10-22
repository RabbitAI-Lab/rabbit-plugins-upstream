## Description:

Automates publishing videos to Douyin Creator Center, including upload, title, hashtags, cover, location selection, publishing, and post-publish verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnnyxu820](https://clawhub.ai/user/johnnyxu820)

### License/Terms of Use:


## Use Case:

External creators or operators use this skill to publish prepared video files to a logged-in Douyin creator account through a browser workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish live Douyin posts through a logged-in creator account.

Mitigation: Require the agent to show the exact account, video file, title, hashtags, cover, and location, and only approve publishing after those details are correct.

Risk: The workflow automatically adds the fixed location 'Suzhou Center', which may be inaccurate for the content.

Mitigation: Remove or override the fixed location unless the user explicitly wants that location attached to the post.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/johnnyxu820/skills/douyin-video-publish)
- [Douyin Creator Center video publishing page](https://creator.douyin.com/creator-micro/content/post/video?enter_from=publish_page)
- [Douyin Creator Center content management page](https://creator.douyin.com/creator-micro/content/manage)

## Skill Output:

**Output Type(s):** [guidance, browser automation actions, configuration]

**Output Format:** [Markdown instructions and interactive browser workflow steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operates in an authenticated Douyin creator browser session and can publish live content.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
