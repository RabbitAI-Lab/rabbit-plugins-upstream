## Description: <br>
Check whether this agent is talking to a NEAR AI Cloud TEE endpoint or to an ordinary one, and cryptographically attest that endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eduv09](https://clawhub.ai/user/eduv09) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect whether an OpenClaw agent is configured to use NEAR AI Cloud TEE endpoints, whether recent turns were served by private endpoints, and whether a direct NEAR endpoint can be attested as genuine TEE hardware. It is useful before handling sensitive data or when a user asks for privacy or TEE proof. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: CLAIMED results are based on local configuration, logs, and public endpoint catalog data rather than cryptographic proof. <br>
Mitigation: Treat CLAIMED results as configuration evidence only and rely on ATTESTED only when the cryptographic checks pass. <br>
Risk: The skill may read OpenClaw config/log metadata, contact NEAR, Intel, and NVIDIA attestation services, and optionally create a local virtual environment. <br>
Mitigation: Run it only when those local reads, network calls, and confirmed local installation steps are acceptable for the environment. <br>
Risk: A partial attestation with skipped checks does not prove the endpoint is genuine TEE hardware. <br>
Mitigation: Report skipped checks explicitly, use the doctor command to identify missing packages or network access, and avoid treating the endpoint as private unless full attestation succeeds. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/eduv09/skills/nearai-verify) <br>
- [OpenClaw homepage](https://github.com/skalenetwork/smartclaws) <br>
- [NEAR AI Cloud verification](https://docs.near.ai/cloud/verification/) <br>
- [NEAR AI Cloud private inference](https://docs.near.ai/cloud/private-inference/) <br>
- [nearai-cloud-verifier](https://github.com/nearai/nearai-cloud-verifier) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports CLAIMED, ATTESTED, FAILED, or skipped checks; optional scripts can read local OpenClaw config/log metadata, contact NEAR/Intel/NVIDIA attestation services, and create a private local venv after confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
