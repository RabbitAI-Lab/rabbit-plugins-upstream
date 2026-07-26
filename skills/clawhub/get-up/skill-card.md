## Description: <br>
Sends fixed Haocun dancing and selfie image links through OpenClaw messaging channels in response to prompts about dancing, selfies, photos, or current status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qidu](https://clawhub.ai/user/qidu) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and OpenClaw developers use this skill to let an OpenClaw agent select fixed CDN-hosted dance or selfie media from a user prompt and send it through configured messaging channels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer can overwrite or append persistent OpenClaw identity and persona files. <br>
Mitigation: Back up IDENTITY.md and SOUL.md before installation and review any persona text before accepting changes. <br>
Risk: The skill can send images through connected messaging accounts. <br>
Mitigation: Require explicit confirmation of the destination channel, recipient, caption, and media URL before any message is sent. <br>
Risk: Broad trigger phrases can activate selfie or image-sending behavior in ordinary conversation. <br>
Mitigation: Narrow trigger patterns, keep the skill disabled unless needed, or require a dedicated command phrase. <br>
Risk: The skill sends fixed CDN-hosted images as persona or selfie media. <br>
Mitigation: Review media rights, consent, and labeling before use, especially in external or customer-facing messaging. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qidu/skills/get-up) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>
- [Clawra reference site](https://clawra.dev/) <br>
- [CDN media asset root](https://cdn.jsdelivr.net/gh/christoagent/haoclaw@main/assets/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples, configuration snippets, and JSON-style helper script output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The helper script reports the selected media URL, channel, and prompt after sending.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata, manifest.json, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
