## Description:

Octave lets an agent use the OOMOL-connected oo CLI to inspect Octave action schemas, run Octave connector actions, and validate workspace access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Octave through an OOMOL-connected account, including listing agents, running Octave enrichment or qualification agents, and validating API key workspace metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote CLI installer commands can execute code from a network source.

Mitigation: Prefer a verified package-manager or otherwise trusted oo CLI installation path, and review remote installer commands before execution.

Risk: Octave run_* actions can process personal, company, customer, or sales data even when no Octave record is modified.

Mitigation: Confirm payload contents and intended data handling with the user before running agent actions that include sensitive business data.

Risk: The skill depends on OOMOL and Octave account connection state, scopes, credits, and workspace access.

Mitigation: Use live action schemas, confirm the target workspace when relevant, and resolve authentication or connection errors through OOMOL account setup before retrying.

## Reference(s):

- [Octave homepage](https://www.octavehq.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Octave skill](https://clawhub.ai/oomol/skills/oo-octave)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects that include data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
