## Description:

AI 3D Printing Toy Generator Toy Multi View Sheets and 3D Models Generator using SOTA 3D APIs such as Tripo/Meshy/etc served on OneKey Agent Gateway by Craftsman Agent, useful for AI Figurine, Stuffed Toy, 3D Printing, Game Asset and Architecture Toy Generation

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to guide agents through remote Craftsman/OneKey toy-generation APIs that create toy design drafts, multi-view reference sheets, 3D generation tasks, progress polling, model links, and preview links from text prompts or image references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, uploaded image URLs, and generated assets are processed by remote OneKey/Craftsman services.

Mitigation: Do not submit confidential prompts, private images, or sensitive reference material unless remote processing is intended and authorized.

Risk: Returned workspace, model, and preview links may expose generated assets or task details to anyone with access to the links.

Mitigation: Share returned URLs only with intended recipients and treat private share links as sensitive.

Risk: The skill requires a OneKey Gateway access key for API calls.

Mitigation: Provide the key through the documented environment variable and avoid embedding credentials directly in shared prompts, scripts, or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ai-hub-admin/skills/3d-printing-generator)
- [Craftsman 3D Generator](https://craftsman-agent.aiagenta2z.com/app/3d-generator)
- [Craftsman website](https://craftsman-agent.aiagenta2z.com)
- [OneKey Agent Gateway endpoint](https://agent.deepnlp.org/agent_router)
- [OneKey access keys](https://deepnlp.org/workspace/keys)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with REST and CLI command examples plus JSON request and response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Remote API responses may include workspace share URLs, generated image URLs, task IDs, progress status, downloadable GLB model URLs, preview image URLs, generation metadata, and credit usage.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
