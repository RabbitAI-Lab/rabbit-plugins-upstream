## Description: <br>
Clone voice and generate new text reading audio with one click using Vidu Audio Clone. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to call dLazy's hosted Vidu Audio Clone service to clone a voice from reference audio and generate spoken audio for new text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist a dLazy API key locally, and the scan did not substantiate the claim that the saved key is restricted to only the current OS user. <br>
Mitigation: Review the dLazy CLI before installing; prefer per-invocation DLAZY_API_KEY or npx when persistent credentials are not needed; check ~/.dlazy/config.json permissions and rotate or revoke any exposed key. <br>
Risk: Voice cloning requests can upload reference audio and prompts to dLazy-hosted endpoints. <br>
Mitigation: Use only audio the user is allowed to upload for voice cloning, and disclose that inputs and generated outputs are handled by dLazy hosted services. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files] <br>
**Output Format:** [JSON result containing generated output URLs or asynchronous task status] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May upload referenced audio to dLazy media storage and return hosted files.dlazy.com URLs; --no-wait returns a generateId for polling.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
