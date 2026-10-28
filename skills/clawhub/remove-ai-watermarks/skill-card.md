## Description:

Removes and identifies AI watermarks and provenance marks in images and video the user generated or edited.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

Apache 2.0

## Use Case:

Content creators and developers use this skill to inspect AI provenance signals and, when authorized, remove AI watermark marks from images or video.

### Deployment Geography for Use:

Global; the skill documents restrictions in mainland China.

## Known Risks and Mitigations:

Risk: Uploading sensitive media to the hosted service may expose it under that service's data practices.

Mitigation: Review the service's privacy terms before uploading sensitive files; use local processing when appropriate.

Risk: Removing a local watermark or provenance signal can be misrepresented as proof that media is human-made, and does not erase server-side generation history.

Mitigation: Keep the original, report only observed signals, and do not present altered generated media as human-made.

Risk: Removing a mark from content the user is not authorized to change can infringe third-party rights, including paid-asset protections.

Mitigation: Process only content the user created or is allowed to edit; stop for stock, marketplace, classifieds, or protected paid-asset marks.

## Reference(s):

- [Project homepage](https://raiw.cc)
- [Source repository listed in skill metadata (provenance unavailable)](https://github.com/wiltodelta/remove-ai-watermarks)
- [ClawHub skill page](https://clawhub.ai/wiltodelta/skills/remove-ai-watermarks)
- [Command recipes](references/commands.md)
- [Install extras](references/install.md)

## Skill Output:

**Output Type(s):** [Analysis, Files, Shell commands, Guidance]

**Output Format:** [Text findings and image or video files written to a separate output path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source media by default; reports only results produced by commands run in the session.]

## Skill Version(s):

1.0.14 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
