## Description:

Meitu Skills is an agent skill library for Meitu OpenAPI that enables AI agents to generate and edit posters, stickers, videos, product images, audio, and related creative assets through scene-specific workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[meituskills](https://clawhub.ai/user/meituskills)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use Meitu Skills to route creative media requests to specialized Meitu workflows for image editing, poster and product image generation, sticker creation, video generation and editing, audio generation, and related asset preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meitu API credentials may be available to the CLI through environment variables or a local credentials file.

Mitigation: Prefer environment variables in shared environments, restrict any local credentials file, and avoid committing credentials.

Risk: User media, prompts, and selected context summaries may be sent to Meitu OpenAPI for processing.

Mitigation: Avoid sensitive portraits, documents, or private context unless the user explicitly accepts remote processing for the task.

Risk: Visual memory and profile files may be created, updated, or reused for personalization.

Mitigation: Review or disable local visual memory and profile files when long-lived personalization is not desired.

## Reference(s):

- [ClawHub Release Page](https://clawhub.ai/meituskills/skills/meitu-skills)
- [README](README.md)
- [Security Model](SECURITY.md)
- [Meitu Tools Command Catalog](meitu-tools/references/tools.yaml)
- [Routing Guide](references/routing-guide.md)
- [Task ID Baseline](references/task-id-baseline.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style responses with shell commands, local file paths, generated media URLs, and user-facing guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require Meitu API credentials and can create or update local output, project, visual memory, and profile files depending on the selected workflow.]

## Skill Version(s):

2.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
