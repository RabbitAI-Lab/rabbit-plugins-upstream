## Description: <br>
Deploy a full-stack app to a live public URL with SettleMesh login, managed database setup, runtime API key wiring, and billing support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[structureintelligence](https://clawhub.ai/user/structureintelligence) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and product teams use this skill to deploy agent-built web apps, APIs, static sites, Next.js apps, container services, or full-stack projects to a public SettleMesh URL without separately wiring hosting, authentication, database setup, runtime secrets, and billing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can authenticate with SettleMesh and deploy public, metered applications. <br>
Mitigation: Use it only when deployment through SettleMesh is intended, confirm spending-related actions, and verify the target app, billing state, and generated public URL before relying on the deployment. <br>
Risk: Deployment may upload source code and use credentials or cached authentication. <br>
Mitigation: Review the project for sensitive files, keep SETTLE_API_KEY and runtime secrets out of uploaded source, and use declared secret injection for container apps. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/structureintelligence/skills/ship-paid-app) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and deployment guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the settlemesh CLI and SETTLE_API_KEY or a cached SettleMesh login session; deployment can publish source to a public run.settlemesh.io URL and may create metered platform usage.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
