## Description: <br>
Multi-platform bidding monitor: scan 50+ sites and filter power/electric bidding notices only. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[powerzzjohn](https://clawhub.ai/user/powerzzjohn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and procurement operators use this skill to scan Chinese procurement and bidding platforms, then filter notices to power and electric industry opportunities. It supports daily rotation, category-specific scans, all-category scans, and auth-required platform review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill scans many external procurement domains through a browser workflow. <br>
Mitigation: Review the configured domains before use and run only the categories needed for the current monitoring task. <br>
Risk: Auth-required platforms may require account credentials, and the artifact documents optional account and password fields in gx_websites.json. <br>
Mitigation: Keep real credentials out of shared source files; prefer environment variables or a private local config with restrictive file permissions. <br>
Risk: Procurement sites may restructure pages, which can reduce result completeness or parsing accuracy. <br>
Mitigation: Periodically verify platform accessibility and update gx_websites.json when site URLs or login flows change. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/powerzzjohn/skills/bid-monitor) <br>
- [Configuration Guide](references/config-guide.md) <br>
- [GX Website List](references/gx_websites.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Console text plus local JSON results and optional Markdown-ready message text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Saves dated bidding_results JSON files and optional wechat_msg text files under the OpenClaw workspace.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
