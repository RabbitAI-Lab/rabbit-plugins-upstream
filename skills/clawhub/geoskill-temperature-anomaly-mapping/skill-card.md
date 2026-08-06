## Description:

Computes current-temperature anomalies against a multi-year climatology, standardizes them, classifies warm and cold anomaly levels, and outputs GeoTIFF rasters plus time-series JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers and geospatial analysts use this skill to run local temperature anomaly mapping for monthly or annual monitoring, extreme warm/cold event screening, and regional diagnostics from synthetic data or local multi-epoch temperature rasters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled helper code can use network services, read local credential stores, and write a home-directory cache even though the advertised mapper is local.

Mitigation: Install and test in an isolated environment; audit or remove unused helper modules; disable network access when running the offline anomaly-mapping workflow.

Risk: The package includes hardcoded Earthdata credentials.

Mitigation: Remove hardcoded credentials before use, rotate any exposed credentials, and provide required service credentials only through the user's own environment or secret-management process.

Risk: Dependencies are not pinned in the artifact requirements.

Mitigation: Pin and review dependency versions before commercial deployment, then install from a controlled lockfile or approved package mirror.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-temperature-anomaly-mapping)
- [SKILL.md](artifact/SKILL.md)
- [README.md](artifact/README.md)
- [LICENSE](artifact/LICENSE)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash commands; generated artifacts are GeoTIFF and JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes anomaly.tif, anomaly_class.tif, timeseries.json, and output-manifest.json to the selected output directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
