## Description: <br>
Batch query elevation data from the Open-Elevation public API by latitude/longitude coordinates, with CSV or JSON output and no API key required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to look up elevation for individual coordinates or CSV batches through the public Open-Elevation API. It can generate CSV or JSON elevation results for mapping, data enrichment, QA checks, and downstream geospatial workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports that coordinate lookup is legitimate but includes under-disclosed geocoding, local persistence, and generic download helpers beyond the advertised coordinate workflow. <br>
Mitigation: Review the bundled geocoding, cache, and downloader modules before deployment; remove unused helper code if only coordinate-based elevation lookup is needed. <br>
Risk: Using --place sends place names to Nominatim, and normal lookup sends coordinates to Open-Elevation. <br>
Mitigation: Avoid sensitive locations unless those third-party services are approved for the use case; prefer explicit coordinates when place-name geocoding is not required. <br>
Risk: The release has a suspicious security verdict from clawscan despite no individual risk findings. <br>
Mitigation: Treat installation as requiring review of the security summary and guidance, then deploy only in environments where outbound calls to Open-Elevation and Nominatim are acceptable. <br>
Risk: The release evidence and artifact license disagree: evidence reports MIT-0, while artifact/LICENSE contains MIT text. <br>
Mitigation: Confirm the intended license with the publisher or release owner before public distribution or enterprise reuse. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/open-elevation) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [Open-Elevation API](https://open-elevation.com/) <br>
- [Open-Elevation lookup endpoint](https://api.open-elevation.com/api/v1/lookup) <br>
- [NASA SRTM reference](https://www2.jpl.nasa.gov/srtm/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, API Calls] <br>
**Output Format:** [CLI text plus CSV or JSON result files; optional QA JSON sidecar for single-point lookup] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Coordinates are sent to Open-Elevation; place-name lookup can send place names to Nominatim; batch requests are chunked up to 100 points per API call.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
