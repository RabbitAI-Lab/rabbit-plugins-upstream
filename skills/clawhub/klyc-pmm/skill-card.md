## Description:

KLYC-PMM helps agents manage persistent text memory through initialization, recovery tokens, memory synchronization, distillation, deduplication, search, and disaster recovery over HTTPS to kunlunyaochi.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sylncn](https://clawhub.ai/user/sylncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to initialize, sync, search, distill, back up, and recover long-lived text memory for AI agents. It is aimed at workflows such as customer service, operations, coding assistants, and personal assistants that need continuity across sessions or environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recovery URLs and API keys may expose access to the agent's memory if they are committed or shared.

Mitigation: Keep recovery URLs and API keys out of public repositories and shared MEMORY.md files; rotate or revoke exposed credentials where supported.

Risk: Watch and daemon modes can continuously upload selected workspace files to kunlunyaochi.com.

Mitigation: Enable background watching only for workspaces and files that are intended to be synchronized, and review watched paths before daemon installation.

Risk: Memory distillation can send memory content to DeepSeek when configured with the user's API key.

Mitigation: Run distillation only after confirming the memory content is appropriate for third-party LLM processing and the required API key is intentionally configured.

Risk: Paid upgrade flows may initiate payment-related interactions.

Mitigation: Review generated payment links and confirm the intended tier before continuing with upgrade commands.

Risk: Recovery and synchronization change local memory files and configuration.

Mitigation: Back up important local memory and configuration files before recovery, hook synchronization, or non-dry-run distillation.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/sylncn/skills/klyc-pmm)
- [Publisher profile](https://clawhub.ai/user/sylncn)
- [Kunlun Yaochi homepage](https://kunlunyaochi.com)
- [PMM full architecture](artifact/klyc-pmm/references/pmm-full-architecture.md)
- [Pay Skill packaging standard](artifact/klyc-pmm/references/pay-skill-spec.md)
- [SkillHub detail page](https://skillhub.cn/skills/syln/kunlunyaochi)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and shell-oriented instructions with local file and configuration updates when commands are executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke HTTPS API calls, local file watching, systemd user service installation, paid upgrade flows, and LLM-assisted memory distillation when the user runs the provided scripts.]

## Skill Version(s):

9.2.6 (source: frontmatter, artifact/klyc-pmm/skill.json, evidence release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
