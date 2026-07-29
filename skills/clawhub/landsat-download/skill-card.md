## Description: <br>
Searches and downloads Landsat 8 and Landsat 9 Collection 2 Level 2 imagery through STAC, with filters for area, date, cloud cover, WRS-2 path/row, band selection, and safe partial-file downloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and geospatial analysts use this skill to find Landsat scenes for a bounding box and time window, inspect matching scene metadata, and download selected public Landsat assets for remote-sensing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release security review marked the package suspicious because it includes an unrelated credential manager with a hardcoded Earthdata password and local secret readers. <br>
Mitigation: Review before installing, remove or clearly scope the credential module, and avoid running in environments that contain sensitive .netrc or ~/.geoskill/secrets.json entries. <br>
Risk: The release security guidance notes an open-ended requests dependency range. <br>
Mitigation: Pin or otherwise tighten the requests dependency range before deployment. <br>
Risk: The downloader performs network requests and writes downloaded files to a local output directory. <br>
Mitigation: Run with intended network access only and choose an output directory where partial and final downloaded files are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/landsat-download) <br>
- [Microsoft Planetary Computer Landsat Collection 2 Level 2](https://planetarycomputer.microsoft.com/dataset/landsat-c2-l2) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1/) <br>
- [Element84 Earth Search API](https://earth-search.aws.element84.com/v1/) <br>
- [STAC specification](https://stacspec.org/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [CLI text or JSON results, plus downloaded Landsat asset files when download mode is enabled] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes selected assets to the configured output directory and may show progress, speed, and ETA during downloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
