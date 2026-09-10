## Description:

Turns slides or documents into narrated slideshow videos with voiceover and transitions through the dLazy CLI and hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to ask an agent to convert slides, documents, or image references into slideshow-style explainer, courseware, report, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party CLI and hosted dLazy service.

Mitigation: Review the dLazy CLI/source before installing and prefer the pinned npx path or a low-privilege environment when a persistent global binary is not desired.

Risk: Attached local files are uploaded to dLazy storage for processing.

Mitigation: Attach only files that are appropriate to share with dLazy and avoid uploading sensitive content without organizational approval.

Risk: The dLazy API key is a credential stored locally or supplied through the environment.

Mitigation: Protect the key, use per-user configuration, and rotate or revoke it if the environment is shared or compromised.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown or plain text guidance with dLazy CLI commands; service responses may include generated video links or files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key. Attached local files are uploaded to dLazy storage before being referenced by the hosted agent.]

## Skill Version(s):

1.0.12 (source: ClawHub release evidence; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
