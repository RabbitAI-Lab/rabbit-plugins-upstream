## Description:

Operates Doppler through OOMOL's oo CLI for reading, creating, updating, exporting, and deleting Doppler projects, configs, secrets, tokens, syncs, and change requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Doppler secrets, projects, environments, configs, change requests, service tokens, syncs, integrations, and dynamic secret leases through an OOMOL-connected Doppler account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and export Doppler secrets through the user's connected account.

Mitigation: Review requests that read, export, or disclose secrets, and run them only for intended projects and configs.

Risk: Write and destructive actions can create, overwrite, revoke, or delete Doppler resources including secrets, projects, configs, tokens, syncs, and leases.

Mitigation: Confirm the exact target, payload, and expected effect before running actions marked write or destructive.

Risk: The setup path includes a remote installer command for the oo CLI.

Mitigation: Prefer a verified or package-manager install path, or inspect the installer before executing it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-doppler)
- [Doppler Homepage](https://www.doppler.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON request payloads and returns connector JSON responses with execution metadata.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
