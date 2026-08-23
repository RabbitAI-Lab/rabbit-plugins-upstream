## Description:

Document-to-video skill for turning Doc, Word, Markdown, PPT, Excel, and PDF inputs into explainer, report, courseware, or training videos through the dLazy CLI and hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, trainers, and business users use this skill to create narrated video content from documents and to continue project-scoped dLazy document-to-video workflows from an agent terminal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads user-selected local documents to dLazy media storage and sends prompts and options to the dLazy API.

Mitigation: Avoid uploading sensitive documents unless dLazy terms and the user's organization policy allow it.

Risk: Authentication can save a dLazy API key in local CLI configuration.

Mitigation: Rotate or revoke keys from the dLazy dashboard when needed, and use DLAZY_API_KEY for temporary credentials when local persistence is not desired.

Risk: The skill depends on a third-party CLI and hosted SaaS service.

Mitigation: Review the dLazy CLI and service terms before installation and use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and service-response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated dLazy projects and uploaded files through the third-party service.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
