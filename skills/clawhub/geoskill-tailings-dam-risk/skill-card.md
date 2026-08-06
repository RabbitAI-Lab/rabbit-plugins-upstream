## Description: <br>
Screen tailings dam bodies, reservoir areas, catchments, and downstream exposure using remote sensing change detection, then produce patrol priorities based on hazard, exposure, and evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and dam-safety teams use this skill to screen tailings dam facilities, compare water-surface changes, estimate catchments and downstream exposure, and prioritize patrol review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can generate reports from synthetic fallback data when real inputs or downloads are missing. <br>
Mitigation: Provide real facility, DEM, and water-mask inputs for serious analysis, and treat synthetic or incomplete-data output as screening-only. <br>
Risk: Operational runs may access geospatial files, write local reports and caches, and optionally download public data. <br>
Mitigation: Run only in environments where those file writes, cache writes, and public data downloads are acceptable. <br>
Risk: Dependency drift can affect production behavior. <br>
Mitigation: Pin dependencies before production deployment. <br>


## Reference(s): <br>
- [risk_rules.json](references/risk_rules.json) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Guidance] <br>
**Output Format:** [GeoJSON, CSV, HTML, JSON, and log files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include facility changes, catchments, screening zones, downstream exposure statistics, a risk report, manifests, QA checks, and logs.] <br>

## Skill Version(s): <br>
2.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
