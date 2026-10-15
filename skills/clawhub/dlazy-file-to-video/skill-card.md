## Description:

Helps turn presentations, documents, spreadsheets, and PDFs into narrated explainer, report, courseware, or training videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and business teams use this skill to request video explanations of presentations, reports, and other documents through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents can be sent to dLazy's hosted service.

Mitigation: Attach only documents approved for upload and review the service before use.

Risk: The CLI may store an API key on the local machine.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: Using the external npm CLI introduces a third-party dependency.

Mitigation: Review its package and source before installing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Text with CLI commands and project-based responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation runs through the dLazy hosted service.]

## Skill Version(s):

1.3.29 (source: ClawHub release; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
