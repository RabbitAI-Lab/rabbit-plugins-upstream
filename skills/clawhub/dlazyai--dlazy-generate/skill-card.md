## Description: <br>
A comprehensive generation skill that selects an appropriate dLazy CLI model to generate images, videos, or audio from user intent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route multimodal media-generation requests to dLazy CLI subcommands for image, video, audio, upscaling, segmentation, vectorization, lip-sync, music, and speech workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent API-key storage can leave dLazy credentials on shared systems. <br>
Mitigation: Prefer per-run DLAZY_API_KEY or npx usage on shared machines, and revoke or remove stored keys with dlazy logout when finished. <br>
Risk: Local files passed to image, video, or audio fields may be uploaded to dLazy-hosted services for processing. <br>
Mitigation: Review local file paths and file contents before passing them to dlazy commands. <br>
Risk: Broad activation terms may cause agents to invoke cloud media generation more often than intended. <br>
Mitigation: Install only when the agent is expected to use dLazy for cloud media generation and review planned commands before execution. <br>


## Reference(s): <br>
- [Dlazy Generate on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-generate) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with dlazy shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated media is returned as hosted URLs from dLazy services; local media paths passed to commands may be uploaded for processing.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
