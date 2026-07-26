## Description: <br>
Converts PPT, Word, Excel, PDF, and other documents into explainer, report, courseware, or training videos through dLazy's hosted file-to-video agent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent to run dLazy's file-to-video workflow, upload selected documents, and continue project-scoped video generation sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, project context, and attached files are sent to dLazy's hosted service. <br>
Mitigation: Use only with documents approved for that service and avoid uploading confidential files unless the organization has approved dLazy. <br>
Risk: The dLazy API key may be stored in the local CLI configuration. <br>
Mitigation: Protect the local config file and rotate or revoke the API key from the dLazy dashboard when access changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video) <br>
- [dLazy CLI repository](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and streamed CLI responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference dLazy project IDs and user-selected local files uploaded through the dLazy CLI.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
