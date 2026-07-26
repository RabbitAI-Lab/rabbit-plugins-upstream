## Description: <br>
Convert storyboard details into a video-generation pipeline that can be added to an OpenClaw canvas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content-production agents use this skill to turn storyboard context, dialogue, and video prompts into a canvas-ready generation pipeline for cloned audio, scene imagery, and videos. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill's stated storyboard purpose is narrower than its behavior around CLI use, credential storage, external service calls, and terminal generation commands. <br>
Mitigation: Install it only when dLazy cloud media generation is intended, and review each proposed terminal command before allowing generation. <br>
Risk: Prompts and selected local media can be uploaded to dLazy services, and an API key may be stored locally. <br>
Mitigation: Use appropriate input data for cloud processing, prefer npx or an environment variable for less persistent setup, and rotate or revoke API keys from the dLazy dashboard when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with JSON pipeline examples and CLI command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces canvas-ready JSON pipeline elements; may invoke dLazy CLI workflows and external dLazy API endpoints when generation is requested.] <br>

## Skill Version(s): <br>
1.2.3 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
