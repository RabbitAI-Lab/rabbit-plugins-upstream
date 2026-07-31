## Description: <br>
Geoskill: 地理数据质量审计 audits local GIS data packages across raster, vector, table, NetCDF, LAS, and document files and produces JSON/HTML reports, issue layers, checksums, and exit codes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, data engineers, and GIS analysts use this skill to validate local geospatial data deliveries, identify CRS, nodata, geometry, encoding, companion-file, and cross-file consistency issues, and generate QA artifacts for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Parsing untrusted geospatial files can expose the runtime to malformed data handled by GIS dependencies. <br>
Mitigation: Run audits on trusted datasets or inside a sandbox, and pin and review dependency versions for geoskill-data-fetcher, Fiona, NumPy, rasterio, netCDF4, and Shapely. <br>
Risk: Quality findings and QA scores can be incomplete when optional GIS dependencies are missing or when compliance conclusions are needed. <br>
Mitigation: Install the optional deep-check dependencies for the target formats and require human review before using results for certification or compliance decisions. <br>


## Reference(s): <br>
- [QA Rules Reference](references/rules.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-geospatial-data-quality-audit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated audit artifacts include JSON, HTML, GeoJSON, text checksums, a manifest, and machine-readable exit codes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Operates on a local input directory and can optionally generate HTML, issue GeoJSON, checksums, custom-rule output, and synthetic demo data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
