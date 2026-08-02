## Description: <br>
CSV数据分析-免费版 helps agents analyze small local CSV files with Python standard-library commands for quick statistics and basic filtering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent users can use this skill for lightweight CSV exploration, including row and column statistics, basic type detection, simple filtering, and CSV export for small local files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Exporting filtered results to an existing path could overwrite or replace useful local data. <br>
Mitigation: Choose output paths deliberately and review the destination before running export commands. <br>
Risk: Large CSV files may exhaust memory or run slowly because the artifact describes an approximately 100 MB practical limit. <br>
Mitigation: Use the skill for small local CSV files, split larger datasets, or switch to a streaming or pandas-based workflow when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/csv-analyzer-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and CSV output paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Intended for local CSV files under about 100 MB; filtered results may be exported to user-selected CSV paths.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
