## Description: <br>
4MP high-resolution raster image generation for print-ready assets and large-scale use. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative users invoke this skill to generate high-resolution raster images through the dLazy hosted Recraft V4 Pro service. It is suitable for creating print-ready visual assets and large-format imagery from prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a third-party CLI and hosted image-generation service. <br>
Mitigation: Verify that the dLazy CLI package and service are trusted before installing or invoking the skill. <br>
Risk: API keys may be stored in a local CLI configuration file when using persistent login. <br>
Mitigation: Use DLAZY_API_KEY for per-invocation authentication on shared or untrusted machines, and rotate or revoke keys from the dLazy dashboard when needed. <br>
Risk: Local media paths supplied to the CLI may be uploaded to dLazy-hosted storage. <br>
Mitigation: Only pass files that are appropriate to upload to the third-party service. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro) <br>
- [dLazy CLI Source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy Homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Images, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON responses containing generated image URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated image outputs are returned as dLazy-hosted URLs; asynchronous requests may return a task identifier for later polling.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
