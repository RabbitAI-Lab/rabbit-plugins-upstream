## Description:

Give your agent a phone number. Amber answers calls, places confirmed outbound calls, completes phone tasks, logs transcripts, and exposes MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[batthis](https://clawhub.ai/user/batthis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and MCP-capable agent users use Amber to add real phone workflows to an agent, including inbound screening, confirmed outbound calling, contact lookup, calendar scheduling, message capture, call history, and transcript review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real calls, caller transcripts, contacts, CRM records, and calendar activity may expose private communications data.

Mitigation: Install only in a trusted local environment, configure caller AI/logging notice, define retention and deletion practices, and keep the dashboard and MCP server local or behind authentication.

Risk: Provider credentials can authorize phone, AI, and gateway activity.

Mitigation: Use least-privilege Twilio, OpenAI, and OpenClaw credentials dedicated to this runtime and rotate or revoke them when no longer needed.

Risk: Outbound calls and calendar writes can create real-world side effects.

Mitigation: Require explicit confirmation for outbound calls and calendar creation, and escalate payment, deposit, contract, medical, legal, financial, or irreversible commitments to the human operator.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/batthis/skills/amber-phone-agent)
- [Publisher profile](https://clawhub.ai/user/batthis)
- [Amber skill documentation](artifact/SKILL.md)
- [Hermes wrapper skill](artifact/skills/amber-phone-agent/SKILL.md)
- [Architecture](artifact/references/architecture.md)
- [Release checklist](artifact/references/release-checklist.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and MCP tool result text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include call preparation details, call history summaries, contact lookup results, calendar availability, setup steps, and local runtime health checks.]

## Skill Version(s):

5.5.50 (source: server-resolved release metadata, runtime package.json, and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
