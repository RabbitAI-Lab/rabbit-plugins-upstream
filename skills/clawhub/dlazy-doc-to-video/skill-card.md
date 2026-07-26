## Description: <br>
Turns Doc, Word, Markdown, PPT, Excel, and PDF documents into explainer, report, courseware, or training videos by driving the dLazy file-to-video agent workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content teams use this skill to ask the hosted dLazy file-to-video agent to parse source documents, create outlines and storyboards, generate voiceover, build videos, and validate the result. It supports new project creation and continued project work through the dLazy CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and attached documents are sent to dLazy, and attached local files can be uploaded to dLazy media storage. <br>
Mitigation: Confirm before sharing confidential files and install only when sending the relevant content to dLazy is acceptable. <br>
Risk: The dLazy API key can be stored in local CLI configuration. <br>
Mitigation: Use DLAZY_API_KEY per invocation when persistence is not desired, and rotate or revoke the key when access is no longer needed. <br>
Risk: The skill depends on a pinned external CLI and hosted SaaS endpoints. <br>
Mitigation: Review the pinned CLI/source and the dLazy service terms before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video) <br>
- [dLazy CLI source link from metadata](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Text] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke the dLazy CLI, stream agent responses, and upload attached local files to dLazy media storage.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
