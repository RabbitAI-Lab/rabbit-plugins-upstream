## Description:

Explains the input/output (IO) file handling, property serialization, and directory-path manipulation methods in Nasal, combining raw stream operations ('io') with high-level path parsing wrappers ('os.path').

This skill is ready for commercial/non-commercial use.

## Publisher:

[container32](https://clawhub.ai/user/container32)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill as reference guidance for generating or reviewing Nasal file-system handling in FlightGear, including raw file streams, property tree XML serialization, path inspection, and directory operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated code may modify files because the reference includes write, delete, and rename APIs.

Mitigation: Review generated Nasal before running it in FlightGear, especially when it writes outside the intended FlightGear export workflow.

Risk: File-system examples may fail or be unsafe if FlightGear security constraints are ignored.

Mitigation: Keep write and delete operations within locations permitted by FlightGear, normally the $FG_HOME/Export/ directory described by the artifact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/container32/skills/nasal-library-file-system)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code]

**Output Format:** [Markdown guidance with inline Nasal code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only reference material; examples that write, delete, or rename files should be reviewed before use in FlightGear.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
