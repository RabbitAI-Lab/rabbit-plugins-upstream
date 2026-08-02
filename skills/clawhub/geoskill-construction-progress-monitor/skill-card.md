## Description: <br>
Monitor construction progress from multi-temporal satellite imagery, classify project stages, detect stagnation, and generate progress reports for infrastructure projects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and project teams use this skill to run construction progress monitoring workflows from project boundaries, schedules, and multi-period imagery inputs. It supports stage classification, stagnation detection, and report generation for infrastructure tracking and timeline audits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Advertised satellite analysis may not match normal execution, which can generate simulated construction progress results. <br>
Mitigation: Treat outputs as decision support only; require real imagery inputs and review generated reports before audits, compliance reviews, payment decisions, or operational decisions. <br>
Risk: The skill can download remote imagery and write cached or output files when bbox/date inputs are used. <br>
Mitigation: Require explicit approval before remote data fetching, document cache and output locations, and use pinned dependencies in controlled environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-construction-progress-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with CLI examples; generated artifacts include GeoJSON, CSV, GeoTIFF, and JSON manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May fetch Sentinel-2 imagery when bbox/date inputs are used; can also run synthetic demo mode.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
