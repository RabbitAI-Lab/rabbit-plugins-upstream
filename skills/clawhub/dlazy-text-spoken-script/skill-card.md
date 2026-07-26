## Description: <br>
Guides agents to generate high-contrast, resonant, story-driven short video spoken scripts using a seven-step structure for hooks, narrative, viewpoint, and punchline. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and agents use this skill to turn a persona, audience pain point, or topic into a short video spoken script with a colloquial rhythm, concrete story details, and a memorable closing line. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes an image-generation workflow that can install or run the dLazy CLI and execute terminal commands. <br>
Mitigation: Install or run the CLI only when the user intentionally wants dLazy image generation, and require explicit user confirmation before each command. <br>
Risk: dLazy login or API-key setup may store credentials in the local CLI configuration. <br>
Mitigation: Use scoped credentials where possible, protect local configuration files, and rotate or revoke API keys when no longer needed. <br>
Risk: Prompts and media paths used with the CLI may send prompt data or upload local media to dLazy services. <br>
Mitigation: Avoid sending confidential prompts or files unless the user has approved that data transfer. <br>


## Reference(s): <br>
- [Dlazy Text Spoken Script on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text script content with optional shell command and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary script output follows a seven-step spoken-script structure; bundled dLazy CLI image-generation steps require user confirmation before terminal execution.] <br>

## Skill Version(s): <br>
1.3.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
