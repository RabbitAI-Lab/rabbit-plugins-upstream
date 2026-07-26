## Description: <br>
Analyzes a bundled sales CSV dataset with question-based summaries, chart generation, and trend insights. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xilef999](https://clawhub.ai/user/xilef999) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to ask sales questions, generate sales or profit charts, and request trend commentary from the bundled sample CSV dataset. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs pandas and matplotlib into the execution environment. <br>
Mitigation: Install and run the skill in an isolated Python environment when reviewing or deploying it. <br>
Risk: Chart generation writes PNG files to the system temporary directory. <br>
Mitigation: Review generated chart files as local artifacts and manage temporary-directory retention according to local policy. <br>
Risk: The included publish.ps1 script can publish the skill using a logged-in ClawHub account. <br>
Mitigation: Run publish.ps1 only when intentionally publishing this release, and review the dry-run output before publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xilef999/skills/l3-sales-data-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [text, files] <br>
**Output Format:** [Plain text responses and PNG chart files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the bundled sales.csv dataset; chart generation writes PNG files to the system temporary directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
