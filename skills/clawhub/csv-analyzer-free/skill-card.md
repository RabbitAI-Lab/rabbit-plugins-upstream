## Description: <br>
CSV Analyzer Free guides agents through lightweight CSV inspection with basic statistics, simple filtering, and optional CSV export using Python standard-library workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and other external agent users use this skill for lightweight CSV exploration when they need row counts, type detection, numeric summaries, unique counts, and single-condition filtering without pandas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local CSV files and can write filtered CSV outputs. <br>
Mitigation: Use it only on files the agent is allowed to read and choose explicit output filenames to avoid overwriting important files. <br>
Risk: The inspected package does not include the referenced analyzer script. <br>
Mitigation: Confirm the required script exists or implement the missing command behavior before relying on the skill in production workflows. <br>
Risk: Large CSV files can exceed the skill's intended lightweight operating range. <br>
Mitigation: Keep inputs near the documented 100 MB limit, split larger files, or use a streaming tool for high-volume analysis. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/csv-analyzer-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and CSV output descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read local CSV files and write explicitly named CSV output files when filtering.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
