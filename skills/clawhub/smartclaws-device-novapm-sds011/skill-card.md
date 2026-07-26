## Description: <br>
Device contract for a NovaPM/SDS011 air-quality bridge. Defines SmartClaws telemetry topics, payloads, local serial behavior, and safety rules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eduv09](https://clawhub.ai/user/eduv09) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this device contract to connect a NovaPM/SDS011 particulate-matter sensor to SmartClaws telemetry workflows and to guide bridge and master agents when reading, validating, and interpreting PM2.5 and PM10 data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incorrect or stale particulate readings could mislead air-quality status responses. <br>
Mitigation: Reject invalid ranges and physically inconsistent PM values, publish no telemetry for invalid frames, and report timestamps so stale data is visible. <br>
Risk: Unexpected command channels could change the read-only safety posture of the device contract. <br>
Mitigation: Treat incoming channels or command topics as setup errors unless an operator explicitly changes the device contract. <br>
Risk: Higher-impact development or staff workflows may require extra confirmation before writes. <br>
Mitigation: Follow the security guidance by confirming the target, account, deployment, dry-run output, and any requested signoff before allowing writes. <br>


## Reference(s): <br>
- [SmartClaws project homepage](https://github.com/skalenetwork/smartclaws) <br>
- [ClawHub skill page](https://clawhub.ai/eduv09/skills/smartclaws-device-novapm-sds011) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Markdown, JSON] <br>
**Output Format:** [Markdown guidance with JSON telemetry examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defines telemetry topics, payload fields, validation rules, and read-only operating constraints for agent use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
