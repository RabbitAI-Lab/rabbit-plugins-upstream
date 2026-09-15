## Description:

Pod AI helps agents read, create, and update Pod AI data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Pod AI through OOMOL, including inspecting connector schemas and creating outbound phone calls with a Pod AI voice agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path may ask users or agents to run remote installer scripts directly in a shell without verification.

Mitigation: Install only after trusting the OOMOL CLI installer source; prefer inspecting the installer, using a signed package manager or pinned release when available, and avoid elevated shells.

Risk: The create_outbound_call action changes Pod AI state by placing an outbound call.

Mitigation: Confirm the exact outbound-call payload and intended effect with the user before running the action.

## Reference(s):

- [Pod AI homepage](https://callpod.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pod-ai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields when actions run successfully.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
