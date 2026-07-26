## Description: <br>
Monitors more than 50 bidding platforms and filters results to electricity-related tender notices only. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[powerzzjohn](https://clawhub.ai/user/powerzzjohn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement or operations staff use this skill to run scheduled or manual scans of bidding platforms for power-sector tender notices and prepare WeChat-ready summaries when matches are found. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: This release includes plaintext third-party account credentials and personal contact details in documentation and configuration files. <br>
Mitigation: Do not install or run this release until the exposed credentials are rotated, personal details are removed or redacted, and account-specific secrets are moved to a private secret store or environment-specific configuration. <br>


## Reference(s): <br>
- [Configuration Guide](references/config-guide.md) <br>
- [Website Inventory](references/gx_websites.json) <br>
- [ClawHub Skill Page](https://clawhub.ai/powerzzjohn/skills/gx-bidding-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated JSON or text result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces bidding_results_YYYYMMDD.json and, only when matches exist, wechat_msg_YYYYMMDD.txt.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
