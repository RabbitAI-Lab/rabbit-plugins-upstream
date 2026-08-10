## Description: <br>
Crawls satellite imagery metadata from Copernicus, USGS EarthExplorer, and Microsoft Planetary Computer, with filtering by bounding box, date range, cloud cover, and platform, and outputs CSV or JSON summaries with deduplication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Remote sensing professionals, developers, and analysts use this skill to search available satellite imagery metadata before downloading source imagery. It helps compare scenes by location, date, cloud cover, platform, and source, then export machine-readable results for follow-up analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow makes network requests to public satellite metadata services and may write result or cache files where configured. <br>
Mitigation: Review destination paths, cache settings, and network endpoints before use in restricted environments. <br>
Risk: The package evidence references a crawler script that is not present in the artifact files. <br>
Mitigation: Verify that the intended package or execution workflow supplies the crawler script before relying on the usage commands. <br>
Risk: The dependency declaration allows any requests version at or above 2.28.0. <br>
Mitigation: Pin or lock dependencies for reproducible deployments. <br>


## Reference(s): <br>
- [Copernicus Open Access Hub](https://scihub.copernicus.eu) <br>
- [USGS EarthExplorer](https://earthexplorer.usgs.gov) <br>
- [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-rs-metadata-crawler) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, code] <br>
**Output Format:** [Markdown with bash command examples and parameter descriptions; the described crawler outputs JSON or CSV metadata files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Metadata-only workflow; described outputs include scene identifiers, dates, cloud cover, path/row, footprints, statistics, and deduplicated result sets.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
