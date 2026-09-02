## Description:

Skill Studio guides agents through diagnosing, designing, generating, validating, packaging, and auditing Agent Skills using five reusable design patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[coolhitbird](https://clawhub.ai/user/coolhitbird)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this meta-skill to create, refactor, audit, validate, package, and install Agent Skills through a staged SOP and supporting Python scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaging flow can copy files into agent skill directories and overwrite existing installed skills.

Mitigation: Review destination paths before using --target or --target all, and keep backups of existing skill directories before installation.

Risk: The validation gate can fail open if validate.py is missing or crashes.

Mitigation: Require packaging to stop when validation cannot run successfully, and review the validation result before distributing the package.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/coolhitbird/skills/skill-studio)
- [Server-resolved GitHub provenance](https://github.com/coolhitbird/skill-studio/tree/master/skill-studio)
- [Skill Create SOP](references/sop.md)
- [Architecture](references/architecture.md)
- [Anti-Patterns](references/anti-patterns.md)
- [Pattern: Tool Wrapper](references/pattern-tool-wrapper.md)
- [Pattern: Generator](references/pattern-generator.md)
- [Pattern: Reviewer](references/pattern-reviewer.md)
- [Pattern: Inversion](references/pattern-inversion.md)
- [Pattern: Pipeline](references/pattern-pipeline.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance, Python command examples, generated skill files, JSON diagnostics, and ZIP packages when packaging scripts are run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify skill directories and install packaged skills when script targets are used.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
