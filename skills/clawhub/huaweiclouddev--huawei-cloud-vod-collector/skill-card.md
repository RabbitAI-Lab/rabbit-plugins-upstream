## Description: <br>
Captures Huawei Cloud developer feedback from errors, user rejections, and reports, records it as markdown feedback, and can deliver selected reports as GitCode issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and support engineers use this skill to collect poor Huawei Cloud experiences, extract useful context from failed actions or user reports, and prepare issue-ready Voice of Developer feedback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad automatic hooks can record tool errors, rejection-like prompts, and nearby conversation context. <br>
Mitigation: Review and narrow the hook configuration before enabling the skill, and disable automatic capture where sensitive conversations may occur. <br>
Risk: Feedback files may contain sensitive context, assistant thinking, or secrets before delivery. <br>
Mitigation: Inspect and redact .vod feedback files before submission, and use the sanitizer on existing records when needed. <br>
Risk: Delivery can install and run AtomGit-GO and store a local plaintext access token. <br>
Mitigation: Run the installer only after accepting the third-party dependency and token storage model, keep the token file private, and remove it when it is no longer needed. <br>
Risk: Reports can be submitted externally to GitCode. <br>
Mitigation: Confirm the configured repository and review each issue body before delivery or batch notification. <br>


## Reference(s): <br>
- [Hook configuration and deployment guide](references/hooks-setup.md) <br>
- [OpenClaw platform integration](references/openclaw-integration.md) <br>
- [AtomGit-GO](https://gitcode.com/weixin_45218422/AtomGit-GO) <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-vod-collector) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/huaweiclouddev) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance] <br>
**Output Format:** [Markdown feedback records, issue text, JSON command responses, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local .vod feedback files and may submit selected feedback to GitCode when configured and authorized.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
