## Description:

Connects Amazon product features to user benefits supported by review evidence and produces listing-expression guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT

## Use Case:

External Amazon sellers and operations teams use this skill to turn product features into benefit statements grounded in collected review evidence. It is intended for listing-benefit analysis, not advertising bidding, unsupported claims, or automatic Amazon page publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits when the user confirms paid work or account auto-confirm rules allow execution.

Mitigation: Verify the Amazon site and ASIN before paid work, use quote-only flows when the user asks only for pricing, and set auto-confirm to always ask when automatic spending is not desired.

Risk: The skill can change account approval settings for future paid operations when the user requests auto-confirm changes.

Mitigation: Confirm the requested threshold, off, or default setting before changing it, then restate the active rule.

Risk: Its broader ARI workflows may exceed the narrow listing-benefit task if invoked casually.

Mitigation: Keep normal use to the fixed listing/benefits workflow unless the user explicitly asks for another supported workflow and understands any cost implications.

Risk: Exports can write local files and may target sensitive or existing paths.

Mitigation: Use safe export paths and avoid writing reports or CSV files over configuration files or other important local files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/feature-benefit)
- [README](README.md)
- [Dedicated operation workflow](references/operation-workflow.md)
- [ARI CLI and API reference](references/reference.md)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with optional shell commands and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are grounded in ARI-collected Amazon review samples and should state data range, sample limitations, credits used, and report links when available.]

## Skill Version(s):

1.4.8 (source: frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
