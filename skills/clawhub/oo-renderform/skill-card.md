## Description:

This skill supports RenderForm requests through the OOMOL oo CLI connector, including searching and reading data, rendering images or PDFs, and taking screenshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate RenderForm through an OOMOL-connected account, inspect connector schemas, list templates and results, check usage, render images or PDFs, and capture website screenshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes pipe-to-shell installer commands that can execute remote code.

Mitigation: Review and verify the oo CLI installer or use a trusted installation method before running setup commands.

Risk: Render and screenshot actions can consume RenderForm credits or trigger external website requests.

Mitigation: Confirm the exact payload, template, target URL, and expected cost impact with the user before running credit-consuming actions.

Risk: Using the skill requires OOMOL to mediate RenderForm account access.

Mitigation: Use the skill only when the deployment accepts OOMOL-connected credential handling for RenderForm.

## Reference(s):

- [RenderForm homepage](https://renderform.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [RenderForm skill page](https://clawhub.ai/oomol/skills/oo-renderform)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
