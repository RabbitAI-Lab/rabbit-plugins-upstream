## Description: <br>
Replicates a reference image or video by recreating its look and structure with the user's own subject, product, or characters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, creators, and developers use this skill to ask a dLazy-hosted agent to recreate the visual style, composition, and structure of supplied reference images or videos using their own content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and attached reference media are sent to dLazy services for processing. <br>
Mitigation: Install and use the skill only when sending that content to dLazy is acceptable for the task and data involved. <br>
Risk: The dLazy API key is saved in local CLI configuration and project sessions can retain task context. <br>
Mitigation: Use explicit new-project or continue-project commands, clear sessions when switching tasks, and rotate or revoke the API key if the local config or account is no longer trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference dLazy project IDs, authentication state, uploaded media, and streamed responses from the dLazy CLI.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
