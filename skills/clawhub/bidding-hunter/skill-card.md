## Description:

Automated government procurement bid discovery engine that scans multiple Chinese procurement platforms, matches configurable keywords, tracks bid statuses, and delivers deadline-aware reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huagavin](https://clawhub.ai/user/huagavin)

### License/Terms of Use:

MIT

## Use Case:

External users, bidding teams, and agents use this skill to monitor Chinese government procurement platforms for user-configured keywords, organize matching opportunities, track deadlines, and produce reports or reminders.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill performs networked browser automation against procurement websites.

Mitigation: Run scans only against trusted public procurement platforms and review configured platform URLs before scheduled use.

Risk: Custom JavaScript adapters can be executed when placed under the configured adapter paths.

Mitigation: Review custom adapter source before adding it to ~/.bidding-hunter/platforms or config custom_paths.

Risk: Webhook notifications can disclose bid intelligence outside the local machine.

Mitigation: Use only approved webhook destinations and verify notification configuration before enabling automated reports.

Risk: The security verdict requires review because local-only privacy claims do not fully cover configured webhook delivery.

Mitigation: Treat webhook use as data sharing and document the intended notification recipients for deployment review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huagavin/skills/bidding-hunter)
- [Server-resolved GitHub source](https://github.com/HuaGavin/bidding-hunter)
- [README](artifact/README.md)
- [Architecture and design guide](artifact/DESIGN.md)
- [Configuration schema](artifact/config/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or CLI text, with optional JSON and CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on user-provided keywords, enabled procurement platforms, local scan state, and configured notification channels.]

## Skill Version(s):

1.0.1 (source: frontmatter, package.json, CHANGELOG, released 2026-07-22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
