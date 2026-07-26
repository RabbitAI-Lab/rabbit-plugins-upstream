## Description: <br>
PixVerse C1 video model for text-to-video, image-to-video, first/last-frame video generation, and reference-image video generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to invoke dLazy's hosted PixVerse C1 video-generation service from an agent. It supports prompt-driven video generation and optional image inputs for reference, component, or first/last-frame workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and local media inputs are sent to dLazy's hosted API and media storage. <br>
Mitigation: Use only prompts and files appropriate for upload to dLazy's service; avoid passing local images or videos unless that data sharing is acceptable. <br>
Risk: The skill depends on installing or running a third-party npm CLI. <br>
Mitigation: Review the referenced npm package and source repository before global installation, and prefer the pinned npx command for one-off use. <br>
Risk: The broad video-generation trigger could route requests to this skill unintentionally. <br>
Mitigation: Use explicit trigger language such as "pixverse c1" when invoking the skill. <br>
Risk: API keys are stored in the local dLazy CLI configuration or supplied through the environment. <br>
Mitigation: Authenticate only on trusted machines and rotate or revoke keys from the dLazy dashboard when access changes. <br>


## Reference(s): <br>
- [Dlazy Pixverse C1 on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy website](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, JSON, guidance] <br>
**Output Format:** [Markdown instructions with bash command examples and JSON response examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Invoked CLI responses may include generated media URLs or asynchronous task status.] <br>

## Skill Version(s): <br>
1.2.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
