## Description: <br>
Dlazy Slideshow Video uses the pinned dLazy CLI to turn slides or documents into narrated slideshow-style videos with voiceover and transitions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content teams use this skill to create explainer, report, courseware, or training videos from slides, PDFs, and other documents through dLazy's hosted file-to-video workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and attached files are sent to dLazy as a third-party service. <br>
Mitigation: Use the skill only when organizational policy allows uploading that content to dLazy, and avoid attaching sensitive files unless approved. <br>
Risk: The dLazy API key grants access to the user's dLazy organization. <br>
Mitigation: Store the key through the dLazy CLI, and rotate or revoke it when access is no longer needed. <br>


## Reference(s): <br>
- [Dlazy Slideshow Video on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and streamed CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the pinned @dlazy/cli 1.2.3 package and may upload user-selected local files to dLazy for project-scoped video generation.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
