## Description: <br>
Download daily, monthly, or climatology NASA POWER meteorological and solar data for points or regions worldwide without an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to retrieve NASA POWER solar and meteorological datasets for point locations, bounding boxes, or named places, then save the results for analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled credential helper includes hardcoded fallback credentials and references several unrelated API keys. <br>
Mitigation: Remove or neutralize bundled default credentials before deployment, rely on user-managed secrets or environment variables, and scan the release for secrets. <br>
Risk: Named-place lookup may send place names to third-party geocoding services, while the privacy notice focuses on NASA POWER requests. <br>
Mitigation: Use explicit latitude/longitude or bounding boxes for sensitive locations, and update user-facing privacy text to disclose geocoding requests. <br>
Risk: Runtime dependencies are specified with lower bounds rather than pinned versions. <br>
Mitigation: Install in an isolated environment and pin reviewed dependency versions or hashes for production workflows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-nasa-power-download) <br>
- [NASA POWER API](https://power.larc.nasa.gov/api/) <br>
- [NASA POWER Documentation](https://power.larc.nasa.gov/docs/) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, code, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands; downloaded data files are CSV, JSON, or optional QA JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes user-selected NASA POWER parameters and date ranges to local output paths; named-place lookup may contact external geocoding services.] <br>

## Skill Version(s): <br>
5.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
