## Description:

House Skills Kit provides Chinese real-estate agent skills, sales SOPs, calculation tools, and brand-specific skill templates for property sales and advisory workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danfeistar](https://clawhub.ai/user/danfeistar)

### License/Terms of Use:

Apache-2.0

## Use Case:

Real-estate sales teams, marketing planners, brokers, channel distributors, and buyer-facing advisors use this kit to select, install, or generate AI skills for Chinese property workflows. It supports transaction calculations, customer reception, lead grading, objection handling, sales closing, mortgage guidance, launch execution, presale marketing, and competitive-intelligence routines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server security evidence reports that the generator and installer can write skill files outside advertised containment paths when given crafted names or paths.

Mitigation: Install only from trusted configs, inspect brand slug, domain, CTA, and contact fields before rendering, avoid custom AGENT_HOME paths with traversal or symlinks, and review path validation before broad use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/danfeistar/skills/house-skills-kit)
- [README](artifact/README.md)
- [Calc Toolkit README](artifact/skills/calc-toolkit/README.md)
- [Kunming Example References](artifact/examples/kunming/references/plates.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance, Python command examples, generated SKILL.md files, manifests, and calculator outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local YAML rules for city-specific calculations and can generate brand-specific skill files from configuration.]

## Skill Version(s):

1.7.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
