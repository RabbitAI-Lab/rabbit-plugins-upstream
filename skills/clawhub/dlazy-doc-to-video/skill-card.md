## Description:

Converts documents into video projects by using dLazy's hosted file-to-video CLI workflow to parse, outline, storyboard, voice over, build, and validate explainer, report, courseware, or training videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to turn Doc, Word, Markdown, PDF, PPT, Excel, or similar source documents into explainer, report broadcast, courseware, and training video workflows through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documents attached with --files may be uploaded to dLazy's third-party service.

Mitigation: Review dLazy's service terms and attach only files that are appropriate to send to that service.

Risk: The dLazy API key may be stored in the user's local CLI configuration.

Mitigation: Use OS account protections for the config file and rotate or revoke organization-scoped keys when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the pinned @dlazy/cli 1.2.3 package and the dLazy file-to-video hosted template.]

## Skill Version(s):

1.0.15 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
