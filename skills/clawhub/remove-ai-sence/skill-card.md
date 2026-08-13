## Description:

Scans front-end projects for AI-associated colors, emoji icons, and exposed English technical errors, then generates an HTML report and guided UI cleanup changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[moan19921019-code](https://clawhub.ai/user/moan19921019-code)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and front-end teams use this skill to review AI-generated or inconsistent UI code, produce a local HTML findings report, and apply brand-aligned cleanup for colors, icons, and user-facing error messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill scans local front-end source files and creates local report or specification files.

Mitigation: Use it only in projects where local source scanning and generated report files are acceptable.

Risk: The skill is designed to make project-wide UI edits for colors, icons, and error-message handling.

Mitigation: Review the generated report before approving replacements and inspect version-control diffs afterward.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/moan19921019-code/skills/remove-ai-sence)
- [Server-resolved source repository](https://github.com/moan19921019-code/remove-ai-sence)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with generated HTML reports, file edits, code snippets, and local configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local report/spec files and propose project-wide UI replacements after user confirmation.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
