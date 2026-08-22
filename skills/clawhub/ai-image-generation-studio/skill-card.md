## Description:

Create and refine images from a written brief, one to four ordered reference images, or an existing base image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan, submit, recover, and review Beatra image-generation, reference-composition, and image-editing tasks for product photos, advertising, brand visuals, posters, social graphics, illustrations, concept art, and background changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra Device Token with permissions beyond image generation.

Mitigation: Install only after reviewing Beatra account authorization and billing controls; keep the credential private, use the bundled authorization flow, and revoke access from the Beatra Console or the uninstall workflow when no longer needed.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Use the documented `python3 scripts/mcp_client.py update --auto off` command to disable automatic updates for the installation, or use `--check` to inspect availability without replacing files.

Risk: Paid image tasks can incur Beatra credit charges and live estimates are provisional.

Mitigation: Require approval before each paid request, freeze the payload with one stable `client_request_id`, avoid duplicate submissions during recovery, and report terminal `billing.net_charged_credits` from the completed task.

Risk: Generated images may drift from source identity, product details, logos, text, layout, or other must-keep requirements.

Mitigation: Inspect every accessible output against the brief and delivered media facts, disclose what could not be inspected, and use the smallest approved follow-up edit, composition, or generation when correction is needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/ai-image-generation-studio)
- [Beatra Skill Homepage](https://beatra.ai/skills/ai-image-generation-studio)
- [Intent and routing](references/intent-and-routing.md)
- [Visual direction and source preparation](references/visual-direction.md)
- [Image payloads and admission](references/image-recipes.md)
- [Review and iteration](references/review-and-iteration.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON payloads]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples; completed tasks return image URLs, artifact IDs, dimensions, usage, and billing facts when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Beatra MCP operations for paid image work after approval, with task polling and terminal billing reporting.]

## Skill Version(s):

0.1.3 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
