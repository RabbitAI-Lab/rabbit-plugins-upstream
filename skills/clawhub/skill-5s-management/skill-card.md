## Description: <br>
Provides Chinese-language 5S management standards, visual management design guidance, site issue diagnosis, improvement templates, and report-generation support for sorting, set-in-order, shining, standardizing, and sustaining workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operations, quality, and manufacturing teams use this skill to check 5S standards, design visual management schemes, diagnose on-site issues, plan corrective actions, and prepare 5S inspection reports. Developers or analysts can also use the included script to turn trusted inspection JSON into an HTML visual report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The report generator reads input and trend JSON files from paths supplied at runtime. <br>
Mitigation: Use trusted inspection data and review file paths before running the script. <br>
Risk: Text fields from inspection JSON are inserted into the generated HTML report. <br>
Mitigation: Avoid opening reports generated from untrusted JSON, and review report contents before sharing. <br>
Risk: The script writes an HTML report to the output path supplied by the user. <br>
Mitigation: Choose output paths carefully to avoid overwriting important files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-5s-management) <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-5s-management) <br>
- [Publisher profile](https://clawhub.ai/user/duding-engicool) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, HTML] <br>
**Output Format:** [Markdown guidance with tables, templates, JSON examples, shell commands, and optional generated HTML reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The report script reads a user-provided inspection JSON file, can read optional trend JSON, writes an HTML report to a user-selected output path, and prints a JSON execution summary.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter version is 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
