## Description: <br>
Calculate solar PV energy potential from NASA POWER solar radiation data. Computes annual GHI, optimal tilt angle, estimated PV output, and economic analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and energy analysts use this skill to estimate solar PV potential for one location or a batch of locations from NASA POWER radiation data. It supports feasibility screening with annual GHI, tilt, PV output, capacity factor, payback, and LCOE estimates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill bundles credential-handling code and checks user-level credential locations that are not central to the solar calculation. <br>
Mitigation: Review the package before installing in environments with ~/.netrc, ~/.geoskill/secrets.json, or service API keys, and remove unrelated credential helpers if they are not required. <br>
Risk: Location lookup behavior can send place names or coordinates to external geocoding and NASA POWER services. <br>
Mitigation: Disclose the external providers used, avoid submitting sensitive locations, and prefer explicit latitude and longitude when privacy matters. <br>
Risk: Solar and economic results are screening estimates and may miss local shading, terrain, soiling, microclimate, financing, incentives, or degradation effects. <br>
Mitigation: Use results for preliminary assessment only and validate project decisions with site-specific engineering and financial analysis. <br>


## Reference(s): <br>
- [ClawHub Skill Release](https://clawhub.ai/ruiduobao/skills/solar-energy-potential) <br>
- [NASA POWER API Endpoint](https://power.larc.nasa.gov/api/temporal/daily/point) <br>
- [NASA POWER Project](https://power.larc.nasa.gov) <br>
- [Skill Details](references/details.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with command examples plus JSON or CSV assessment outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include single-location or batch solar metrics and economic estimates.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
