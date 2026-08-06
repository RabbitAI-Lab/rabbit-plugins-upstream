## Description: <br>
Computes forest fire burn severity from pre/post-fire NIR and SWIR imagery using differenced Normalized Burn Ratio (dNBR), classifying areas into unburned, low, moderate, and high severity categories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and fire-response teams use this skill to assess burn severity, map fire damage, and generate burn severity reports from verified local NIR/SWIR GeoTIFFs or exploratory bbox/date imagery downloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Auto-download mode can produce burn-severity reports from unsuitable or heuristically assigned imagery. <br>
Mitigation: Prefer verified local pre-fire and post-fire NIR/SWIR GeoTIFFs; independently check downloaded bands, dates, alignment, and pre/post scene ordering before relying on results. <br>
Risk: AOI, bbox, and date-range queries may be sent to external imagery services and cached locally. <br>
Mitigation: Avoid sensitive locations in auto-download mode unless external-service use and cache handling have been reviewed. <br>
Risk: dNBR results can be misleading when rasters are misaligned, mismatched, low quality, or not true NIR/SWIR bands. <br>
Mitigation: Validate image provenance, band identity, CRS, alignment, nodata handling, and scene quality before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-forest-fire-burn-severity) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; execution produces an HTML report, JSON results, and a machine-readable output manifest.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on supplied pre/post-fire NIR and SWIR GeoTIFFs, synthetic demo inputs, or bbox/date auto-download parameters.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
