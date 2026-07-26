## Description: <br>
This skill helps agents fetch comments from Douyin Creator Center through a CLI and batch send replies for selected videos. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lfp1979](https://clawhub.ai/user/lfp1979) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and agents managing a Douyin creator account use this skill to list comments on a selected video, identify comments that need replies, generate short reply text, and send batch responses through the creator-center CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically post public Douyin replies from a saved login session without a required preview or confirmation. <br>
Mitigation: Use a dedicated Douyin account or browser profile, inspect generated replies before sending, and avoid vague auto-reply prompts. <br>
Risk: Saved browser session data can provide account control to anyone with access to the skill profile directory. <br>
Mitigation: Protect the scripts/user-data profile and delete it when the automation is no longer needed. <br>
Risk: Failed replies may leave screenshots containing comment or account UI on disk. <br>
Mitigation: Review and delete failure screenshots after troubleshooting. <br>


## Reference(s): <br>
- [CLI reference](references/cli.md) <br>
- [Auto-reply workflow](references/auto-reply-workflow.md) <br>
- [Matching rules](references/matching-rules.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Douyin Creator Center comment management](https://creator.douyin.com/creator-micro/interactive/comment) <br>
- [ClawHub skill page](https://clawhub.ai/lfp1979/douyin-auto-reply) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, JSON, configuration] <br>
**Output Format:** [Markdown guidance with inline bash commands and JSON examples; the CLI emits single-line JSON results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a persistent Chromium profile for Douyin login state and can directly send public replies when the reply action is invoked.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and scripts/package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
