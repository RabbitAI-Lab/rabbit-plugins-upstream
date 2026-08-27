## Description:

Turn user-supplied public policy digest points into one policy digest still per page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content teams use this skill to plan and generate one policy digest still per supplied public-points page, while avoiding invented policy details or forged official notices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied digest prompts and optional reference files are sent to Beatra for generation.

Mitigation: Use only public, approved digest points and avoid submitting sensitive or private content.

Risk: The skill can spend paid Beatra credits for image generation.

Mitigation: Show the live model price and obtain user approval before each billable page request.

Risk: The skill stores a broad shared Beatra Device Token locally.

Mitigation: Protect the local credential file, never expose the token in chat or logs, and disconnect when access is no longer needed.

Risk: Silent package-owned automatic updates are enabled by default.

Mitigation: Disable auto-update before use in controlled environments and review updates before re-enabling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/policy-digest-set)
- [Beatra skill homepage](https://beatra.ai/skills/policy-digest-set)
- [Policy-digest workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces page plans, Beatra generation commands, task polling guidance, and delivery notes for generated still artifacts.]

## Skill Version(s):

0.1.1 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
