## Description:

Helps agents create AI-generated images, video, audio, and 3D assets and manage WorkRally projects, shots, materials, and collaborative canvases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-adm](https://clawhub.ai/user/tencent-adm)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent through media generation, production planning, file uploads, and asset and canvas management in WorkRally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials grant access to WorkRally content.

Mitigation: Install the WorkRally CLI only if trusted, use a scoped API key where possible, and protect the credentials directory.

Risk: Uploading local files shares their contents with a remote service.

Mitigation: Obtain explicit user confirmation before uploading files.

Risk: Deleting materials or overwriting shared canvases can affect collaborators.

Mitigation: Obtain explicit user confirmation before deleting, clearing, or overwriting remote content.

## Reference(s):

- [WorkRally on ClawHub](https://clawhub.ai/tencent-adm/skills/workrally)
- [WorkRally](https://workrally.qq.com)
- [AI generation guide](references/ai-generation-guide.md)
- [Shotlist guide](references/shotlist-guide.md)
- [Canvas guide](references/canvas-guide.md)
- [Upload and assets guide](references/upload-and-assets-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Media asset links]

**Output Format:** [Markdown guidance with CLI commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media and edited projects reside in the user's WorkRally account.]

## Skill Version(s):

2.10.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
