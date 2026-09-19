## Description:

Replicate (replicate.com). Use this skill for Replicate requests that read, create, update, list, retrieve, or cancel data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Replicate through an OOMOL-connected account, including inspecting live action schemas and running Replicate connector actions. It supports account, model, version, collection, and prediction workflows, with confirmation expected before write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct remote script execution for installing the oo CLI.

Mitigation: Prefer official, verifiable oo CLI installation methods and review installer commands before running them with user permissions.

Risk: Replicate write actions can create or cancel predictions and change service state.

Mitigation: Review the live action schema and confirm the exact payload and intended effect with the user before executing write actions.

## Reference(s):

- [Replicate homepage](https://replicate.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Replicate skill on ClawHub](https://clawhub.ai/oomol/skills/oo-replicate)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads; connector responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
