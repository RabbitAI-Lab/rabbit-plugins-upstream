## Description: <br>
Crawls satellite imagery metadata from Copernicus, USGS EarthExplorer, and Microsoft Planetary Computer with search filters, statistics, deduplication, and JSON/CSV export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and remote-sensing practitioners use this skill to find available satellite scenes by area, date range, platform, source, and cloud cover before deciding what imagery to download or analyze. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Embedded fallback Earthdata credentials and local credential readers may expose secrets or create unexpected credential use. <br>
Mitigation: Remove embedded credentials, rotate any exposed account credentials, require user-supplied credentials through documented environment, netrc, or secrets-file paths, and review local credential reads before installation. <br>
Risk: Place-name searches may send location text to geocoding services. <br>
Mitigation: Use explicit bounding boxes for sensitive locations and document when external geocoding services are contacted. <br>
Risk: An unpinned requests dependency can reduce install reproducibility and complicate vulnerability review. <br>
Mitigation: Pin dependency versions or provide a lockfile for reviewed releases. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/rs-metadata-crawler) <br>
- [Copernicus Open Access Hub](https://scihub.copernicus.eu) <br>
- [USGS EarthExplorer](https://earthexplorer.usgs.gov) <br>
- [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, CSV, Files, Shell commands] <br>
**Output Format:** [CLI text summaries plus JSON or CSV result files; optional JSON QA sidecar.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Metadata only; outputs scene identifiers, dates, cloud cover, footprints, statistics, and deduplicated merged records without downloading satellite imagery.] <br>

## Skill Version(s): <br>
0.3.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
