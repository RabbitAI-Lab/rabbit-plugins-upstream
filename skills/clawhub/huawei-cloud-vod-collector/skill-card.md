## Description:

Captures poor Huawei Cloud developer experiences, sanitizes and deduplicates feedback, and prepares prioritized Voice of Developer reports or GitCode issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dev-skills-operator](https://clawhub.ai/user/dev-skills-operator)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to collect Huawei Cloud tool or service issues from agent sessions, preserve useful context, sanitize feedback, and deliver actionable product requirements or GitCode issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install persistent tools under the user's profile.

Mitigation: Review the installation path and installed tool before enabling the skill in a shared or sensitive environment.

Risk: Quality telemetry is used unless opted out.

Mitigation: Disable telemetry with the documented opt-out setting when telemetry is not appropriate.

Risk: A GitCode access token may be stored locally.

Mitigation: Protect the token file, avoid sharing the user profile, and remove the token when the integration is no longer needed.

Risk: Feedback delivery can send selected issue context to the configured GitCode repository.

Mitigation: Review or disable automatic hooks and avoid including secrets, personal data, or full conversation history in feedback files.

## Reference(s):

- [Hooks Setup](references/hooks-setup.md)
- [OpenClaw Integration](references/openclaw-integration.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [VoD Feedback Record Template](assets/VOD_FEEDBACKS.md)
- [VoD GitCode Issue Template](assets/VOD_ISSUE.md)
- [AtomGit-GO](https://gitcode.com/weixin_45218422/AtomGit-GO)
- [Huawei Cloud KooCLI Documentation](https://support.huaweicloud.com/cli/index.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown feedback files, GitCode issue content, JSON command results, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local .vod feedback records and may submit selected issue context to the configured GitCode repository.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
