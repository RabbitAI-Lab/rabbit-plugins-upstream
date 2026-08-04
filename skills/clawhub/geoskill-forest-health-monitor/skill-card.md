## Description: <br>
Monitors forest canopy vitality decline, drought stress, pest damage, and wind throw from multi-temporal spectral indices using historical baselines, persistence state machines, and climate attribution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run or adapt a forest-health monitoring workflow for AOI or bbox-based anomaly assessment and field-sampling planning. Treat outputs as decision-support evidence only until real-data behavior is verified. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may present simulated forest-health outputs as operational analysis. <br>
Mitigation: Do not use outputs for operational, scientific, or regulatory forest-health decisions until real input data is required and synthetic output is clearly labeled. <br>
Risk: Documented download and place-based options may be unsupported or may use placeholder spatial inputs. <br>
Mitigation: Require explicit AOI or bbox inputs, verify the resulting dataset manifest, and confirm source imagery before relying on results. <br>
Risk: Overwrite protection may not be honored consistently. <br>
Mitigation: Run in a fresh output directory or preserve backups before using existing output paths. <br>


## Reference(s): <br>
- [Forest health schema](references/forest_health_schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash CLI examples; runtime outputs include GeoTIFF, GeoJSON, CSV, Parquet or CSV fallback, JSON manifests, and log text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Security evidence reports simulated outputs and unsupported real-data download options; review before operational use.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
