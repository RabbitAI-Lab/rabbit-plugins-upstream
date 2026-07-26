## Description: <br>
Query real-time road conditions, closures, and traffic issues in Norway. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[geoffreycasaubon](https://clawhub.ai/user/geoffreycasaubon) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to check Norwegian road closures, barriers, and route conditions when planning travel or responding to road-status questions. It is focused on official NVDB road data for Norway and can return current summaries or JSON for further analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts the public NVDB road-data service when it checks conditions. <br>
Mitigation: Use it only in environments where outbound access to the public NVDB API is acceptable. <br>
Risk: Road-condition results may omit current traffic, weather, or safety-critical incidents. <br>
Mitigation: Verify safety-critical travel decisions with official live road sources before acting. <br>


## Reference(s): <br>
- [Norway Roads API Reference](references/api-docs.md) <br>
- [Statens Vegvesen NVDB API](https://nvdbapiles-v3.atlas.vegvesen.no) <br>
- [ClawHub Skill Page](https://clawhub.ai/geoffreycasaubon/skills/norway-roads) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Plain text road-condition summaries or JSON returned from a CLI command] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires outbound HTTPS access to the public NVDB API; no API key is documented.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
