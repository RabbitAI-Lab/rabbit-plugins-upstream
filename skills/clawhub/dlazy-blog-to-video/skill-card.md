## Description:

Helps turn blog posts and other documents into narrated videos with storyboards and voiceovers using dLazy's file-to-video service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and teams use this skill to request narrated videos from blog posts or documents and continue video projects through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is labeled blog-to-video but invokes a broader file-to-video service that can upload local documents to a third party.

Mitigation: Only attach files you are comfortable uploading to dLazy and review the intended content before sending it.

Risk: Continuing a previous session could use the wrong project.

Mitigation: Confirm the project identifier before continuing an existing session.

Risk: Logging in stores a revocable API key in local dLazy configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if it is exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text with command examples and links to generated videos when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation is performed by the dLazy service; attached files may be uploaded to dLazy.]

## Skill Version(s):

1.0.29 (source: ClawHub release; source-file frontmatter says 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
