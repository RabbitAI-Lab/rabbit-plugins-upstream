## Description: <br>
Checks and fixes English abbreviations in TRPG rules, scenarios, character sheets, catalogs, maps, and other player/GM-facing files by expanding game terms to Chinese full names with abbreviations in parentheses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ice26985850](https://clawhub.ai/user/ice26985850) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
TRPG writers, editors, and maintainers use this skill to make player- and GM-facing Traditional Chinese game materials easier to read by replacing unexplained English abbreviations such as STR, HP, or DC with Chinese full-name-plus-abbreviation forms. It applies to rulebooks, scenarios, character sheets, catalogs, maps, and reference files while preserving formula variables, filenames, and specified table exceptions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may change many TRPG content files in one pass, which can introduce unintended terminology or formatting changes. <br>
Mitigation: Use it in a version-controlled project and review the proposed diff before accepting edits. <br>
Risk: Projects using Simplified Chinese or mixed-language terminology may receive replacements that do not match the intended writing style. <br>
Mitigation: Review terminology and script consistency, especially where the artifact requires Traditional Chinese names. <br>
Risk: Backup, draft, or transitional files may be skipped by the artifact's file-selection guidance even when a project wants them checked. <br>
Mitigation: Confirm the target file set before running the skill and explicitly include exceptional files when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ice26985850/skills/trpg-abbr-check-rules) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance and file edits or proposed replacements] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May affect many TRPG content files at once; review diffs before accepting changes.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
