## Description:

LENS helps an agent use a person's context, judgment, and voice when explicitly asked, and supports calibrating or distilling that profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[capachow](https://clawhub.ai/user/capachow)

### License/Terms of Use:

MIT-0

## Use Case:

People use LENS to tailor an agent's reasoning and writing to their personal context when they request it. They can also calibrate, update, or distill their LENS profile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills.

Mitigation: Review and scan skill before deployment.

## Reference(s):

- [LENS ClawHub release](https://clawhub.ai/capachow/skills/lens)
- [Trinity definitions](references/trinity-definitions.md)
- [Resolve protocol](references/resolve-protocol.md)
- [Alignment scales](references/alignment-scales.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration]

**Output Format:** [Conversational text or Markdown; YAML and JSON profile configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile calibration and distillation are user-directed; conversation collection and scheduled workflows may be enabled during setup.]

## Skill Version(s):

2.1.0 (source: package.json and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
