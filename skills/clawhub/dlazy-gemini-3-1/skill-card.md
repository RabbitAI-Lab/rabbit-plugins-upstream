## Description: <br>
Google's multimodal model with strong long-context and vision understanding for document parsing, image/video understanding, and structured output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to call dLazy's hosted Gemini 3.1 wrapper for multimodal prompting, including text prompts and selected image or video inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected local media files are sent to dLazy cloud endpoints for inference. <br>
Mitigation: Review inputs before invocation and avoid sending sensitive prompts, images, videos, or file paths unless dLazy is approved for that data. <br>
Risk: The CLI can persist an API key in local user configuration. <br>
Mitigation: Use the per-invocation DLAZY_API_KEY option when key persistence is not desired, and rotate or revoke organization keys as needed. <br>
Risk: Documentation contains a minor version inconsistency for the referenced @dlazy/cli package. <br>
Mitigation: Verify the intended @dlazy/cli version before installing or running the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-3-1) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy website](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON responses from the dLazy CLI with optional Markdown guidance from the agent] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return asynchronous task identifiers when no-wait mode is used.] <br>

## Skill Version(s): <br>
1.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
