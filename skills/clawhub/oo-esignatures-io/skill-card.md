## Description:

eSignatures.com lets an agent read, create, and update eSignatures.com data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate eSignatures.com from an OOMOL-connected account, including retrieving contract and template data, creating templates or contracts, and withdrawing contracts after confirming the intended payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could run unreviewed installation scripts.

Mitigation: Review installer commands before use, prefer verified or version-pinned installation sources, and require explicit approval before running curl|bash or irm|iex setup steps.

Risk: Contract creation, template creation, and contract withdrawal can change eSignatures.com account state.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running state-changing actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-esignatures-io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [eSignatures.com homepage](https://esignatures.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
