## Description: <br>
Image generation skill that selects an appropriate dLazy CLI image model based on the prompt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to generate, edit, upscale, vectorize, or segment images through the dLazy CLI and hosted image-generation APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and local media inputs may be sent to dLazy API and file-hosting endpoints. <br>
Mitigation: Use only approved content, avoid sensitive inputs unless dLazy is approved for that data, and review dLazy service terms before use. <br>
Risk: The dLazy CLI can store an API key in the local user configuration. <br>
Mitigation: Use the DLAZY_API_KEY environment variable for per-command authentication when persistence is not desired, and rotate or revoke keys from the dLazy dashboard if exposure is suspected. <br>
Risk: Image-generation requests may consume dLazy credits. <br>
Mitigation: Confirm account authorization and available credits before running large or repeated generation jobs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy service](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files] <br>
**Output Format:** [Markdown guidance with dlazy CLI commands and JSON command output URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce hosted media URLs on files.dlazy.com and may upload local media files when supplied as inputs.] <br>

## Skill Version(s): <br>
1.3.5 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
