## Description:

Create a WeChat Official Account visual pack from a finished article, outline, brand assets, photos, or visual references. Produce a lead cover plus coordinated in-article illustrations with clear section focus and consistent visual direction for WeChat articles, WeChat post images, brand stories, product explainers, event recaps, and knowledge content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to plan and generate a coordinated lead cover plus supporting illustrations for WeChat Official Account articles. It supports article-driven generation, brand-asset composition, and focused refinements through Beatra image tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a persistent shared Beatra device authorization with broad media, wallet, and task permissions.

Mitigation: Install only when this authorization is acceptable, keep the token out of chat, logs, command arguments, and diffs, and use the bundled uninstall/disconnect workflow when removing the package.

Risk: The bundled client silently checks for and installs verified package updates by default.

Mitigation: Review the automatic update setting before use and run `python3 scripts/mcp_client.py update --auto off` if explicit control over code changes is required.

Risk: Image generation creates paid Beatra tasks and can consume credits.

Mitigation: Require a single clear paid-call confirmation, reuse the same `client_request_id` only for unchanged recovery, poll the returned `task_id`, and report `billing.net_charged_credits` from the task result.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/wechat-article-visual-pack)
- [Beatra Skill Homepage](https://beatra.ai/skills/wechat-article-visual-pack)
- [Workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated image artifact links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents through Beatra MCP image generation, ordered asset uploads, task polling, billing reporting, and at most one focused unexecuted refinement suggestion.]

## Skill Version(s):

0.1.1 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
