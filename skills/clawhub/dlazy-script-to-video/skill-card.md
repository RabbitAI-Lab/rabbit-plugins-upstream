## Description: <br>
Dlazy Script To Video helps agents turn a script or scene breakdown into a storyboarded, shot-by-shot video workflow using the dLazy CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and creative teams use this skill when they want an agent to start or continue dLazy storyboard projects that convert scripts, screenplay material, or shot lists into multi-shot video plans and generated video assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends prompts and options to the external dLazy API. <br>
Mitigation: Review prompts for sensitive information before use and only run the skill with an approved dLazy account and API key. <br>
Risk: Files attached with --files are uploaded to dLazy media storage. <br>
Mitigation: Attach only files that are approved for upload to dLazy and omit private or regulated content unless the user has confirmed it is permitted. <br>
Risk: A global CLI install persists the dLazy package on the local system. <br>
Mitigation: Use the pinned npx invocation when a temporary, non-global execution path is preferred. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy website](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and CLI guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May stream responses from the dLazy CLI and may reference uploaded user-provided files when the user explicitly attaches files.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
