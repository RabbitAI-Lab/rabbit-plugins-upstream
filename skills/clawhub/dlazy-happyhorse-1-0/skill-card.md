## Description: <br>
Happy Horse 1.0 video model covers text-to-video, first-frame-to-video, reference-to-video, and video editing through the dLazy CLI and hosted API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to generate or edit video with Happy Horse 1.0 from prompts and optional image or video inputs. It is useful when an agent needs to call a cloud video-generation service and return generated media URLs or asynchronous task status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [JSON result payloads and Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses @dlazy/cli pinned to 1.2.3; prompts and selected parameters are sent to api.dlazy.com, and local media inputs may be uploaded to files.dlazy.com. Mitigate credential and upload risk by reviewing the pinned package/source, using npx or DLAZY_API_KEY for less persistent setup, passing only media suitable for upload, and rotating or revoking API keys from the dLazy dashboard when needed.] <br>

## Skill Version(s): <br>
1.3.4 (source: evidence.json release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
