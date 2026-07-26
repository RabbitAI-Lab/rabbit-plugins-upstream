## Description: <br>
Connects an AI agent to Danube's growing marketplace of services and tools through a single API key so the agent can discover, search, and execute available tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[danube](https://clawhub.ai/user/danube) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to connect an AI agent to Danube's marketplace, discover available services and tools, execute selected tools, and guide users through credential requirements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Danube API key can grant user-scoped read, execute, and write access through marketplace tools. <br>
Mitigation: Keep the API key private, scoped, and revocable; review each discovered tool's purpose and required parameters before running it. <br>
Risk: Marketplace tools can include operations that write or delete user-scoped resources. <br>
Mitigation: Confirm user intent before executing tools that modify resources, and inspect returned schemas and parameters before execution. <br>
Risk: External service credentials may be required for some tools. <br>
Mitigation: Direct users to configure credentials in the Danube dashboard and retry only after authorization is complete. <br>


## Reference(s): <br>
- [Danube homepage](https://danubeai.com) <br>
- [Danube documentation](https://docs.danubeai.com) <br>
- [Danube dashboard](https://danubeai.com/dashboard) <br>
- [ClawHub skill page](https://clawhub.ai/danube/skills/tools-marketplace) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash and JSON configuration blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and a user-scoped DANUBE_API_KEY for marketplace access.] <br>

## Skill Version(s): <br>
8.0.13 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
