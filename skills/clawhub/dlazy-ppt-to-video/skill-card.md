## Description: <br>
ppt to video, powerpoint to video, slides to video, presentation to video - parse the deck, outline, storyboard, voiceover, build, validate. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to convert PowerPoint, Keynote, and other documents into explainer, pitch, courseware, report, or training videos through the dLazy CLI and hosted service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Presentations, documents, prompts, and attached files are sent to dLazy API and file storage when the skill is used. <br>
Mitigation: Use the skill only when you explicitly want dLazy's hosted document-to-video service, and attach only files you are comfortable sending to dLazy. <br>
Risk: The dLazy organization API key may be stored locally for CLI authentication. <br>
Mitigation: Prefer per-invocation DLAZY_API_KEY for sensitive environments, check local config file permissions before saving a key, and rotate or revoke keys from the dLazy dashboard when needed. <br>
Risk: The required dLazy CLI is installed or run from npm. <br>
Mitigation: Review the pinned @dlazy/cli package and source before installing, and use the pinned npx command if you do not want to keep a global CLI installation. <br>


## Reference(s): <br>
- [dLazy CLI repository](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides authentication, project selection, file attachment, and dLazy CLI invocation for document-to-video workflows.] <br>

## Skill Version(s): <br>
1.0.2 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
