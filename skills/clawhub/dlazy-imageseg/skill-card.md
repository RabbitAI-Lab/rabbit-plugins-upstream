## Description: <br>
Image matting tool that separates foreground from background and returns a transparent-background image URL for product image processing, character cutout, and composition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to call the dLazy image segmentation CLI for background removal and receive hosted transparent PNG output URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected local media may be uploaded to dLazy's hosted service for processing. <br>
Mitigation: Use the skill only with media that is approved for remote processing, and avoid passing private files unless that upload is intended. <br>
Risk: The dLazy API key may be stored in the local CLI configuration. <br>
Mitigation: Prefer DLAZY_API_KEY for temporary use when appropriate, and rotate or revoke the key if it may have been exposed. <br>
Risk: The skill depends on the external dLazy CLI and hosted API availability. <br>
Mitigation: Review the pinned CLI package before installation and use dry-run or async polling options where they fit the workflow. <br>


## Reference(s): <br>
- [Dlazy Imageseg on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-imageseg) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI returns hosted image URLs, and async mode can return a task identifier for polling.] <br>

## Skill Version(s): <br>
1.3.5 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
