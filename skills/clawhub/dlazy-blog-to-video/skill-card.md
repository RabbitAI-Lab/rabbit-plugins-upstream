## Description: <br>
Dlazy Blog To Video helps agents invoke the dLazy file-to-video SaaS workflow to turn blog posts or other documents into narrated videos with storyboard, voiceover, and build steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents can use this skill to start or continue dLazy file-to-video projects for converting blog posts, articles, and documents into narrated videos for social, YouTube, training, courseware, or report-broadcast use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill advertises blog-to-video but routes agents through a broader file/document-to-video SaaS workflow. <br>
Mitigation: Treat it as a general file-to-video wrapper and confirm the intended document or file scope before use. <br>
Risk: Prompts and explicitly attached files may be sent to dLazy API and file storage endpoints. <br>
Mitigation: Avoid submitting confidential documents unless the dLazy account, data handling terms, and storage behavior are acceptable. <br>
Risk: The workflow requires a dLazy API key that may be stored in local CLI configuration. <br>
Mitigation: Use account-scoped keys, keep the local config protected, and rotate or revoke the key when access changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy website](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and CLI guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to run pinned dLazy CLI commands, attach files, or continue an existing dLazy project.] <br>

## Skill Version(s): <br>
1.0.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
