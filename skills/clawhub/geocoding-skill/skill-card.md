## Description: <br>
Forward and reverse geocoding using Nominatim and Open-Meteo, including address-to-coordinate, coordinate-to-address, and batch CSV workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data practitioners use this skill to convert addresses and coordinate pairs for mapping, analysis, and batch data enrichment with Nominatim/OpenStreetMap and Open-Meteo. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive home, customer, or business address data may be sent to external geocoding providers. <br>
Mitigation: Avoid sensitive location data unless the external data flow is acceptable; document provider use and prefer approved or self-hosted endpoints for sensitive workloads. <br>
Risk: The release bundles unrelated credential-handling code with a hardcoded Earthdata password. <br>
Mitigation: Remove the bundled password and unrelated credential helpers, then rotate any exposed credential before relying on the skill. <br>
Risk: Dependency and runtime behavior may drift because dependencies are not tightly pinned. <br>
Mitigation: Pin dependencies to reviewed versions and scan the environment before installation or execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geocoding-skill) <br>
- [Nominatim](https://nominatim.org/) <br>
- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; runtime outputs can be CSV or JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call Nominatim or Open-Meteo and write local geocoding result files.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
