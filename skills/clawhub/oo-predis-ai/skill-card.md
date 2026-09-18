## Description:

Predis.ai (predis.ai) helps an agent read, create, and update Predis.ai data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Predis.ai from an agent workflow, including creating AI-generated content, listing generated posts, and browsing templates after inspecting live action schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands executed directly in a shell.

Mitigation: Review the setup path before installation, prefer a versioned, signed, or checksum-verified oo CLI package from the vendor, and avoid running installer commands in an elevated terminal.

Risk: The skill can create Predis.ai content through a write action.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Predis.ai homepage](https://predis.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Predis.ai ClawHub skill page](https://clawhub.ai/oomol/skills/oo-predis-ai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
