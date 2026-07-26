## Description: <br>
炽风 guides agents through Linux fan-speed diagnosis and control using sensor checks, safer sysfs paths first, and lower-level EC methods only when needed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fslong520](https://clawhub.ai/user/fslong520) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and advanced Linux users can use this skill when diagnosing overheating systems and selecting a fan-control approach. It helps them inspect sensor data, identify safer fan interfaces first, and prepare commands or scripts for manual testing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Root-level writes to low-level fan or EC controls can destabilize hardware or create unsafe thermal behavior. <br>
Mitigation: Use read-only detection and vendor-supported tools first, avoid trial EC writes without device-specific validation and recovery access, and monitor temperatures continuously. <br>
Risk: Persistent fan overrides or autostarted control loops can preserve unsafe settings after testing. <br>
Mitigation: Do not enable autostart until the configuration has been safely tested, fan response has been verified, and a recovery path is available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fslong520/skills/blazefan) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Code, Configuration guidance] <br>
**Output Format:** [Markdown with inline bash and C code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include root-level hardware-control commands that require human review before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
