## Description: <br>
Searches local iFA Evolution help indexes and HTML documentation to answer Chinese help queries with structured summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers using iFA Evolution can ask for help topics, function descriptions, interface parameters, call formats, return values, notes, and comparisons without manually searching local HTML help files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contains hardcoded Windows paths for the iFA Evolution help directory and topic index, including a user-specific path. <br>
Mitigation: Confirm and adjust the local help and index paths before use, and limit agent file access to the intended documentation folders. <br>
Risk: Answers depend on the local help files and the selected topic version, so results may not match a different iFA Evolution installation or documentation release. <br>
Mitigation: Verify the selected HTML file and topic version against the installed product documentation when using the output for implementation decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/ifa-help-query) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Structured Chinese Markdown with occasional PowerShell snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prioritizes topic name, related HTML file, function description, interface parameters, call format, return values or error codes, notes, and comparison dimensions.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
