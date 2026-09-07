## Description:

Kuaidi100 support for searching and reading shipment tracking data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Kuaidi100 connector schemas, identify likely parcel carriers, and query current shipment tracking through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute downloaded code.

Mitigation: Use the skill only with an already trusted oo CLI installation, prefer verified or package-manager installation methods, and require separate approval before installing local software.

Risk: Carrier detection results are advisory and may identify the wrong parcel carrier.

Mitigation: Prefer a carrier known from the shipment source and avoid automatically selecting the first candidate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kuaidi100)
- [Kuaidi100 homepage](https://www.kuaidi100.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs the agent to inspect the live connector schema before running Kuaidi100 actions.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
