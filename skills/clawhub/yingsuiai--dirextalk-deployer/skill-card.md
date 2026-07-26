## Description: <br>
Deploy, resume, verify, update, and destroy a Dirextalk server on AWS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yingsuiai](https://clawhub.ai/user/yingsuiai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to install the versioned npm deployer and manage the lifecycle of a Dirextalk server on AWS, including deployment, repair, verification, updates, and teardown. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The deployer can manage AWS infrastructure, DNS-related deployment steps, AWS credential profiles, and service-scoped local agent wiring. <br>
Mitigation: Review the npm package README and SKILL.md before use, confirm billing and domain prompts carefully, and prefer a dedicated temporary IAM user over root keys where possible. <br>
Risk: Deployment, update, and destroy commands can change or remove cloud resources. <br>
Mitigation: Run lifecycle commands only from the installed versioned deployer runtime after the required confirmations, and use status or verify commands before update or destroy operations. <br>
Risk: AWS secrets, agent tokens, private keys, generated credentials, or initialization codes could be exposed during setup. <br>
Mitigation: Keep secrets and generated credentials out of chat transcripts and avoid pasting or exposing them while following the deployment workflow. <br>


## Reference(s): <br>
- [dirextalk-deployer homepage](https://github.com/YingSuiAI/dirextalk-deployer) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated commands should be reviewed before execution because the deployment workflow can affect AWS infrastructure and local agent configuration.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
