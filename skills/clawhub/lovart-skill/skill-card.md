## Description:

Lovart API lets agents generate images, videos, audio, music, and design assets through Lovart AI while managing Lovart projects, conversation threads, uploads, downloads, and generation settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lovart-admin](https://clawhub.ai/user/lovart-admin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to send creative generation requests to Lovart AI, retrieve generated media files, and continue work across Lovart projects and conversation threads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local files may be sent to Lovart for generation or upload.

Mitigation: Review prompts and file paths before use, and avoid sending confidential or regulated data unless approved.

Risk: The skill stores project and thread history locally and may reuse recent Lovart threads by default.

Mitigation: Inspect local Lovart configuration and thread state before sensitive work, and switch or remove threads when context reuse is not desired.

Risk: TLS verification can be disabled with LOVART_INSECURE_SSL, increasing exposure to intercepted traffic.

Mitigation: Keep TLS verification enabled and avoid setting LOVART_INSECURE_SSL except in reviewed, controlled environments.

Risk: Upload and download commands can move data between local paths, Lovart services, and generated artifact URLs.

Mitigation: Use trusted paths and URLs only, and scan downloaded artifacts before opening or redistributing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lovart-admin/skills/lovart-skill)
- [Lovart project canvas](https://www.lovart.ai/canvas?projectId={project_id})

## Skill Output:

**Output Type(s):** [Text, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown status messages with JSON command output and downloaded media file attachments.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LOVART_ACCESS_KEY and LOVART_SECRET_KEY; may store project and thread history under ~/.lovart and download generated files to /tmp/lovart.]

## Skill Version(s):

1.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
