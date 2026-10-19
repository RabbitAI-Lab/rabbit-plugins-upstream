## Description:

Generates and edits images, creates videos, and turns images into 3D meshes using a user-configured ComfyUI server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images, animate images or text into video, and create 3D meshes through a ComfyUI server they configure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected source images are sent to the configured ComfyUI server.

Mitigation: Use the default local endpoint or a server you control; use HTTPS for remote servers and avoid sending sensitive inputs to untrusted hosts.

Risk: Generated media and metadata can remain on disk.

Mitigation: Review the configured output directory and remove stored outputs when they are no longer needed.

Risk: API credentials may be exposed if stored in configuration or shared insecurely.

Mitigation: Keep API keys in environment variables rather than committed configuration files or shared messages.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sunshinejnjn/skills/image-with-comfyui)
- [Setup and data privacy](README.md)
- [CLI reference](references/cli-reference.md)
- [Output delivery](references/delivery.md)
- [Workflow attribution](references/attribution.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with generated media attachments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images, videos, and 3D mesh files may be saved locally and delivered to the user.]

## Skill Version(s):

4.0.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
