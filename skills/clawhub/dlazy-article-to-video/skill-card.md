## Description:

Helps turn articles and documents into narrated explainer videos using dLazy's hosted workflow for outlining, storyboarding, voiceover, assembly, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and teams use this skill to turn an article or document into a narrated explainer, training, or report video through dLazy's service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached files are uploaded to dLazy's hosted service.

Mitigation: Attach only files you are comfortable sharing with dLazy.

Risk: The third-party CLI is installed or run to access the service.

Mitigation: Review @dlazy/cli before installing if high assurance is required; use npx instead of global installation if preferred.

Risk: Access requires a dLazy API key stored by the CLI or supplied at runtime.

Mitigation: Protect the key and rotate or revoke it when no longer needed.

## Reference(s):

- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides a project-based hosted video workflow; files attached to CLI requests are uploaded to dLazy.]

## Skill Version(s):

1.0.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
