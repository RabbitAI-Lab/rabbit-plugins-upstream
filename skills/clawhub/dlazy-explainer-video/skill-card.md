## Description:

Turn a document, topic, or brief into a narrated explainer video by creating an outline, storyboard, voiceover, and validated build.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People who need explainer, courseware, or training videos can use this skill to turn a document, topic, or brief into a narrated video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment was partial and noted a CLI login and project-listing mismatch, though it treated the flagged operations as expected for the skill's purpose.

Mitigation: Review the full skill and installation details, and decide whether the reported login and project-listing operations fit your use before installing.

Risk: Prompts are sent to dLazy's hosted API, and attached local files are uploaded to its media storage.

Mitigation: Avoid attaching sensitive files unless the service's data handling meets your requirements.

## Reference(s):

- [dLazy CLI project page (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Text, Shell commands, Configuration guidance]

**Output Format:** [Narrated explainer video with text guidance and CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the dLazy file-to-video template; a dLazy API key is required.]

## Skill Version(s):

1.0.41 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
