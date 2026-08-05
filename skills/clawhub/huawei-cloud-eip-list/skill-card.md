## Description: <br>
Lists Huawei Cloud EIP resources in a selected region with public IP address, EIP ID, status, bandwidth, associated instance, and creation time using KooCLI as the primary path and the Huawei Cloud EIP Python SDK as a fallback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and network engineers use this skill to inventory Huawei Cloud Elastic IP resources for discovery, cost review, compliance reporting, and connectivity troubleshooting. The skill is read-only and reports EIP details from the authenticated account and selected region. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses the user's configured Huawei Cloud credentials to query EIP inventory. <br>
Mitigation: Use a least-privilege IAM policy limited to public IP list and get permissions, and avoid broad account credentials unless they are explicitly required. <br>
Risk: EIP inventory can expose public IP addresses and cloud resource metadata. <br>
Mitigation: Run the skill only in trusted agent sessions where sharing regional EIP inventory is appropriate. <br>
Risk: Credential handling mistakes could disclose Huawei Cloud AK/SK values. <br>
Mitigation: Keep credentials in local hcloud configuration or Huawei Cloud environment variables, and do not paste AK/SK secrets into the conversation. <br>


## Reference(s): <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [EIP Policies](references/eip-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Data Flow Diagram](references/dataflow-diagram.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-eip-list) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, optional Python SDK code, and formatted EIP inventory results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include region-scoped EIP counts, IDs, public IP addresses, statuses, bandwidth data, associated instances, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
