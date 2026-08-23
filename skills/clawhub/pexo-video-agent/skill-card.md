## Description:

Pexo Video Agent helps an agent create finished 5-120 second multi-shot videos from text, images, URLs, scripts, or audio through Pexo's external video generation service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pexo](https://clawhub.ai/user/pexo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn natural-language video requests and approved media assets into product ads, social clips, explainer videos, brand videos, and revisions managed through Pexo projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Briefs, selected files, and related metadata are sent to Pexo for video generation.

Mitigation: Obtain explicit user consent before the first transmission, upload only user-approved assets, and exclude secrets, regulated data, and unrelated local files.

Risk: The skill requires a Pexo API key for authenticated requests.

Mitigation: Store PEXO_API_KEY only in an owner-readable config file or trusted environment variable, avoid exposing it in chat or logs, and rotate it if it may have been shared.

Risk: Video generation can consume paid credits.

Mitigation: Show the available estimate and run billing confirmation only after explicit user approval; the bundled confirmation script requires the --user-approved flag.

Risk: Remote media URLs or local files could include inappropriate, private, or unsupported inputs.

Mitigation: Use only public HTTPS URLs with approval, ask users to upload private or signed assets directly, and avoid searching the local filesystem for extra material.

## Reference(s):

- [Pexo Video Agent on ClawHub](https://clawhub.ai/pexo/skills/pexo-video-agent)
- [Pexo OpenClaw Guide](https://pexo.ai/connect/openclaw)
- [Setup Checklist](references/SETUP-CHECKLIST.md)
- [Troubleshooting](references/TROUBLESHOOTING.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated videos are returned as download URLs and local files when asset retrieval succeeds.]

## Skill Version(s):

0.3.16 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
