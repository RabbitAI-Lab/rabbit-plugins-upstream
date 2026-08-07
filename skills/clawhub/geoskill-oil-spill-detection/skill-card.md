## Description: <br>
Detects suspected oil slick candidates from SAR dark spots using wind, shape, texture, vessel, and natural slick signals for human review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run SAR dark-spot detection, rank suspected oil slick candidates, and produce review artifacts for environmental monitoring workflows. The outputs support triage and human review, not final attribution or regulatory determination. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make outbound requests to Microsoft Planetary Computer and cache downloaded imagery locally. <br>
Mitigation: Run it only where outbound satellite-data access and local storage are approved; set --cache-dir to a controlled location or clear ~/.geoskill_cache after use. <br>
Risk: Dependencies are not fully pinned, so future package changes could alter runtime behavior. <br>
Mitigation: Pin and review dependency versions before production deployment. <br>
Risk: SAR dark spots are not proof of an oil spill and may be caused by natural slicks, low wind, rain cells, or other conditions. <br>
Mitigation: Treat outputs as suspected candidates and require human review before operational, administrative, safety, or attribution decisions. <br>


## Reference(s): <br>
- [Oil spill detection factors](artifact/references/oil_spill_factors.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-oil-spill-detection) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Shell commands, Guidance] <br>
**Output Format:** [GeoJSON, CSV, NumPy or GeoTIFF raster, JSON manifests, PDF or text review report, and Markdown guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces candidate oil slick artifacts for human review; can use provided SAR inputs or download Sentinel-1 data when bbox and date-range arguments are supplied.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
