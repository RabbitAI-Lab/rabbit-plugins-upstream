## Description: <br>
Manifest helps OpenClaw users set up a smart LLM router that routes requests to cost-effective models and tracks usage, costs, and health. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to install and configure the Manifest router, choose local or cloud mode, and understand the usage, cost, and health tools available to an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud mode can process routing and usage metadata outside the local machine. <br>
Mitigation: Use local mode for sensitive work unless Manifest Cloud handling routing and usage metadata is acceptable, and review Manifest security, privacy, and account terms before enabling cloud mode. <br>
Risk: Setup and uninstall commands modify OpenClaw plugin configuration and restart the gateway. <br>
Mitigation: Review commands before running them and confirm the target OpenClaw environment and credentials before making changes. <br>


## Reference(s): <br>
- [Manifest documentation](https://github.com/mnfst/manifest) <br>
- [Manifest homepage](https://manifest.build) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with bash command blocks and tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes local and cloud setup guidance, OpenClaw plugin commands, and agent-facing usage, cost, and health tool descriptions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
