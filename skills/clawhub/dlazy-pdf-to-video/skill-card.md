## Description:

Guides an agent through turning PDFs and other documents into narrated explainer, presentation, or training videos using dLazy's hosted file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and business users can use this skill to request narrated explainer, report, courseware, or training videos from PDFs and other documents through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's hosted service.

Mitigation: Check dLazy's data handling and avoid attaching sensitive documents unless its terms are acceptable.

Risk: An API key is needed and may be stored locally by the dLazy CLI.

Mitigation: Protect the local key, use the per-invocation environment variable when appropriate, and rotate or revoke compromised keys.

Risk: The workflow requires installing or running a third-party CLI package.

Mitigation: Review the pinned npm package and its listed source before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted workflow returns replies through the CLI; generated video delivery depends on the dLazy service.]

## Skill Version(s):

1.0.29 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
