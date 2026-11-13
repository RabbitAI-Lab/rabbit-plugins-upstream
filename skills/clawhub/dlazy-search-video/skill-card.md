## Description:

Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to search Pixabay for stock footage by keyword and retrieve video URLs and metadata for sourcing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review noted a mismatch between the stated Pixabay search purpose and visible dLazy authentication or CLI setup; the CLI's internal behavior was not established.

Mitigation: Confirm that dLazy authentication and CLI setup are expected for this skill, and review the linked CLI package before configuring an API key.

## Reference(s):

- [dLazy CLI project (metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Video URLs, Metadata]

**Output Format:** [JSON search results containing video URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search terms and filters can be supplied through CLI options; results are paginated.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
