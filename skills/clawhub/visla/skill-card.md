## Description:

Creates AI-generated videos from text scripts, URLs, PPT/PDF documents, or AI-generated visuals (AIGC) using Visla.

This skill is ready for commercial/non-commercial use.

## Publisher:

[visla-admin](https://clawhub.ai/user/visla-admin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and operators use this skill to ask an agent to create Visla videos from scripts, URLs, documents, media, speech, ideas, or AIGC storyboard and motion-video workflows. It also supports account, avatar, voice, style, and project-status checks needed to configure and monitor video creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected scripts, URLs, documents, images, audio, and video files are sent to Visla for processing.

Mitigation: Use the skill only for content that may be processed under the user's Visla account terms, and avoid uploading confidential material unless those terms and internal policies allow it.

Risk: The skill requires Visla API credentials and can optionally read saved credentials from ~/.config/visla/.credentials.

Mitigation: Use dedicated Visla API credentials, avoid exposing secrets in responses, and deny saved-credential access when credentials should be supplied only through environment variables, CLI arguments, or direct input.

Risk: Local file inputs can include documents or media with sensitive content.

Mitigation: Process only files explicitly selected by the user; the artifact documents path traversal, system-directory, extension, and format checks before file reads or uploads.

## Reference(s):

- [Visla API](https://www.visla.us/visla-api)
- [ClawHub skill page](https://clawhub.ai/visla-admin/skills/visla)
- [ClawHub publisher profile](https://clawhub.ai/user/visla-admin)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with CLI commands, progress updates, project identifiers, status summaries, and download links when Visla returns them.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses VISLA_API_KEY and VISLA_API_SECRET credentials; video generation may run for several minutes and AIGC workflows can take longer.]

## Skill Version(s):

2.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
