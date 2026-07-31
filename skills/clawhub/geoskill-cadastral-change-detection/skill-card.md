## Description: <br>
Topology-aware cadastral parcel change detection between two epochs, identifying new, deleted, expanded, reduced, split, and merged parcels from cadastral vector data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and land-administration teams use this skill to compare two locally supplied epochs of cadastral parcel vector data, audit boundary changes, detect split and merge events, and generate change ledgers and topology issue reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cadastral parcel inputs and generated reports may contain sensitive land or ownership data retained on local storage. <br>
Mitigation: Run the skill only in an approved local environment, choose a protected output directory, and clean up reports, manifests, logs, and spreadsheets according to the data handling policy. <br>
Risk: Unreviewed geospatial dependencies or floating dependency versions can introduce operational or supply-chain risk. <br>
Mitigation: Use a virtual environment or lockfile with reviewed versions of the required packages before running the skill. <br>
Risk: Incorrect CRS units or tolerance settings can produce misleading area and boundary-change classifications. <br>
Mitigation: Confirm the input coordinate reference system and configure geometry tolerances in the CRS units before using the results for review or reporting. <br>


## Reference(s): <br>
- [Cadastral business rules](artifact/references/cadastral_rules.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-cadastral-change-detection) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with CLI commands, plus generated GeoJSON, XLSX, CSV, JSON, HTML/PDF-style report, manifest, QA, and log files when the command is run.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires locally supplied before and after cadastral vector datasets; bbox, date-range, and AOI flags are present for CLI consistency but do not fetch data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
