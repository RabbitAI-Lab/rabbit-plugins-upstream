## Description:

Zylvie (zylvie.com). Use this skill for reading, creating, updating, and deleting Zylvie data through the OOMOL `oo` CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and business users use this skill to manage Zylvie products, coupons, license keys, and subscriptions through an OOMOL-connected Zylvie account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and destructive Zylvie actions can change, delete, archive, refund, or redeem production data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running actions tagged `[write]` or `[destructive]`.

Risk: The first-time setup fallback includes pipe-to-shell installer commands for the `oo` CLI.

Mitigation: Prefer OOMOL's official installation documentation and review installer commands before execution.

Risk: Connector payloads may fail or affect unintended records if built without the current action contract.

Mitigation: Fetch the live action schema with `oo connector schema` before constructing `oo connector run` payloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-zylvie)
- [Zylvie Homepage](https://zylvie.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands run through the `oo` CLI and return connector responses as JSON.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
