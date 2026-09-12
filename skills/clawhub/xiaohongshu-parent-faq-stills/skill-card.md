## Description:

Turn Xiaohongshu parent FAQ notes into a 4 to 8 still answer set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External educators and school staff use this skill to turn supplied or publicly looked-up Xiaohongshu parent questions into 4 to 8 answer stills grounded in confirmed teaching facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can connect to a Beatra account and use a broad shared bearer credential.

Mitigation: Review whether the Beatra authorization is acceptable for the deployment environment and keep the credential in the documented local credential file only.

Risk: Approved lookup, generation, transform, or edit work can spend Beatra credits.

Mitigation: Use the skill's required approval cards, live price checks, unique client request IDs, and task polling before and after each paid stage.

Risk: Automatic package updates are enabled by default and can replace package-owned files.

Mitigation: Use the documented auto-update disable command when unattended code replacement is not allowed.

Risk: Generated answer stills could include incorrect, invented, or unreadable text.

Mitigation: Review each still against the picked parent question and confirmed answer line, and treat small generated text as a review item rather than certified content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/xiaohongshu-parent-faq-stills)
- [Beatra skill homepage](https://beatra.ai/skills/xiaohongshu-parent-faq-stills)
- [Parent FAQ still workflow](references/workflow.md)
- [Xiaohongshu parent FAQ lookup](references/parent-faq-lookup.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [MCP connection](references/mcp-connection.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with approval cards, command examples, task status, billing details, and delivered image artifact metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free slot plan before paid lookup or image generation; generated stills are delivered as image artifacts with MIME type, dimensions, byte size, and charged credits when available.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
