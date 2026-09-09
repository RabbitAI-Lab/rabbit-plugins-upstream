## Description:

Turns Douyin comment objections into short talking demo clips, one authorized still and one objection reply per clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and their agents use this skill to plan and generate short clips that answer public Douyin comment objections from authorized stills, confirmed product facts, and approved voice assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a persistent Beatra credential with broad Beatra tool and spending scopes.

Mitigation: Authorize only on an account where those scopes are acceptable, review before sensitive deployments, and use the documented uninstall and disconnect workflow when access should be removed.

Risk: The bundled client sends package and platform registration metadata during setup.

Mitigation: Review the installation and registration references before authorizing the package in environments with metadata handling restrictions.

Risk: Silent code updates are enabled by default.

Mitigation: Disable automatic updates with the documented update command before use when change-control review is required.

Risk: Lookup, clone, speech, and video steps can consume paid Beatra credits.

Mitigation: Use the documented per-stage confirmation cards, live price checks, unique client request IDs, and billing reports before and after paid work.

## Reference(s):

- [Douyin comment-to-demo workflow](references/workflow.md)
- [Douyin comment lookup](references/comment-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/douyin-comment-to-demo-clip)
- [Beatra skill homepage](https://beatra.ai/skills/douyin-comment-to-demo-clip)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON request examples, task reports, and generated media artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces separate 2 to 15 second clips; does not stitch clips.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
