## Description: <br>
Your pet dies if you don't write. Adopt a virtual tamagotchi, journal daily to keep it alive, earn tokens on Base. One command to start, no wallet needed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dxdleady](https://clawhub.ai/user/dxdleady) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to set up a DiaryBeast pet, journal through the service, check pet status, interact with shop and wall endpoints, and maintain streak-based rewards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a third-party online diary service and sends journal content to DiaryBeast. <br>
Mitigation: Avoid secrets, highly sensitive personal details, or identifying information in entries, and review any public excerpt before posting. <br>
Risk: Setup stores a DiaryBeast session token locally under the OpenClaw workspace. <br>
Mitigation: Run setup only after reviewing the visible script, protect the local workspace, and re-authenticate intentionally when the session expires. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dxdleady/skills/openclaw-skill) <br>
- [DiaryBeast Homepage](https://diarybeast.xyz) <br>
- [DiaryBeast App](https://dapp.diarybeast.xyz) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash and curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Setup can create local DiaryBeast address and token files under the OpenClaw workspace.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
