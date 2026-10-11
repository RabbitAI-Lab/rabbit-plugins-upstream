## Description:

Guides agents to clone a custom voice from an authorized audio sample using dLazy's Qwen3-TTS voice-cloning command.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other voice-application creators use this skill to submit authorized voice samples for cloning and use the resulting custom voice in later text-to-speech requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloning a voice without the speaker's permission could enable impersonation.

Mitigation: Use only samples you own or are explicitly authorized to clone.

Risk: Local voice samples may be uploaded to dLazy-hosted services.

Mitigation: Review the sample and service terms before submission; avoid sharing sensitive or unauthorized recordings.

Risk: Saved API keys persist locally, and the documented example command and output appear inconsistent with voice cloning.

Mitigation: Use a per-run DLAZY_API_KEY when persistence is unwanted and verify the current CLI help and returned output before relying on examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package listed in skill metadata](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text]

**Output Format:** [Markdown with shell commands and JSON result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides use of a returned custom voice in subsequent text-to-speech calls; confirm the actual CLI output.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
