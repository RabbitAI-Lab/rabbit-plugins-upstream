## Description:

Chinese real-estate AI advisor skill generation kit for four roles: home buyers, developer sales teams, brokerage agents, and channel distributors, with 29 business modules that can render a brand-specific Chinese real-estate advisor Skill from a brand.yaml configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danfeistar](https://clawhub.ai/user/danfeistar)

### License/Terms of Use:

Apache-2.0

## Use Case:

External Chinese real-estate businesses, including developers, brokerages, channel distributors, and home-buyer platforms, use this kit to generate brand-customized AI advisor skills. Developers and operators can configure role archetypes, business modules, local market content, and adapters to produce installable skill files for agent runtimes.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Generated real-estate guidance and calculator outputs may contain outdated or locally incorrect mortgage, tax, fee, or policy numbers.

Mitigation: Verify all mortgage, tax, fee, and policy values against current official local sources before using outputs with customers.

Risk: Local helper scripts and rendering inputs may read or write files outside the intended template scope if used with untrusted paths or configuration.

Mitigation: Review helper scripts before installation, avoid rendering untrusted brand.yaml files, and do not pass untrusted template names or paths to calculator or rendering tools.

Risk: Broad trigger wording could cause the skill to activate in unrelated real-estate or finance conversations.

Mitigation: Use narrow trigger keywords and review generated skill text before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/danfeistar/skills/house-skills-kit)
- [README](artifact/README.md)
- [Tools README](artifact/tools/README.md)
- [Kunming Plate References](artifact/examples/kunming/references/plates.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown skill files, JSON manifests, YAML configuration, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated skills depend on brand.yaml configuration, selected archetype, selected modules, and optional local helper scripts.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
