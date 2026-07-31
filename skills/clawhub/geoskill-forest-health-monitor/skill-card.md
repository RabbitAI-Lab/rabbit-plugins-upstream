## Description: <br>
Monitor forest canopy vitality decline, drought stress, pest damage, or wind throw from multi-temporal spectral indices, distinguishing short-term fluctuations from persistent decline using historical baselines, persistence state machines, and climate attribution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, analysts, and developers use this skill to assess forest health anomalies, identify persistent decline zones, correlate anomalies with climate variables, and plan field sampling from AOI or bounding-box inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Outputs may be simulated or based on placeholder named-place handling rather than validated real-data ingestion. <br>
Mitigation: Treat results as demo or simulated analysis until real imagery ingestion, geocoding, and AOI handling are validated for the target workflow. <br>
Risk: Forest-health classifications and pest or disease attribution may be incorrect without field evidence. <br>
Mitigation: Use outputs to prioritize review and sampling, not as a final regulatory, safety, or operational determination; confirm important findings with field data. <br>
Risk: Documented command examples may not match the actual script behavior. <br>
Mitigation: Run a controlled smoke test and inspect request, QA, manifest, and log outputs before relying on the workflow for production data. <br>


## Reference(s): <br>
- [Forest health schema](references/forest_health_schema.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-forest-health-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, files] <br>
**Output Format:** [Markdown guidance with CLI commands; generated artifacts include GeoTIFF, GeoJSON, CSV, Parquet, JSON manifests, QA JSON, and logs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should be reviewed as analysis support and validated against real AOI, imagery, geocoding, and field data before decisions.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
