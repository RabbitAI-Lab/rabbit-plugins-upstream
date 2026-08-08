## Description: <br>
Topology-aware cadastral parcel change detection between two epochs that identifies new, deleted, expanded, reduced, split, and merged parcels from cadastral vector data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and land administration teams use this skill to compare two local parcel vector datasets and produce change layers, ledgers, topology issue reports, and audit artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cadastral and ownership datasets may contain sensitive local records that should not be broadly exposed. <br>
Mitigation: Run the skill in an approved local environment, use a private --output-dir, and review generated reports and manifests before sharing them. <br>
Risk: Incorrect CRS units, geometry validity issues, thresholds, or matching parameters could lead to misleading parcel-change conclusions. <br>
Mitigation: Review qa.json and the audit report, use CRS-appropriate tolerance values, validate business rules, and require human review before using outputs for legal, administrative, or compensation decisions. <br>
Risk: Unpinned runtime dependencies can change behavior across installations. <br>
Mitigation: Use pinned or locked dependency versions for production deployments. <br>


## Reference(s): <br>
- [Default cadastral business rules](references/cadastral_rules.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-cadastral-change-detection) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with CLI commands plus GeoJSON, XLSX or CSV, CSV, JSON manifests, HTML/PDF-like audit report, and log files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes outputs to a local output directory and records request, dataset, QA, output manifest, and run log files.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
