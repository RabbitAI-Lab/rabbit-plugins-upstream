## Description: <br>
Generates detailed short-video storyboard scripts from user-provided themes, structured copy, or outlines while preserving supplied spoken copy word for word. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and production teams use this skill to turn structured short-video copy into shot-by-shot storyboard scripts with scene, camera, lighting, and spoken-script guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is framed as text-only storyboard generation but includes instructions to install and run a cloud media-generation CLI. <br>
Mitigation: Use it only when cloud dLazy generation is intended, review the npm package and CLI behavior before installation, and require explicit confirmation before running any dlazy command. <br>
Risk: Prompts, copy, and referenced local media paths may be sent to dLazy cloud endpoints during CLI use. <br>
Mitigation: Avoid sensitive copy and private local media paths unless the user has approved cloud processing for that material. <br>
Risk: The CLI stores API-key configuration locally. <br>
Mitigation: Review API-key storage behavior, protect the local configuration file, and rotate or revoke keys when access is no longer needed. <br>


## Reference(s): <br>
- [Dlazy Text Storyboard Script on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script) <br>
- [dLazy CLI Source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown storyboard with video parameters and repeated shot sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes aspect ratio, resolution, calculated dimensions, paragraph function, scene, camera movement, notes, shooting technique, and spoken script.] <br>

## Skill Version(s): <br>
1.2.3 (source: evidence release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
