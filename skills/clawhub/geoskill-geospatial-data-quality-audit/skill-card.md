## Description: <br>
Unified geospatial data quality audit for GIS data packages that checks raster, vector, table, NetCDF, and directory structure and produces JSON/HTML reports, issue layers, checksums, and machine-readable exit codes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, data engineers, and GIS teams use this skill to audit local geospatial data deliveries for readability, CRS, nodata, geometry, encoding, companion-file, and cross-file consistency issues before accepting or sharing packages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML reports may be unsafe to open when created from untrusted input data. <br>
Mitigation: Audit trusted or sandboxed data packages first and avoid opening generated HTML reports from untrusted inputs until report escaping is confirmed fixed. <br>
Risk: The audit writes or overwrites local report files in the selected output directory. <br>
Mitigation: Use a dedicated output directory for each run and review existing files before running the tool. <br>
Risk: The release depends on the unresolved geoskill-data-fetcher package. <br>
Mitigation: Review and pin the dependency in an isolated environment before relying on the skill. <br>
Risk: Compliance or certification conclusions require human review. <br>
Mitigation: Treat the audit outputs as evidence for review rather than final certification. <br>


## Reference(s): <br>
- [QA Rules Reference](references/rules.md) <br>
- [ClawHub release page](https://clawhub.ai/ruiduobao/skills/geoskill-geospatial-data-quality-audit) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Analysis, Files] <br>
**Output Format:** [Markdown guidance plus CLI-generated JSON, HTML, GeoJSON, text checksum, and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The audit CLI can emit qa-report.json, qa-report.html, qa.json, spatial_issues.geojson, checksums.txt, output-manifest.json, and exit codes for automation.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
