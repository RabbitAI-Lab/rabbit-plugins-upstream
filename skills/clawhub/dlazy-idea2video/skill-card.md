## Description: <br>
Turns a user's idea into a video-generation workflow plan covering story, characters, scenes, shots, keyframes, shot videos, and final concatenation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative users use this skill to turn a video idea into a staged production plan, canvas-ready workflow shapes, and dLazy CLI generation steps. It is intended for agent-assisted media planning and generation with explicit user confirmation before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill combines canvas-planning guidance with mandatory terminal-based generation, which may exceed what a user expects from a planning workflow. <br>
Mitigation: Require explicit confirmation before running generation commands and keep each proposed command visible for review. <br>
Risk: Prompts and referenced media may be sent to dLazy API services and uploaded to dLazy media storage. <br>
Mitigation: Use the skill only with inputs suitable for dLazy services, avoid sensitive media, and review uploaded inputs before approving commands. <br>
Risk: Using a globally installed CLI may persist tooling and API configuration on the local system. <br>
Mitigation: Prefer the pinned npx invocation when a global install is not desired, and rotate or revoke dLazy API keys from the dLazy dashboard when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-idea2video) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy website](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with inline shell commands, workflow configuration details, and generated media URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create canvas workflow shapes and propose or run dLazy CLI commands after user confirmation.] <br>

## Skill Version(s): <br>
1.3.9 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
