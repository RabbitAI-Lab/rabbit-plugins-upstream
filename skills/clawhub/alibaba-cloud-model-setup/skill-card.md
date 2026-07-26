## Description: <br>
Configure OpenClaw to use Alibaba Cloud Bailian provider (Pay-As-You-Go or Coding Plan) through a strict interactive flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[extraterrest](https://clawhub.ai/user/extraterrest) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to add, switch, or repair Alibaba Cloud Bailian model provider configuration in OpenClaw, including plan selection, site selection, API key handling, model selection, backup, and JSON validation. <br>

### Deployment Geography for Use: <br>
Global, subject to the selected Alibaba Cloud Bailian site and account eligibility. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify persistent OpenClaw configuration while handling API keys. <br>
Mitigation: Use it only when you intend to update OpenClaw configuration, prefer environment-variable API key storage, and inspect the resulting config and backup after running. <br>
Risk: Documented no-write and safety controls do not fully match the script behavior in this version. <br>
Mitigation: Do not rely on --list-models or --non-interactive as no-write safeguards; review the command path before execution. <br>


## Reference(s): <br>
- [OpenClaw Alibaba Cloud Bailian Configuration](references/openclaw_alibaba_cloud.md) <br>
- [ClawHub skill listing](https://clawhub.ai/extraterrest/skills/alibaba-cloud-model-setup) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or run a Python setup script that updates persistent OpenClaw configuration.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
