## Description:

Publishes Markdown to a user-configured S3-compatible bucket and returns a shareable web page link on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users publish selected Markdown documents to their own S3-compatible bucket when they want to share a browser-viewable page instead of pasting the document into chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Published Markdown is publicly accessible and may expose sensitive content.

Mitigation: Publish only on explicit request; review documents and remove secrets and personal information before upload.

Risk: Bucket credentials are stored in plaintext in ~/.md-web/config.json.

Mitigation: Protect the configuration file and use a dedicated bucket with the least-privilege object token practical.

Risk: Setting expire_days to 0 can clear existing bucket lifecycle configuration.

Mitigation: Use a dedicated bucket and avoid expire_days: 0 unless clearing lifecycle rules is intended.

Risk: The public viewer may share an origin with sensitive applications or cookies.

Mitigation: Host the viewer on a dedicated domain without sensitive cookies or other apps on the same origin.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/rockbenben/skills/md-web)
- [Skill homepage (OpenClaw metadata; not verified import provenance)](https://github.com/rockbenben/aishort-skills/tree/main/skills/md-web)

## Skill Output:

**Output Type(s):** [Text, Web page link]

**Output Format:** [Markdown link to a publicly accessible web page]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uploads Markdown to the user's S3-compatible bucket; relative local images are not uploaded.]

## Skill Version(s):

1.1.4 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
