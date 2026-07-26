## Description: <br>
Formats and lints Markdown files for consistent headings, links, spacing, emphasis, and readability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation maintainers use this skill to normalize Markdown documents, fix heading structure, standardize links and emphasis, and review formatting changes before accepting them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Formatting can overwrite the Markdown file supplied by the user and may alter text layout or emphasis. <br>
Mitigation: Run the formatter only on intended files and review the resulting diff before accepting changes. <br>


## Reference(s): <br>
- [Markdown Heading Syntax](references/heading-syntax.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown files with command-line status messages and review guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Edits only the user-specified Markdown file and should be followed by diff review.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
