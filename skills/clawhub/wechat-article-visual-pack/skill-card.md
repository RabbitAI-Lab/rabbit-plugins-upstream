## Description:

Create a WeChat Official Account visual pack from a finished article, outline, brand assets, photos, or visual references. Produce a lead cover plus coordinated in-article illustrations with clear section focus and consistent visual direction for WeChat articles, WeChat post images, brand stories, product explainers, event recaps, and knowledge content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and brand teams use this skill to turn a WeChat Official Account article, outline, or brand imagery into a coordinated lead cover and supporting in-article illustration set. The skill guides route selection, paid image generation or transformation, task recovery, and final delivery of ordered image artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Beatra authorization includes paid spending ability and media scopes beyond image generation.

Mitigation: Install only after reviewing the requested authorization, confirm each paid generation request before submission, and revoke the connected device from the Beatra Console when access is no longer trusted.

Risk: The skill uses a shared local Beatra credential under `~/.beatra`.

Mitigation: Keep the credential file private, avoid exposing tokens in prompts, logs, command arguments, or diffs, and use the bundled uninstall flow or Beatra Console revocation to disconnect.

Risk: The bundled client silently checks for and applies package updates by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when deterministic review is required, and use `python3 scripts/mcp_client.py update --check` to inspect available updates.

Risk: Generation requests consume Beatra credits and can be duplicated if retried with changed inputs after an uncertain response.

Mitigation: Use one opaque `client_request_id`, retry only identical requests with the same ID after transport uncertainty, and report `billing.net_charged_credits` from the returned task data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/wechat-article-visual-pack)
- [Beatra skill homepage](https://beatra.ai/skills/wechat-article-visual-pack)
- [Workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown guidance with inline JSON payloads, shell commands, and returned image task artifact links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces ordered Beatra image-task results for a two-to-four-image WeChat article visual sequence when the user approves paid generation or transformation.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
