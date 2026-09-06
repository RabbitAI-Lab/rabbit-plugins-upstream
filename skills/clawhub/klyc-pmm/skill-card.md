## Description:

KLYC-PMM helps agents initialize, restore, search, distill, and synchronize long-term text memory through a remote KLYC memory service with HTTPS API calls, local configuration, and optional file-watching automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sylncn](https://clawhub.ai/user/sylncn)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to give AI agents persistent text memory, recovery by KLYC token, semantic search, backup, distillation, and optional file-change synchronization. It is aimed at long-running assistant, customer support, operations, coding, and personal-assistant workflows that can accept remote service calls and local configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends and retrieves memory data through a remote memory service and handles sensitive recovery URLs and API keys.

Mitigation: Review the data flow before use, configure only trusted endpoints, and keep recovery URLs and API keys out of MEMORY.md, chat logs, shell history, and repositories.

Risk: The skill can install persistent file watching and synchronization behavior.

Mitigation: Run the read-only quickstart or self-test first, scope watched files deliberately, and do not run oneclick.sh or install-daemon.sh as root unless a system-wide daemon is intended.

Risk: The skill includes payment-related prompts and upgrade flows.

Mitigation: Confirm the intended service tier and payment link with the user before proceeding, and stop if the required payment extension or manual approval path is unavailable.

Risk: The distillation workflow can use a third-party LLM API key and send candidate memory content for semantic judgment.

Mitigation: Use a dedicated API key, preview with dry-run behavior when available, and avoid distilling content that should not leave the local environment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sylncn/skills/klyc-pmm)
- [KLYC Homepage](https://kunlunyaochi.com)
- [PMM Full Architecture](artifact/references/pmm-full-architecture.md)
- [Pay Skill Spec](artifact/references/pay-skill-spec.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct the agent to run local shell scripts that create configuration files, install a user daemon, call HTTPS APIs, and update local memory files.]

## Skill Version(s):

9.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
