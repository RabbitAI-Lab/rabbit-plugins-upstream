## Description: <br>
Download current, historical, and forecast air quality data for common pollutants from Open-Meteo, with CSV or JSON outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to retrieve air quality measurements and forecasts for selected coordinates, places, dates, pollutants, and aggregation levels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports unrelated bundled credential-handling code with a plaintext Earthdata password and local secret readers. <br>
Mitigation: Remove or clearly justify the credential module, rotate the exposed credential, and require secrets to be supplied through documented runtime configuration. <br>
Risk: The skill may send coordinates, place names, date ranges, and pollutant selections to third-party air quality or geocoding services. <br>
Mitigation: Document the privacy behavior clearly and avoid submitting sensitive locations unless the user has approved those external requests. <br>
Risk: The security guidance calls for tighter dependency constraints. <br>
Mitigation: Pin or bound runtime dependencies and review dependency updates before release. <br>


## Reference(s): <br>
- [Open-Meteo Air Quality API documentation](https://open-meteo.com/en/docs/air-quality-api) <br>
- [Open-Meteo](https://open-meteo.com/) <br>
- [WAQI API](https://api.waqi.info/) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/air-quality-download) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Files, JSON, CSV] <br>
**Output Format:** [Markdown guidance with bash command examples; CSV or JSON data files when the CLI is executed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write optional QA summary JSON files next to generated outputs.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
