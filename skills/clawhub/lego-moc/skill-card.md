## Description:

Recognises loose LEGO parts from photos, builds an inventory, and helps design an LDraw model that a server checks and can render with building instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[garmanwu](https://clawhub.ai/user/garmanwu)

### License/Terms of Use:

MIT-0

## Use Case:

External LEGO enthusiasts can use an agent to identify parts from photos, manage an inventory, and design a model from the parts they own. They can receive model check results, a 3D preview, and building instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious and reports guidance to bypass network restrictions; its scan covered only part of the components and is inconclusive.

Mitigation: Do not install until the reported guidance is addressed; review the release and obtain a complete security scan.

Risk: Photos, parts lists, and model details are sent to the service; inventory links can be used by anyone who has them, and passed models are public.

Mitigation: Upload only material intended for sharing, and keep inventory and model links private.

## Reference(s):

- [LEGO MOC ClawHub page](https://clawhub.ai/garmanwu/skills/lego-moc)
- [LEGO MOC project homepage](https://github.com/garmanwu/lego-moc)
- [LEGO parts service](https://lego.groundrl.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [LDraw model text, JSON configuration, and human-readable responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return model check notes and links to previews and building instructions.]

## Skill Version(s):

2.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
