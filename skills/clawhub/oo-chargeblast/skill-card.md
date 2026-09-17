## Description:

Chargeblast (chargeblast.com). Use this skill for Chargeblast requests involving reading, creating, and updating account data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Chargeblast action schemas and run supported connector actions for alerts, orders, merchants, deflection logs, credit requests, and alert updates. It is intended for OOMOL-connected Chargeblast accounts where credentials are handled by the platform rather than by the agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup guidance can execute arbitrary code if the installer source is compromised or unexpected.

Mitigation: Review the installer path before installation and prefer a pinned, verified oo CLI release or official package manager.

Risk: Write actions such as create_credit_request and update_alert can change Chargeblast account state.

Mitigation: Inspect the live action schema and confirm the exact payload and intended effect with the user before running state-changing actions.

## Reference(s):

- [Chargeblast homepage](https://www.chargeblast.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Chargeblast skill page](https://clawhub.ai/oomol/skills/oo-chargeblast)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo CLI schema inspection before constructing connector action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
