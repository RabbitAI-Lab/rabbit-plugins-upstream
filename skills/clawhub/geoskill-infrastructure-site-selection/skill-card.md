## Description: <br>
Multi-criteria suitability analysis for infrastructure site selection, including raster comparison, index computation, and assessment report generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and planning teams use this skill to run suitability analysis for infrastructure site selection from slope, land-cover, road-proximity, elevation, bbox, or AOI inputs. It helps generate machine-readable statistics, an HTML report, and a run manifest for site-assessment workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: BBox or AOI-based runs may contact Microsoft Planetary Computer and cache downloaded public geospatial data locally. <br>
Mitigation: Run the skill in an environment where outbound data access and cache locations are acceptable, or provide local elevation data to avoid auto-download behavior. <br>
Risk: Unpinned dependencies can reduce reproducibility across deployments. <br>
Mitigation: Use pinned dependency versions or a lockfile in controlled or production deployments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-infrastructure-site-selection) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples; generated artifacts include JSON, HTML, and manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI writes outputs to a local directory and may cache downloaded public geospatial data when bbox or AOI inputs are used.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and CLI --version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
