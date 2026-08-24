## Description:

Turn one product photo into a vertical product video with spoken narration for product launches, listings, storefront promos, and shoppable social posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, creators, and commerce teams use this skill to turn a product photo and merchant-supplied claims into a short vertical video with narration. The agent guides inspection, script preparation, Beatra media generation, billing confirmation, task polling, and delivery review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a shared Beatra Device Token under ~/.beatra.

Mitigation: Review before installing in managed or sensitive environments, keep the token out of chat and logs, and use the uninstall or disconnect guidance when access should be removed.

Risk: The workflow uploads selected product media to Beatra.

Mitigation: Use only product media the user is authorized to process and avoid exposing private prompts, credentials, or sensitive input content during recovery.

Risk: Paid Beatra credit usage can occur after confirmation.

Mitigation: Follow the two approval gates, show the live estimate and request identity before paid calls, and retry uncertain paid work only with the same frozen request identity.

Risk: The bundled client silently self-updates by default.

Mitigation: Disable automatic updates with python3 scripts/mcp_client.py update --auto off when runtime code replacement is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/product-video-studio)
- [Beatra skill homepage](https://beatra.ai/skills/product-video-studio)
- [The first frame](references/first-frame.md)
- [Writing the narration](references/copy-craft.md)
- [Commerce video workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Files, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON tool arguments; final delivery can include generated video artifact details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses explicit user confirmations before paid media generation and reports returned task, billing, duration, and media facts.]

## Skill Version(s):

0.1.2 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
