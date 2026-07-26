## Description: <br>
Jw Data Analyst helps agents generate Python data-processing scripts, visual charts, and statistical reports for Excel, CSV, JSON, API, and database data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and data-focused agent users use this skill to load, clean, analyze, visualize, and report on structured data from files, APIs, and databases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process sensitive datasets, database connections, and API sources. <br>
Mitigation: Use anonymized data where possible and provide read-only, least-privilege credentials unless confidential analysis is intended. <br>
Risk: Generated scripts and output files may write charts to a local D drive by default. <br>
Mitigation: Confirm and adjust output paths before running generated code. <br>
Risk: Large files over 100MB may be resource intensive. <br>
Mitigation: Process large datasets in batches and validate results on representative samples before full runs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/jw-data-analyst) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, files, guidance] <br>
**Output Format:** [Markdown reports, Python scripts, PNG/SVG charts, and Excel/CSV files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save generated charts to a local D drive by default; files over 100MB may need batch processing.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
