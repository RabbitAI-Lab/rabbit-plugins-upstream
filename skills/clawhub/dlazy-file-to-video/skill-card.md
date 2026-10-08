## Description:

Turns user-provided presentations, documents, spreadsheets, and PDFs into narrated explainer, training, or report videos through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and teams use this skill to turn supplied documents into explainer, courseware, training, or report videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy's hosted service.

Mitigation: Review documents for sensitive content and obtain approval before uploading.

Risk: An API key may be stored in local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: Using the hosted service may consume paid credits.

Mitigation: Confirm available credits and expected usage before starting a video task.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation runs on dLazy's hosted service; results can be continued by project.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
