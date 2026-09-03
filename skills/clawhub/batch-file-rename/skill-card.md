## Description:

Batch file renaming utility with pattern matching, regex, sequence numbering, and dry-run preview. Supports prefix/suffix, case conversion, whitespace cleanup, and recursive directory processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and other end users use this skill to generate shell command recipes for bulk file renaming, including pattern replacement, sequence numbering, normalization, and recursive processing with dry-run checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bulk rename commands can change many filenames in the wrong folder if run without review.

Mitigation: Run the dry-run preview first and confirm the working directory before applying any mv commands.

Risk: Filename collisions can fail a rename or overwrite existing files in some environments.

Mitigation: Check the proposed destination names for collisions and make a backup before bulk operations.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes dry-run preview recipes, backup guidance, quoting guidance, and collision checks for bulk rename operations.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
