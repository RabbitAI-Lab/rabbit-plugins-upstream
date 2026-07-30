## Description: <br>
Checks whether an agent is using a NEAR AI Cloud TEE endpoint, reports configured and recently served models, and performs endpoint or message-level verification when the required verifier components are available. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eduv09](https://clawhub.ai/user/eduv09) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to check whether NEAR AI requests are routed to private TEE-backed endpoints, attest the current endpoint, and explain which privacy or verification level was actually reached. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Level 1 checks are informational and Level 2 attestation is point-in-time, so results can be overstated if reported without their evidence level. <br>
Mitigation: Report the exact level reached and preserve PASS, FAIL, and SKIP states; use Level 3 plugin evidence for message-specific proof. <br>
Risk: Optional dependency installation and the separate OpenClaw plugin can change the local environment. <br>
Mitigation: Ask for approval before running installation, prefer the skill's private virtual environment path, and review the plugin separately before enabling it. <br>
Risk: Gateway routes, third-party models, or fallback chains can send prompts outside a TEE. <br>
Mitigation: Use the served-model check and configure chains without non-TEE fallback models when prompts must remain inside the enclave. <br>


## Reference(s): <br>
- [ClawHub nearai-verify Skill Page](https://clawhub.ai/eduv09/skills/nearai-verify) <br>
- [OpenClaw / SmartClaws Homepage](https://github.com/skalenetwork/smartclaws) <br>
- [NEAR AI Cloud Verification](https://docs.near.ai/cloud/verification/) <br>
- [NEAR AI Cloud Private Inference](https://docs.near.ai/cloud/private-inference/) <br>
- [nearai-cloud-verifier](https://github.com/nearai/nearai-cloud-verifier) <br>
- [NEAR AI Endpoint Catalog](https://completions.near.ai/endpoints) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON output from bundled verification scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports CLAIMED, ATTESTED, PROVEN, FAILED, PASS, FAIL, or SKIP states depending on available checks and plugin evidence.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
