## Description: <br>
Converts PDFs and other documents into explainer, report, courseware, or training videos by using the dLazy hosted sandbox agent to parse, outline, storyboard, voice, build, and validate the result. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content teams, educators, and business users can use this skill to start or continue dLazy file-to-video projects from PDFs and other documents. It is intended for document explainer videos, report broadcasts, courseware, and training video workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and attached documents are sent to dLazy API and media storage endpoints. <br>
Mitigation: Confirm the user is comfortable sending the content to dLazy before use, and avoid attaching sensitive documents unless that transfer is approved. <br>
Risk: The dLazy API key can be saved in the local CLI configuration. <br>
Mitigation: Use per-run DLAZY_API_KEY when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed. <br>
Risk: The skill installs or runs a pinned third-party npm CLI package. <br>
Mitigation: Review the pinned @dlazy/cli package and declared source before installing it in sensitive environments. <br>


## Reference(s): <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown instructions with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses project-scoped chat sessions and may attach local files through the dLazy CLI.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
