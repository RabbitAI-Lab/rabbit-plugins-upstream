## Description:

Cloudflare Worker (workers.cloudflare.com) handles Cloudflare Worker requests, including reading, creating, updating, and deleting Worker resources through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage Cloudflare Workers and Workers Builds from an agent session through an OOMOL-connected account. It supports inspection, lifecycle operations, script content and settings changes, secret bindings, and build job management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, overwrite, or delete Cloudflare Worker resources when write or destructive actions are approved.

Mitigation: Review the target resource, payload, and expected effect before approving write actions, and require explicit confirmation for destructive actions.

Risk: The first-time setup instructions include remote shell installer commands for the oo CLI.

Mitigation: Prefer a verified or package-manager installation path, or inspect the installer before running it.

## Reference(s):

- [Cloudflare Workers](https://workers.cloudflare.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cloudflare-worker)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo connector schema and run commands; write and destructive actions require user confirmation before execution.]

## Skill Version(s):

1.0.7 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
