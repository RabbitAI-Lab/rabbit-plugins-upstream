## Description:

Guides developers in building and running Go services with the clone-and-own servicepack framework.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create Go services with concurrent workers, dependency-aware startup, retries, and graceful shutdown in a servicepack-based project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup command can replace the module path and reinitialize Git history in a clone.

Mitigation: Review the framework repository first, and run setup only in a disposable or intentionally changeable clone.

Risk: Framework updates overwrite framework-owned files.

Mitigation: Keep custom services and lifecycle hooks in the documented project-owned files.

## Reference(s):

- [servicepack setup guide](references/setup.md)
- [servicepack framework homepage](https://github.com/psyb0t/servicepack)
- [ClawHub servicepack release](https://clawhub.ai/psyb0t/skills/servicepack)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Docker for the documented build and development workflows.]

## Skill Version(s):

1.10.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
