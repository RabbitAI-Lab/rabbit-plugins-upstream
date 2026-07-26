## Description: <br>
Analyzes sales data by answering queries, generating charts, producing trend insights, and exporting standardized PDF sales reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[goo2200](https://clawhub.ai/user/goo2200) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and business users can use this skill to query bundled sales data, create sales or profit visualizations, summarize trends, and assemble weekly PDF sales reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence marks the bundle suspicious due to credentialed production/SRE workflows with automatic memory persistence and possible git sync behavior. <br>
Mitigation: Review permissions before deployment, avoid granting production observability or admin credentials unless intended, and avoid configuring organization memory unless team-wide git sync and possible pushes are acceptable. <br>
Risk: Generated charts and reports are stored on the local filesystem and may persist after use. <br>
Mitigation: Run the skill in an isolated environment and review or clean generated files before sharing outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/goo2200/skills/data-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Analysis, Files] <br>
**Output Format:** [Plain text responses, PNG chart file paths, and PDF report file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Charts are written under /tmp and PDF reports under /tmp/sales_report.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
