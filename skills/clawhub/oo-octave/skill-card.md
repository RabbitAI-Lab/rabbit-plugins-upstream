## Description:

Octave enables an agent to read, create, and update Octave data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users working with an OOMOL-connected Octave account use this skill to inspect Octave action schemas, run connector actions, list agents, and execute enrichment, qualification, call-prep, and context-agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Octave workspaces may contain sensitive customer or business data.

Mitigation: Review the skill before installation and confirm the target action and payload before running account-connected actions.

Risk: Some Octave agent actions can change workspace state or have under-scoped write behavior.

Mitigation: Require explicit user confirmation before running run_* actions or any action tagged as write or destructive.

Risk: First-time setup guidance includes remote installer commands.

Mitigation: Avoid running one-line installers unless the OOMOL installation endpoint is trusted or the installer can be verified by safer means.

## Reference(s):

- [Octave homepage](https://www.octavehq.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON containing data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
