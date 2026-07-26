## Description: <br>
csv-handler-free helps agents inspect, read, clean, and export CSV files by detecting common encodings and delimiters, profiling row and column structure, normalizing column names, dropping empty rows, and writing UTF-8-SIG CSV output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and operations teams use this skill when an agent needs to inspect a single CSV file, detect its encoding and delimiter, perform basic cleanup, and export a cleaned CSV for downstream work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read local CSV files and write exported CSV outputs. <br>
Mitigation: Review input and output paths before allowing the agent to access files or write results. <br>
Risk: The skill may run local processing commands while handling CSV data. <br>
Mitigation: Approve only expected CSV-processing commands and review generated code before execution. <br>
Risk: Supplying a callback URL could expose completion metadata or sensitive workflow context to an external endpoint. <br>
Mitigation: Use callback URLs only for intended external notifications and avoid them for sensitive CSV work. <br>
Risk: Malformed CSV rows may be skipped during parsing, which can make outputs incomplete. <br>
Mitigation: Check row counts and parser warnings against the original file before relying on cleaned results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/csv-handler-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with Python code snippets, shell configuration examples, JSON-style status results, and exported CSV files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads local CSV inputs, may run local processing commands, and may write cleaned CSV outputs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
