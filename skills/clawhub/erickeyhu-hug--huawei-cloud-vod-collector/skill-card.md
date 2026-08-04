## Description: <br>
Captures poor Huawei Cloud developer experiences, turns them into structured Voice of Developer feedback records, and can deliver selected reports as GitCode issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to capture errors, rejected outputs, and user-reported Huawei Cloud issues, then preserve enough context to create actionable product feedback. Integrators can connect the skill to OpenClaw or Hermes hooks and configure delivery to a GitCode issue repository. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic feedback capture can include broad conversation context, including full-dialog or thinking fields. <br>
Mitigation: Review generated feedback files before delivery and remove sensitive or unnecessary dialog details. <br>
Risk: Feedback can be submitted to a configured GitCode repository outside the local workspace. <br>
Mitigation: Confirm the configured destination repository before running delivery commands. <br>
Risk: Auto-login uses AtomGit-GO and stores a local access token at ~/.atomcode/auth.toml. <br>
Mitigation: Treat the token file as sensitive, restrict access to the local environment, and delete it when it is no longer needed. <br>
Risk: Captured reports may contain secrets or credentials pasted into the session. <br>
Mitigation: Run the sanitizer and manually inspect reports before submission. <br>


## Reference(s): <br>
- [Hooks Setup](references/hooks-setup.md) <br>
- [OpenClaw Integration](references/openclaw-integration.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [VoD Feedback Record Template](assets/VOD_FEEDBACKS.md) <br>
- [GitCode Issue Template](assets/VOD_ISSUE.md) <br>
- [AtomGit-GO](https://gitcode.com/weixin_45218422/AtomGit-GO) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, Configuration, API Calls, Guidance] <br>
**Output Format:** [Markdown feedback records and issue text with supporting shell commands, JSON command responses, and YAML hook configuration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates .vod feedback files, updates feedback status in place, and may submit configured reports to GitCode.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
