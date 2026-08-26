## Description:

AI Headshot Studio helps an agent transform a casual selfie into a studio-quality professional headshot with appropriate styling, background, attire, and lighting while preserving the person's identity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to plan, confirm, execute, track, and review a Beatra image-generation workflow that turns selfies or accepted drafts into professional headshots for LinkedIn, resumes, company websites, business cards, or social media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra device authorization.

Mitigation: Install only if the user accepts that authorization scope, and reconnect with full Beatra authorization only after explicit user approval.

Risk: Selected face images are uploaded to Beatra for processing.

Mitigation: Confirm the exact paid generation request and ordered image references before execution, and avoid exposing authentication tokens, private prompts, or sensitive image details in recovery messages.

Risk: The local package silently checks for and installs updates by default.

Mitigation: Use the documented update controls to disable automatic checks with `python3 scripts/mcp_client.py update --auto off` when silent updates are not acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/ai-headshot-studio)
- [Beatra skill homepage](https://beatra.ai/skills/ai-headshot-studio)
- [Headshot routing](references/headshot-routing.md)
- [Portrait craft](references/portrait-craft.md)
- [Workflow](references/workflow.md)
- [Review and recovery](references/review-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides a single-image Beatra headshot workflow and returns task details, artifact links, observed dimensions, and billing fields when available.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
