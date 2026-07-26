## Description: <br>
Fast image generation with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to generate images through the dLazy hosted Seedream 5.0 Lite API from text prompts or reference images. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and local image inputs are sent to dLazy cloud services for generation. <br>
Mitigation: Avoid submitting confidential or restricted content unless the user has approved dLazy as a provider for that data. <br>
Risk: The dLazy CLI may store an API key in a local config file. <br>
Mitigation: Use the per-invocation DLAZY_API_KEY environment variable or verify config-file permissions on shared machines. <br>
Risk: Generated assets are hosted by dLazy and returned as external URLs. <br>
Mitigation: Review generated output links before sharing them outside the intended workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite) <br>
- [dLazy Homepage](https://dlazy.com) <br>
- [dLazy CLI Source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated image results are returned as dLazy-hosted URLs; async runs may return a task identifier for later polling.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
