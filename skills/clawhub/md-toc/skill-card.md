## Description:

Generate a table of contents for a Markdown file by extracting ATX headings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical writers, and documentation reviewers use md-toc to create a navigable Markdown table of contents or quick outline for README files, notes, and long documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper reads the Markdown file path supplied by the user.

Mitigation: Run it only on intended local Markdown files and review the generated table of contents before inserting it into documentation.

Risk: The helper requires bash and awk to run.

Mitigation: Confirm those command-line tools are available in the target environment before relying on the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/md-toc)
- [Publisher profile](https://clawhub.ai/user/terrycarter1985)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown list with relative anchor links, usually printed to stdout after a bash command.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads a user-specified Markdown file; supports --max to cap heading depth; skips fenced code blocks.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
