## Description: <br>
Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative production teams use this skill to convert user-selected raster image assets into scalable vector output through the dLazy CLI and hosted service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-selected images may be uploaded to dLazy's hosted service and returned as hosted files. <br>
Mitigation: Use the skill only with images appropriate for third-party processing and review service terms before sending sensitive assets. <br>
Risk: The CLI uses an API key saved in local user configuration or supplied through DLAZY_API_KEY. <br>
Mitigation: Use per-invocation environment variables when persistent local credentials are not desired, and rotate or revoke keys when access is no longer needed. <br>
Risk: A global CLI install persists a third-party binary on the system. <br>
Mitigation: Use the pinned npx invocation when a non-persistent install path is preferred. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize) <br>
- [dLazy CLI Source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy Homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Files, Configuration instructions] <br>
**Output Format:** [JSON response with hosted output URL; optional downloaded file when --save is used] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a dLazy API key; accepts an image URL or local image path and supports asynchronous task polling.] <br>

## Skill Version(s): <br>
1.2.5 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
