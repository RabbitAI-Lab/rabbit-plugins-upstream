## Description: <br>
Generates videos by selecting an appropriate dLazy CLI video model for text, image, first/last-frame, digital human, and lip-sync requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to choose and run dLazy video-generation CLI commands for text-to-video, image-to-video, first/last-frame video, digital human, segmentation, and lip-sync workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys may be stored in the local dLazy CLI config, and the security evidence notes that local storage protections may be weaker than the skill text claims. <br>
Mitigation: Prefer per-invocation DLAZY_API_KEY use when persistent storage is not desired, or manually restrict permissions on ~/.dlazy/config.json. <br>
Risk: Prompts, parameters, and local media files passed to image, video, or audio fields are sent to dLazy cloud endpoints. <br>
Mitigation: Only pass files and prompts intended for upload to dLazy's cloud service. <br>
Risk: The security verdict is suspicious despite no listed risk findings. <br>
Mitigation: Review the skill and dLazy CLI before installation; use the pinned npx command when avoiding persistent global installs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-generate) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The selected dLazy CLI commands may return JSON envelopes and hosted media URLs.] <br>

## Skill Version(s): <br>
1.4.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
