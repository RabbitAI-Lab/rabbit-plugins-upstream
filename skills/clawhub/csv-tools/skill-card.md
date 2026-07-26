## Description: <br>
CSV Tools helps agents inspect, clean, transform, validate, profile, split, merge, and sample CSV and TSV files locally with Python standard-library commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data practitioners use this skill to generate and run local CSV utility commands for routine data exploration, cleanup, validation, profiling, splitting, merging, and sampling workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Some commands create or overwrite default output files such as filtered.csv, sorted.csv, merged.csv, chunk.csv, and deduped.csv. <br>
Mitigation: Review the command before execution, run it from the intended working directory, and pass an explicit --output path when preserving existing files matters. <br>
Risk: The skill is intended for local CSV-like tabular files and can produce misleading results if applied to unsupported formats or high-stakes decisions without review. <br>
Mitigation: Use it only for CSV, TSV, or pipe-delimited text and independently verify important calculations, profiles, and validation results. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/cqdev-ai/skills/csv-tools) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Files, Analysis] <br>
**Output Format:** [Markdown guidance with shell commands; command execution can produce terminal text, CSV files, or JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally without network behavior; write operations target command output paths.] <br>

## Skill Version(s): <br>
1.1.0 (source: release metadata, package.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
