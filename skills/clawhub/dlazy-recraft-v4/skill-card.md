## Description: <br>
1MP raster image generation with refined design judgment for everyday creative work and fast iteration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, designers, and creative users use this skill to generate 1MP raster images through the dLazy Recraft V4 hosted API from prompts and aspect-ratio parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a dLazy API key that may be saved in the local CLI configuration. <br>
Mitigation: Use DLAZY_API_KEY for temporary per-invocation authentication when local credential persistence is not desired, and rotate or revoke exposed keys from the dLazy dashboard. <br>
Risk: Prompts and local media paths supplied to the command are sent to dLazy API and media storage endpoints for generation. <br>
Mitigation: Only pass prompts and media files intended for upload to dLazy, and review the pinned @dlazy/cli package before installation or execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files, Guidance] <br>
**Output Format:** [JSON responses containing generated image URLs, plus shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated images are returned as hosted PNG URLs; asynchronous mode can return a task identifier for polling.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
