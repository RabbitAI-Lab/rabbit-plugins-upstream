## Description:

Turn final manuscript or course text into ordered chapter audio with one consistent narrator, live price estimates, a representative pilot, and focused refinements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, audiobook producers, and developers use this skill to convert final manuscripts or course text into chapterized audiobook audio. It supports intake, pronunciation planning, narrator selection, pilot approval, paid Beatra speech generation, delivery tracking, and focused corrections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to Beatra and stores a shared Device Token for account access.

Mitigation: Use the bundled authorization helper, keep the token only in the private credential file, and never expose it in chat, logs, command arguments, or copied files.

Risk: Approved voice cloning, speech synthesis, and cover generation can spend Beatra credits.

Mitigation: Require a current production card and explicit approval for each paid step, then submit each approved request once with durable task tracking.

Risk: Automatic package updates are enabled by default for this installation.

Mitigation: Review the update behavior before installing and disable silent checks with `python3 scripts/mcp_client.py update --auto off` when automatic replacement is not desired.

Risk: The bundled client sends installation and platform metadata during Beatra operations.

Mitigation: Treat use as an account-connected workflow and review the skill's security summary, registration behavior, and disconnect path before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/ai-audiobook-narration)
- [Beatra skill homepage](https://beatra.ai/skills/ai-audiobook-narration)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Chapter production](references/chapter-production.md)
- [Delivery and recovery](references/delivery-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Performance, cost, and quality](references/performance-and-quality.md)
- [Tasks and results](references/tasks-and-results.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Text]

**Output Format:** [Markdown with inline shell commands, JSON request examples, task results, and billing facts when returned]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include approved production cards, chapter ledgers, Beatra task IDs, audio URLs, artifact IDs, usage, and billing fields returned by the service.]

## Skill Version(s):

0.2.0 (source: server evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
