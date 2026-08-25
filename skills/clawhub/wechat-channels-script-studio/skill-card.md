## Description:

Turns product facts into a WeChat Channels short-video sales script with a second-by-second segment table, full narration, product-link conversion beats, and a six-dimension draft score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, merchants, and marketing teams use this skill to turn verified product or service facts into WeChat Channels selling scripts, including segment timing, spoken narration, link-placement beats, and a draft quality check. It can optionally guide storyboard frame and narration audio generation after user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a shared Beatra credential and can submit paid remote media-generation requests.

Mitigation: Install only if you trust Beatra, review the authorization grant, require user approval before paid generation, and report only returned billing facts such as `billing.net_charged_credits`.

Risk: The bundled client can silently check for updates and replace package-owned files.

Mitigation: Review the update behavior before deployment and consider disabling silent updates with `python3 scripts/mcp_client.py update --auto off`.

Risk: Generated sales scripts can become misleading if missing product claims are filled in without evidence.

Mitigation: Use only user-supplied commercial facts, name gaps plainly, and write around missing prices, results, certifications, offer terms, or reference-video performance claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/wechat-channels-script-studio)
- [Beatra skill homepage](https://beatra.ai/skills/wechat-channels-script-studio)
- [Structuring the script](references/script-structure.md)
- [Placing the product-link beats](references/product-link-beats.md)
- [Script studio workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with script tables, narration text, review notes, and inline shell commands when setup or recovery is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include returned task IDs, artifact links, dimensions, duration, resolved model, and net charged credits when optional media is produced.]

## Skill Version(s):

0.1.2 (source: server evidence release.version and artifact manifest version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
