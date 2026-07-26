## Description: <br>
ByteDance's Seedance 2.0 video generation skill supports text-to-video, first/last-frame generation, and multi-modal image, video, and audio references through the dLazy CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to generate videos with ByteDance Seedance 2.0 through dLazy's hosted API, using prompts plus optional image, video, audio, or first/last-frame inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected media files are sent to dLazy's cloud service for generation. <br>
Mitigation: Review prompts and media for sensitive content before use, and avoid submitting data that should not leave the user's environment. <br>
Risk: Using dlazy login stores an API key in the local dLazy configuration file. <br>
Mitigation: Use DLAZY_API_KEY for temporary sessions when persistent credentials are not desired, and rotate or revoke keys from the dLazy dashboard if exposure is suspected. <br>


## Reference(s): <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [Dlazy Seedance 2.0 on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [CLI command guidance and JSON responses containing generated media URLs or asynchronous task status] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include hosted media URLs from files.dlazy.com or a generateId for later polling.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
