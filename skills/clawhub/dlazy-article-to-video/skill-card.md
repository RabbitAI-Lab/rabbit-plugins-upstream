## Description: <br>
Turns articles and documents into narrated explainer videos by using the dLazy hosted file-to-video workflow for outline, storyboard, voiceover, build, and validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn articles, PDFs, office documents, reports, courseware, or training material into narrated explainer videos through the dLazy CLI and hosted service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill label emphasizes article-to-video, but the artifact and security summary show broader document and file-to-video handling. <br>
Mitigation: Review and approve it as a hosted file/document conversion integration, not only as an article conversion helper. <br>
Risk: Files attached with the dLazy CLI are uploaded to dLazy media storage. <br>
Mitigation: Attach only files that are appropriate to upload to dLazy and avoid sensitive material unless the upload is approved. <br>
Risk: The dLazy API key can be stored in the local CLI configuration. <br>
Mitigation: Use per-invocation credentials when preferred, and rotate or revoke the dLazy API key when access is no longer needed. <br>
Risk: A global CLI install leaves a persistent binary on the system. <br>
Mitigation: Use the pinned npx invocation when a non-persistent install posture is preferred. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide dLazy CLI authentication, project selection, file upload, and follow-up commands.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
