## Description:

This skill helps agents turn garment flat-lay or on-model reference images into on-model e-commerce fashion photos while preserving garment style, color, texture, print, and tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, merchandisers, and agents use this skill to generate model-worn product photos from flat-lay garments, optional reference poses, and optional fixed model identity inputs. It supports single-garment and full-look workflows for catalog, marketplace, and social commerce imagery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided garment, reference, and prompt inputs are sent to dLazy-hosted services for generation.

Mitigation: Review dLazy's CLI and service terms before installing or running the skill, and avoid submitting sensitive images unless that service use is approved.

Risk: Model-selection filters and generated fashion imagery could be used in ways that discriminate, imply endorsement, or create inappropriate images involving minors.

Mitigation: Use the demographic and model-selection controls only for legitimate merchandising needs, review generated images before publication, and reject outputs that imply endorsement or inappropriate depictions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/flat-lay)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image assets may be returned as hosted URLs and can be saved to local files when the CLI save option is used.]

## Skill Version(s):

1.0.0 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
