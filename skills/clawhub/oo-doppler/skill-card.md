## Description:

Doppler (doppler.com). Use this skill for ANY Doppler request -- reading, creating, updating, and deleting data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Doppler action schemas, run validated connector actions, and manage projects, environments, configs, secrets, service tokens, syncs, integrations, dynamic secret leases, and change requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and export sensitive Doppler secrets.

Mitigation: Require explicit user intent before exposing secret values, especially for secret export, get_secret, and list_secrets actions.

Risk: The skill can perform high-impact write and destructive operations against Doppler resources.

Mitigation: Confirm the exact target, payload, and expected effect before running actions tagged write or destructive.

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Do not let an agent run curl|bash or irm|iex installer commands automatically; install the oo CLI through a verified, pinned, or package-manager based process.

## Reference(s):

- [Doppler homepage](https://www.doppler.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-doppler)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Doppler icon](https://static.oomol.com/logo/third-party/Doppler.svg)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before submitting action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
