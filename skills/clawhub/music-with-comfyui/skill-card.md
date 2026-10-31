## Description:

Generates music and audio from a prompt through a user-configured ComfyUI server running AceStep Audio 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

BSD 3-Clause

## Use Case:

ComfyUI users can create songs and instrumental tracks from a music description, with optional lyrics and style controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, lyrics, and any configured API key are sent to the selected ComfyUI endpoint.

Mitigation: Use an endpoint you trust and HTTPS for remote connections; avoid sending sensitive prompts or lyrics.

Risk: Generated audio may remain on the server when cleanup fails; cleanup attempts stop after three failures until the hint counter is reset.

Mitigation: Do not rely on automatic deletion for sensitive material. Review the server copy and reset purge_fail_hints as documented if cleanup attempts need re-arming.

Risk: Configuration bookkeeping can lose updates during concurrent runs.

Mitigation: Avoid concurrent runs that update the same configuration bookkeeping, or review the configuration afterward.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/sunshinejnjn/skills/music-with-comfyui)
- [AceStep ComfyUI nodes](https://github.com/AceStep/AceStep-ComfyUI)
- [ComfyUI purge-after-retrieval plugin](https://github.com/sunshinejnjn/comfyui-purge-after-retrieval)
- [Workflow attribution](references/attribution.md)
- [CLI language code reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Files, Guidance]

**Output Format:** [Generated MP3 audio, with title and lyrics when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional controls include duration, lyrics, language, tempo, style, and seed.]

## Skill Version(s):

0.4.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
