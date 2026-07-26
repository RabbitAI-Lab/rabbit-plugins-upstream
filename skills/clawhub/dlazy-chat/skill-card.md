## Description: <br>
Chat with the dlazy sandbox agent, a project-scoped assistant that runs skills end-to-end over multiple turns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to start or continue project-scoped conversations with dLazy's hosted sandbox agent, discover available skills and projects, and run multi-turn work through the dlazy CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger words could route ordinary chat or attached files to dLazy unintentionally. <br>
Mitigation: Use explicit requests such as 'use dlazy chat' and review attached files before invocation. <br>
Risk: Prompts and files passed with --files are sent to dLazy's hosted API and media storage. <br>
Mitigation: Avoid attaching sensitive files unless use of the dLazy hosted service is acceptable for that data. <br>
Risk: The CLI may store a dLazy API key in the local user configuration. <br>
Mitigation: Use npx for on-demand execution when preferred, and rotate or revoke stored API keys when access should change. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-chat) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or terminal text with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Streams replies through the dlazy CLI; local files attached with --files are uploaded before use.] <br>

## Skill Version(s): <br>
1.2.8 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
