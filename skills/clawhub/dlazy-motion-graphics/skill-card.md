## Description: <br>
Creates code-driven motion graphics such as kinetic typography, animated text videos, animated infographics, explainers, logos, and transitions using Remotion code through the dLazy hosted sandbox agent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, designers, and content teams use this skill to start or continue dLazy motion-graphics projects that produce code-driven animated graphics rather than AI-generated footage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, options, and attached files are sent to dLazy hosted services. <br>
Mitigation: Use the skill only with content that is appropriate for dLazy's hosted service, and avoid attaching sensitive local files unless that transfer is acceptable. <br>
Risk: The dLazy API key may be stored locally in the user configuration file. <br>
Mitigation: Prefer the per-invocation DLAZY_API_KEY environment variable when persistent credentials are not desired, check permissions on ~/.dlazy/config.json after login or auth set, and rotate or revoke keys from the dLazy dashboard if exposure is suspected. <br>


## Reference(s): <br>
- [Dlazy Motion Graphics on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-motion-graphics) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy website](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and code-oriented guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires dLazy API authentication; attached local files are uploaded to dLazy storage before use.] <br>

## Skill Version(s): <br>
1.3.5 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
