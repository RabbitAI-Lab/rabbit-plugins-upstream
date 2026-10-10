## Description:

Generates original music from a style description and optional lyrics using a user-configured ComfyUI server running AceStep Audio 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

BSD-3-Clause

## Use Case:

People creating original songs or instrumental tracks use this skill to turn a description, optional lyrics, or an image-inspired mood into audio through their own ComfyUI server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Music descriptions, lyrics, and workflow data are sent to the configured ComfyUI endpoint; generated audio is saved to disk.

Mitigation: Use a local or trusted server and trusted output storage; avoid sensitive prompts or lyrics when either is untrusted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sunshinejnjn/skills/music-with-comfyui)
- [AceStep 1.5 model](https://huggingface.co/AceStep/AceStep1.5)
- [AceStep ComfyUI nodes](https://github.com/AceStep/AceStep-ComfyUI)
- [CLI usage reference](references/cli-reference.md)
- [Workflow attribution](references/attribution.md)

## Skill Output:

**Output Type(s):** [Audio files, Text]

**Output Format:** [Generated audio file with a brief delivery message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio is saved locally; format depends on the server and delivery channel.]

## Skill Version(s):

0.3.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
