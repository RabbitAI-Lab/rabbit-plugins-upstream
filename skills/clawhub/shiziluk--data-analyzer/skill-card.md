## Description: <br>
Data Analyzer helps agents query sales data, generate sales and profit charts, analyze trends, and create PDF business reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shiziluk](https://clawhub.ai/user/shiziluk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to query packaged sales data, visualize sales or profit metrics, inspect profit trends, and assemble simple PDF business reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The PDF report function accepts a user-controlled chart path. <br>
Mitigation: Pass only chart images created for the intended report and review the PDF before sharing. <br>
Risk: Dependencies are not pinned in the artifact requirements. <br>
Mitigation: Pin pandas, matplotlib, and fpdf2 versions before controlled deployment. <br>
Risk: A stray HTML document is packaged with a .sh installer filename. <br>
Mitigation: Remove or rename that file before using installer workflows; do not execute it as a shell script. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shiziluk/skills/data-analyzer) <br>
- [Publisher profile](https://clawhub.ai/user/shiziluk) <br>


## Skill Output: <br>
**Output Type(s):** [text, image files, PDF files] <br>
**Output Format:** [Plain text responses with generated PNG charts and PDF reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes generated chart and report files to temporary local paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
