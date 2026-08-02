## Description: <br>
CSV文件处理(免费版) helps agents profile, read, clean, and export CSV files with encoding and delimiter detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and operations users can use this skill to inspect single CSV files, detect common encodings and delimiters, clean basic tabular data, and export results for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: CSV inputs and generated outputs may contain sensitive data. <br>
Mitigation: Treat CSV files as sensitive, review outputs before sharing, and keep processing within trusted workspaces. <br>
Risk: Writing CSV output to the wrong path could overwrite important files. <br>
Mitigation: Use explicit output paths and confirm targets before writing cleaned or exported CSV files. <br>
Risk: A callback URL could send processing status or results to an unintended destination. <br>
Mitigation: Provide a callback URL only when the destination is intended and trusted. <br>
Risk: Malformed CSV rows may be skipped during parsing, which can hide lost records. <br>
Mitigation: Review row counts and parsing warnings after cleaning, especially before relying on exported data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/csv-handler-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Python, bash, and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read local CSV files and write cleaned CSV output when the user provides paths.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
