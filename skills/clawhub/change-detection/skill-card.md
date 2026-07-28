## Description: <br>
Detects vegetation, urban, and water changes between time-separated satellite images using NDVI difference, image differencing, and Change Vector Analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to compare co-registered satellite imagery from two time periods, generate change magnitude and mask outputs, and produce change statistics for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Under-disclosed network fetching or place-resolution behavior may send data outside an expected local-only workflow. <br>
Mitigation: Review and disable network-backed fetch or place features unless they are required, approved, and configured for the deployment environment. <br>
Risk: Bundled hardcoded Earthdata credentials could expose shared secrets or create unauthorized access patterns. <br>
Mitigation: Remove bundled credentials before use and require user- or environment-supplied secrets through an approved secret-management path. <br>
Risk: Change maps can contain false positives when imagery is misregistered, cloud-contaminated, or cross-sensor imagery is not normalized. <br>
Mitigation: Use co-registered imagery with matching CRS and resolution, apply cloud masking, and review outputs before relying on the results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/change-detection) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands; generated artifacts may include GeoTIFF, GeoJSON, Shapefile, and JSON outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided, co-registered raster inputs and appropriate local geospatial dependencies.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
