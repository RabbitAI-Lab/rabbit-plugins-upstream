## Description: <br>
Xlsx Pro helps agents create, edit, format, recalculate, and validate Excel and tabular files with spreadsheet formulas rather than hardcoded calculation results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ricobaboule](https://clawhub.ai/user/ricobaboule) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and analysts use this skill when an agent needs to read, clean, create, format, or update XLSX, XLSM, CSV, or TSV files and deliver a spreadsheet artifact. It is especially suited to workbooks that need Excel formulas, LibreOffice recalculation, and formula-error checks before delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The formula recalculation path can modify the user's LibreOffice profile by installing a macro. <br>
Mitigation: Review before installing and prefer a disposable LibreOffice profile or isolated container for recalculation. <br>
Risk: The LibreOffice helper may compile and load a native LD_PRELOAD shim from temporary storage. <br>
Mitigation: Run the skill only in an environment where local native compilation and reuse from temp storage are acceptable, or disable that path if it is not needed. <br>
Risk: Opening and recalculating untrusted spreadsheets can expose the user to spreadsheet and LibreOffice document risks. <br>
Mitigation: Avoid untrusted spreadsheets or process them in an isolated container with least-privilege filesystem access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ricobaboule/skills/xlsx-pro) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with Python and shell code blocks; spreadsheet files and JSON recalculation reports may be produced during use.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated spreadsheets may require LibreOffice headless recalculation and formula-error scanning before delivery.] <br>

## Skill Version(s): <br>
1.0.1 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
