## Description: <br>
BOM Toolkit helps manage bill-of-materials workflows, including completeness checks, version comparison, mechanical/electrical splitting, supplier BOM merging, and change reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and engineers use this skill to review local BOM spreadsheets, compare BOM versions, split mechanical and electrical items, merge supplier BOMs, and generate change reports for non-standard automation projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local BOM spreadsheets and creates report or split/merged output files, which may persist sensitive supplier or project data. <br>
Mitigation: Run it only on approved local files and store generated outputs in locations acceptable for the sensitivity of the BOM data. <br>
Risk: BOM comparisons, classifications, and completeness checks can affect procurement or engineering change decisions. <br>
Mitigation: Review generated reports and manually check unclassified or ambiguous items before using results for purchasing, build, or ECN decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/bom-toolkit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell commands and generated Excel or text report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes local BOM spreadsheets; Excel scripts require openpyxl.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
