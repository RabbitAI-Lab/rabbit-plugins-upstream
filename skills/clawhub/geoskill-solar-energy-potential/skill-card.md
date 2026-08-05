## Description: <br>
Calculate solar PV energy potential from NASA POWER solar radiation data, including annual GHI, optimal tilt angle, estimated PV output, and economic analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, energy analysts, and geospatial practitioners use this skill to estimate solar PV resource potential and economics for single sites or batches of coordinate-based locations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Latitude and longitude coordinates are sent to NASA POWER, and place-name lookup may send place names through additional resolver code. <br>
Mitigation: Use --lat and --lon for sensitive locations, avoid --place when location privacy matters, and confirm that any place resolver in the runtime environment is acceptable. <br>
Risk: The security review flags dependency posture as under-disclosed. <br>
Mitigation: Install in an isolated environment and pin numpy and requests to reviewed current versions before operational use. <br>
Risk: Solar and economic outputs are estimates and may omit local shading, terrain, soiling, financing, incentives, and microclimate effects. <br>
Mitigation: Use the results for screening and compare against detailed engineering tools or local measurements before making design or investment decisions. <br>


## Reference(s): <br>
- [Solar Energy Potential details](references/details.md) <br>
- [NASA POWER Project](https://power.larc.nasa.gov) <br>
- [NASA POWER Daily Point API](https://power.larc.nasa.gov/api/temporal/daily/point) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-solar-energy-potential) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Files, Guidance] <br>
**Output Format:** [Console text with optional JSON or CSV output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses coordinates or batch CSV input and returns solar resource, PV output, and economic metrics.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
