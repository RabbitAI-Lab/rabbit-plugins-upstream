## Description: <br>
A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict 'plan first, render later' flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, marketers, educators, and production teams use this skill to plan cinematic or narrative storyboards, confirm character and script gates, and generate storyboard images through the dLazy CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Storyboard prompts, parameters, and referenced media may be sent to dLazy cloud services for generation. <br>
Mitigation: Avoid sensitive content in prompts or uploaded files, and use this skill only when remote prompt and media processing is acceptable. <br>
Risk: The dLazy CLI stores an API key for authenticated generation workflows. <br>
Mitigation: Use npx for non-persistent CLI use when preferred, and rotate or revoke the stored dLazy API key if needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown with storyboard plans, prompts, confirmation gates, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces staged storyboard planning guidance and generation commands; generated image URLs are returned by the dLazy CLI.] <br>

## Skill Version(s): <br>
1.3.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
