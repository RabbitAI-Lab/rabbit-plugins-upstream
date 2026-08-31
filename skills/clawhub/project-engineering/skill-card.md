## Description:

Project Engineering helps coding agents design greenfield engineering baselines and make evidence-driven changes in existing repositories before implementation, refactoring, review, testing, or delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liubai00](https://clawhub.ai/user/liubai00)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and engineering teams use this skill to guide coding agents through greenfield architecture, existing-repository discovery, scoped implementation, risk-calibrated validation, review, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read repository structure, Git status, build manifests, and related project files.

Mitigation: Use it only on repositories the user is comfortable allowing an agent to inspect.

Risk: Engineering work can lead to commits, pushes, deployments, migrations, credential changes, or production operations if authorization is unclear.

Mitigation: Require separate explicit approval before those actions; keep default work to local inspection or authorized workspace changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/liubai00/skills/project-engineering)
- [Project Homepage](https://github.com/liubai00/project-engineering)
- [Usage Guide](docs/USAGE.md)
- [Greenfield Projects and Engineering Baseline](references/greenfield.md)
- [Engineering Discovery and Evidence Recovery](references/discovery.md)
- [Architecture and Boundary Design](references/architecture.md)
- [Implementation, Data, and Validation](references/implementation.md)
- [Project Archetypes and Risk Levels](references/risk-and-archetypes.md)
- [Planning, Review, and Delivery](references/delivery.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and shell-command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed file changes, validation commands, risk notes, and delivery reports depending on user authorization.]

## Skill Version(s):

1.0.2 (source: changelog, released 2026-08-25; server release metadata agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
