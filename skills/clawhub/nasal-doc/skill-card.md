## Description:

Generates and verifies inline documentation and type annotations for Nasal, enhancing code readability and developer accuracy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[container32](https://clawhub.ai/user/container32)

### License/Terms of Use:

MIT-0

## Use Case:

Developers working with FlightGear Nasal code use this skill to add, remove, or check inline documentation and human-readable type annotations without changing program logic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated documentation or type annotations may be incorrect or misleading for the target Nasal code.

Mitigation: Use the check workflow and review the generated annotations against the source behavior before committing changes.

Risk: The add-doc and remove-doc workflows are intended to modify user-selected Nasal files.

Mitigation: Review diffs before committing changes, especially in important source trees.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Markdown guidance with Nasal code comments and type annotations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits to user-selected Nasal files for add-doc and remove-doc workflows.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
