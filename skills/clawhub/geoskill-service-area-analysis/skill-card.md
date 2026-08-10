## Description: <br>
Computes network-based facility service areas, nearest-facility assignment, and multi-threshold coverage statistics, producing service area GeoJSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to compute service-area isochrones, assign locations to the nearest facility, and summarize coverage across travel-time thresholds from local or synthetic network inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes under-disclosed network and credential-handling code outside the main local service-area workflow. <br>
Mitigation: Review the package before installing and remove or clearly disclose bundled geocoding, download, home-directory cache, and credential-discovery helpers. <br>
Risk: Evidence security guidance reports hardcoded Earthdata credentials. <br>
Mitigation: Remove the credentials from the package and rotate any exposed credentials before release or deployment. <br>
Risk: Dependencies are not pinned. <br>
Mitigation: Pin dependency versions and review transitive packages before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-service-area-analysis) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [GeoJSON and JSON files with Markdown guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary artifacts include service_area.geojson, service_area_stats.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact openai.yaml and CHANGELOG list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
