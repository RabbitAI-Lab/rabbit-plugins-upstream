## Description:

House Skills Kit generates brand-customized Chinese real-estate AI advisor skills from a brand.yaml configuration across four role archetypes and 29 business modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danfeistar](https://clawhub.ai/user/danfeistar)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, real-estate operators, brokerages, channel distributors, and home-buyer platforms use this kit to generate branded Chinese advisor skill Markdown and manifests from YAML configuration and modular templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some optional templates steer agents into customer, owner, or channel data management without enough consent, retention, or activation safeguards.

Mitigation: Review generated brand.yaml triggers before installation, use explicit brand/project/city phrases, and require user confirmation before lead capture or contact sharing.

Risk: Real-estate CRM, developer-sales, and channel workflows can involve customer, owner, and partner data.

Mitigation: Connect only adapters that enforce authorization, data minimization, retention, deletion, and access controls for the relevant data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/danfeistar/skills/house-skills-kit)
- [README](README.md)
- [Mock Adapter README](adapters/mock/README.md)
- [Kunming Example README](examples/kunming/README.md)
- [Kunming Plate Reference](examples/kunming/references/plates.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown skill files, JSON manifests, YAML configuration, and shell/Python commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated skills are brand-customized from YAML inputs, selected role archetypes, optional modules, and configured data adapters.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
