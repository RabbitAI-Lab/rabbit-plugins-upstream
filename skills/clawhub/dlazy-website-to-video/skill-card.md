## Description: <br>
Dlazy Website To Video turns a supplied website URL into a promo, social ad, or product demo video by using the dLazy CLI to run the hosted website-to-video template. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and content teams use this skill when they have a website URL and want an agent to start or continue a dLazy website-to-video project for promo videos, social ads, or product demos. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends prompts, supplied URLs, and any attached files to the third-party dLazy SaaS endpoints described in the evidence. <br>
Mitigation: Install and use it only when that data transfer is acceptable for the user's content and organization policy. <br>
Risk: Authentication requires a dLazy API key that may be saved in the local CLI configuration. <br>
Mitigation: Use the documented login or environment-variable flow, protect the local config file, and rotate or revoke the key from the dLazy dashboard when needed. <br>
Risk: A persistent global CLI install changes the local toolchain. <br>
Mitigation: Use the pinned npx invocation when a non-persistent install is preferred. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and streamed CLI text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference dLazy project ids and uploaded file URLs returned through the third-party CLI.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
