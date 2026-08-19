## Description:

ppt to video, powerpoint to video, slides to video, presentation to video — parse the deck, outline, storyboard, voiceover, build, validate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to turn slide decks and documents into explainer, pitch, courseware, training, or report videos through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached local files are sent to dLazy's hosted API and media storage.

Mitigation: Confirm the documents are appropriate for dLazy's hosted service before attaching confidential or sensitive content.

Risk: The dLazy API key may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local user account and rotate or revoke the API key when the CLI is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with inline bash commands and streamed CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated video assets are produced by the dLazy hosted service outside the skill.]

## Skill Version(s):

1.0.5 (source: server release evidence; artifact frontmatter states 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
