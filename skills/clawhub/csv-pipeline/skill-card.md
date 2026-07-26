## Description: <br>
CSV Data Pipeline helps agents process, transform, analyze, and report on CSV, TSV, JSON, and JSON Lines data files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and agent operators use this skill to guide local file-based data workflows such as filtering, joining, aggregation, deduplication, validation, format conversion, and Markdown report generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent to read sensitive local datasets. <br>
Mitigation: Use only files you intend the agent to inspect and transform. <br>
Risk: Data transformations can overwrite or replace important files. <br>
Mitigation: Keep backups and write outputs to new paths before replacing originals. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with bash and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local CSV, TSV, JSON, JSON Lines, or Markdown report files when the agent runs the suggested commands or code.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
