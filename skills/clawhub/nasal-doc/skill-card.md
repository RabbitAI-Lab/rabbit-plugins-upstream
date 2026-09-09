## Description:

Generates and verifies inline documentation and type annotations for Nasal, enhancing code readability and developer accuracy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[container32](https://clawhub.ai/user/container32)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers working with Nasal source files use this skill to add, remove, or check inline documentation and human-readable type annotations without changing program logic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The add-doc and remove-doc workflows can change selected Nasal source files.

Mitigation: Run them only on intended files and review diffs before accepting changes.

Risk: Generated type annotations are intended for human and AI readers and are not enforced by FlightGear's Nasal interpreter.

Mitigation: Use check mode and code review to confirm annotations against source behavior before relying on them.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, Code, Guidance]

**Output Format:** [Annotated Nasal source comments and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The add-doc and remove-doc workflows may edit selected Nasal source files; check mode inspects annotations without generating the full fix code.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
