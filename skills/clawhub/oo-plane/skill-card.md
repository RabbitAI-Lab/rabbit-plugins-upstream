## Description:

Plane (plane.so) skill for reading, creating, updating, and deleting Plane data through OOMOL's connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Plane projects, work items, labels, states, members, and user profile data through OOMOL-connected CLI actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute arbitrary code.

Mitigation: Review the installer path before use and prefer a verified package, pinned release, checksum, or signature-checked installer.

Risk: Plane write and delete actions can change or remove work items.

Mitigation: Approve these actions only after confirming the exact target, payload, and expected effect.

## Reference(s):

- [Plane homepage](https://plane.so)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-plane)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON command payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, OOMOL sign-in, and a connected Plane account.]

## Skill Version(s):

1.0.2 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
