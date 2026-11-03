## Description:

Generates music from a text description and optional lyrics through a user-configured ComfyUI server using AceStep Audio 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

BSD 3-Clause

## Use Case:

External users and developers can generate a song or instrumental track from a music description, with optional lyrics and style settings, using an existing ComfyUI server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Music prompts, lyrics, and an optional API key are sent to the configured ComfyUI server.

Mitigation: Use a server you trust, use HTTPS for remote connections, and avoid sending sensitive content.

Risk: Remote deletion of the generated audio is best effort and may fail if the server lacks cleanup support.

Mitigation: Tell the user that remote cleanup is attempted, verify the server cleanup plugin before relying on deletion, and honor the user's keep setting.

## Reference(s):

- [AceStep Audio 1.5 model](https://huggingface.co/AceStep/AceStep1.5)
- [CLI Usage Reference](references/cli-reference.md)
- [Image-First Reference](references/image-first.md)
- [Workflow Source Attribution](references/attribution.md)
- [ComfyUI purge-after-retrieval plugin](https://github.com/sunshinejnjn/comfyui-purge-after-retrieval)

## Skill Output:

**Output Type(s):** [Audio files, Configuration instructions]

**Output Format:** [Generated MP3 audio file with command-line configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The audio file is saved under the configured output directory; generation uses the selected ComfyUI server.]

## Skill Version(s):

0.4.13 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
