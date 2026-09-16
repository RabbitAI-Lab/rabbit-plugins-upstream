## Description:

Enables agents to read, create, update, and delete Cartes.io maps and markers through the OOMOL-connected cartes connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to operate Cartes.io maps and markers from an agent session through an OOMOL-connected account. It supports public read and search workflows, plus confirmed write or destructive map and marker changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute local code.

Mitigation: Avoid curl-to-shell or PowerShell iex installer paths unless the installer source and integrity are independently verified.

Risk: Cartes.io actions depend on OOMOL as an intermediary with server-side credential handling.

Mitigation: Install only when OOMOL is acceptable for the deployment and confirm the connected Cartes.io account and scopes are appropriate.

Risk: Write and destructive actions can change or delete Cartes.io maps and markers.

Mitigation: Confirm the exact target, payload, and expected effect before allowing create, update, or delete actions.

## Reference(s):

- [Cartes.io homepage](https://cartes.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Cartes.io skill page](https://clawhub.ai/oomol/skills/oo-cartes)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs Cartes.io actions through the oo CLI and returns connector JSON responses containing action data and execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
