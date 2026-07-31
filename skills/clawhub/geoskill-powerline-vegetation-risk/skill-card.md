## Description: <br>
Identifies vegetation encroachment, rapid growth, and tree fall risks along powerline corridors and generates prioritized inspection points. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and utility vegetation-management teams use this skill to screen powerline corridor vegetation, assess tree fall hazards, and prioritize inspection or maintenance routes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can contact an external satellite-data service and use locations as search parameters. <br>
Mitigation: Use local input files for sensitive locations or require explicit approval before network-based data retrieval. <br>
Risk: Automatic data-download behavior is under-disclosed relative to the main analysis flow. <br>
Mitigation: Document the data flow clearly and add an explicit network opt-in flag before deployment in restricted environments. <br>
Risk: Dependencies are not pinned. <br>
Mitigation: Pin dependencies and review them before installing in production or sensitive environments. <br>


## Reference(s): <br>
- [Risk scoring schema](references/risk_scoring.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-powerline-vegetation-risk) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI examples and generated analysis files including GeoJSON, GeoTIFF, CSV, and JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces risk points, high-risk line segments, clearance raster data, inspection priorities, request metadata, output manifest, and QA checks.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
