## Description:

Turns a written article into a narrated explainer video through outlining, storyboarding, voiceover, generation, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People who want an article or document turned into a narrated explainer, report, course, or training video can use this skill to guide the video creation process.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes that login and project-listing commands are not clearly tied to the video-making purpose.

Mitigation: Check why those steps are needed before running them, and confirm the account and project you intend to use.

Risk: Prompts are sent to dLazy and attached local files are uploaded to its media storage; using the CLI also requires an API key.

Mitigation: Review dLazy's terms before sharing sensitive material, send only the content needed for the video, and use an API key scoped to the intended organization.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy service](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video files, Text guidance, Shell commands]

**Output Format:** [Generated video media and text responses; CLI interactions use shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can use article text or attached local files; attached files are uploaded to dLazy media storage.]

## Skill Version(s):

1.0.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
