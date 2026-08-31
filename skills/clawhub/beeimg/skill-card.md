## Description:

Free image hosting with albums, privacy controls, and API access. Upload images by URL or file, organize into albums with folders, set privacy levels, and manage your hosted images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beeimg](https://clawhub.ai/user/beeimg)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to upload images to BeeIMG, organize hosted images into albums or folders, adjust privacy settings, and manage hosted image records through API-backed commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The BeeIMG API key can upload images, manage albums, change privacy settings, and delete hosted images.

Mitigation: Use BEEIMG_API_KEY from the environment and review the intended upload, album, privacy, or deletion action before execution.

Risk: Deletion can remove a hosted image when the image ID and delete key are correct.

Mitigation: Confirm the exact image ID and delete key before proposing or running any deletion.

Risk: Uploads and albums may be public by default if no privacy setting is supplied.

Mitigation: Confirm the desired privacy setting before upload or album creation when visibility matters.

## Reference(s):

- [BeeIMG Homepage](https://beeimg.com)
- [BeeIMG API Key Page](https://beeimg.com/api/newkey)
- [BeeIMG MCP Server](https://beeimg.com/mcp)
- [ClawHub Beeimg Skill Page](https://clawhub.ai/beeimg/skills/beeimg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with curl command examples and JSON response snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include BeeIMG API endpoints, privacy options, album or image identifiers, and deletion keys when relevant.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
