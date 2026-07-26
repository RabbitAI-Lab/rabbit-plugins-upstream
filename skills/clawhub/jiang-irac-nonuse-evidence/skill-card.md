## Description: <br>
CNIPA撤三（连续三年不使用）双轨证据引擎：答辩证据链构建 + 质证审计（SJ-6 + IRAC + 风险A–E）。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jisngzhongling](https://clawhub.ai/user/jisngzhongling) <br>

### License/Terms of Use: <br>
Commercial License <br>


## Use Case: <br>
Trademark practitioners and legal operations teams use this skill to process CNIPA three-year non-use cancellation case evidence, map period and proof elements, generate defense or cross-examination materials, and produce risk reports for human review. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Unsafe file handling may affect source or output files when organizing case materials. <br>
Mitigation: Use trusted case files, install in a dedicated environment, and only use organize-directory behavior with a disposable output folder. <br>
Risk: The local web or desktop UI could create exposure if made reachable from a network. <br>
Mitigation: Keep the Web UI bound to 127.0.0.1 and avoid exposing the desktop or web server to a network. <br>
Risk: Dependencies and local execution behavior may need additional production review. <br>
Mitigation: Pin and review dependencies before production use. <br>
Risk: Generated legal documents and risk reports may be incomplete or unsuitable without professional review. <br>
Mitigation: Treat outputs as technical and methodological support, verify source evidence, and have qualified users review case submissions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jisngzhongling/skills/jiang-irac-nonuse-evidence) <br>
- [README.md](README.md) <br>
- [INSTALL.md](INSTALL.md) <br>
- [DISCLAIMER.md](DISCLAIMER.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with command examples and generated document, spreadsheet, PDF, and JSON report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local outputs can include defense reasons, evidence catalogs, risk reports, reordered evidence PDFs, spreadsheets, and validation JSON files; human legal review remains required.] <br>

## Skill Version(s): <br>
3.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
