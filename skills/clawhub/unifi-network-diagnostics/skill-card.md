## Description: <br>
Diagnose a private household UniFi network for Operator and discover non-secret local helper configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[catholicbeer](https://clawhub.ai/user/catholicbeer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Household network owners and operators use this skill to diagnose UniFi Wi-Fi, internet, DNS, latency, packet loss, AP, switch, gateway, WAN, client connectivity, suspicious device behavior, and local helper setup issues with read-only checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local network diagnostics and UniFi helper queries can expose sensitive household network details if shared without review. <br>
Mitigation: Review diagnostic output before sharing it publicly; the skill requires redaction of secrets, local paths, MAC addresses, private topology, WAN IP addresses, tokens, cookies, API keys, and credential-like values. <br>
Risk: Remembering the local UniFi helper path writes local configuration outside the repository. <br>
Mitigation: Use the write option only after explicit owner approval and only when the owner wants the helper path remembered. <br>
Risk: Incorrect state-changing remediation could disrupt controller, gateway, AP, switch, DNS, DHCP, firewall, Wi-Fi, client, or system behavior. <br>
Mitigation: Require explicit owner approval before any state-changing action, including the exact action, expected effect, risk, and rollback or stop condition. <br>


## Reference(s): <br>
- [Diagnostic Model](references/diagnostic-model.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/catholicbeer/skills/unifi-network-diagnostics) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Structured Markdown assessment with observations, inferences, ranked hypotheses, confidence, unresolved questions, and a recommended next action.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Bundled diagnostics emit redacted JSON evidence; state-changing remediation is presented only after explicit owner approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence, released 2026-07-13T21:54:26Z) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
