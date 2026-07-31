## Description: <br>
Object-level building change detection between two epochs that identifies new, demolished, expanded, reduced, split, and merged buildings from footprint vectors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and construction auditors use this skill to compare before-and-after building footprint datasets and generate object-level change statistics and reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Auto-download and synthetic fallback modes can produce misleading change-audit results. <br>
Mitigation: Use user-supplied, temporally valid before-and-after building datasets for real audits, and treat synthetic-mode output as demonstration data. <br>
Risk: Dependency and provenance uncertainty can increase production or sensitive-workflow risk. <br>
Mitigation: Pin and review dependencies, review generated outputs, and confirm release provenance before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-building-change-audit) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Shell commands] <br>
**Output Format:** [GeoJSON, HTML report, JSON manifest, and command-line text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes building_changes.geojson, report.html, and output-manifest.json; synthetic mode may also write synthetic input GeoJSON files.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
