## Description:

Turns a document, topic, or brief into a narrated explainer, courseware, or training video workflow covering outline, storyboard, voiceover, build, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and teams use this skill to operate the dLazy hosted video-generation CLI for document-to-video, explainer, courseware, report broadcast, and training-video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or invokes the third-party @dlazy/cli package.

Mitigation: Review the package or source before installation in sensitive environments, and use the pinned npx invocation when a persistent global binary is not desired.

Risk: The dLazy API key is stored locally or supplied through the environment.

Mitigation: Treat the key as a credential and rotate or revoke it if the CLI environment may have been compromised.

Risk: Attached local files are uploaded to dLazy media storage for processing.

Mitigation: Attach only files that are appropriate to upload to dLazy for the requested video-generation task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated project sessions and uploaded user-selected files handled by the dLazy CLI.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
