## Description: <br>
Turn a scrape, dataset, or endpoint into a priced API that other agents and people can pay per call. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[structureintelligence](https://clawhub.ai/user/structureintelligence) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data publishers use this skill to deploy a live data-serving app, publish a priced API manifest, verify the charge path, and guide callers through quoted, metered requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill authenticates with SettleMesh and may cache a reusable session while creating or managing paid public APIs. <br>
Mitigation: Use a scoped key when possible, review session persistence, and run logout or cleanup steps if deployed services or credentials should not persist. <br>
Risk: Pricing manifests and published endpoints can expose paid API behavior or billing effects if reviewed incorrectly. <br>
Mitigation: Review the pricing manifest before publishing, confirm payment capability with SettleMesh checks, and require explicit human confirmation for spending or credential-lending actions. <br>


## Reference(s): <br>
- [Sell Live Dataset ClawHub listing](https://clawhub.ai/structureintelligence/skills/sell-live-dataset) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash commands and pricing manifest guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the settlemesh CLI and SETTLE_API_KEY; suggested commands make authenticated, metered network calls to SettleMesh.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
