## Description: <br>
Create timestamped quick notes in a daily notes directory for short notes, thoughts, or daily log entries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers can use this skill to append short timestamped notes to a daily Markdown file without opening an editor. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes user-provided notes to local Markdown files and may create a notes directory or daily note file in the selected path. <br>
Mitigation: Use an explicit notes directory when location matters and review the generated daily note file after execution. <br>
Risk: Broad trigger phrases such as "log this" may invoke the skill during ordinary conversation. <br>
Mitigation: Confirm intent before running the skill when the trigger phrase is ambiguous. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands] <br>
**Output Format:** [Markdown daily note entry plus terminal confirmation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Appends timestamped bullet lines to YYYY-MM-DD.md; optional tags are bracketed prefixes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
