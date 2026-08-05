## Description: <br>
Helps users choose aperture and shutter speed together based on desired depth of field, motion rendering, and balanced exposure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bianchunhui](https://clawhub.ai/user/bianchunhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Photographers and photography-learning agents use this skill to explain how aperture and shutter speed affect exposure, depth of field, and motion effects, then recommend concrete aperture and shutter combinations. It is intended for exposure-parameter decisions, not light-meter compensation, film selection, or pure gear-spec lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can be misapplied to light-meter compensation, film or ISO selection, or pure camera-gear questions. <br>
Mitigation: Use the documented boundaries and route those requests to a more specific skill or answer them as general knowledge. <br>
Risk: Book-derived examples include film-era assumptions and may omit modern digital ISO and sensor-noise tradeoffs. <br>
Mitigation: When advising digital-camera users, mention ISO and sensor-noise considerations as context without changing the skill's aperture-shutter decision focus. <br>
Risk: Incorrect exposure recommendations could produce unusable photos in unusual lighting or motion conditions. <br>
Mitigation: Ask for scene context when needed and frame recommendations as starting points to verify with metering, test shots, or exposure preview. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/bianchunhui/nyip-photography-skills/tree/main/exposure-dual-control) <br>
- [ClawHub skill page](https://clawhub.ai/bianchunhui/skills/exposure-dual-control) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text] <br>
**Output Format:** [Markdown or plain text photography guidance with aperture and shutter speed recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include concrete f-stop and shutter-speed pairings plus short rationale for creative effect.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and test-prompts.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
