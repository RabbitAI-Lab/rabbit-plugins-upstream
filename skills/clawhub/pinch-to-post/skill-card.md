## Description: <br>
Manage WordPress sites through WP Pinch MCP tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickhamze](https://clawhub.ai/user/nickhamze) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to manage WordPress content, media, users, comments, settings, WooCommerce tasks, and governance checks through WP Pinch MCP tools. It is intended for WordPress sites the user is authorized to administer from an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help perform administrative WordPress actions, including content changes, role changes, settings updates, plugin/theme operations, and bulk edits. <br>
Mitigation: Install it only for sites the user intends to manage, use least-privileged WordPress credentials or the OpenClaw Agent role, and keep read-only mode or daily write budgets enabled where practical. <br>
Risk: Publishing, deleting, bulk editing, or plugin/theme changes can have broad site impact if requested too loosely. <br>
Mitigation: Draft first, confirm before publishing or bulk operations, orient with site health or digest tools before major changes, and review WP Pinch audit logs. <br>
Risk: Broad triggers may make the skill available in loosely related WordPress or blogging conversations. <br>
Mitigation: Limit installation to intended WordPress-management workspaces and require explicit user confirmation before write operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nickhamze/skills/pinch-to-post) <br>
- [WP Pinch homepage](https://wp-pinch.com) <br>
- [WP Pinch project](https://github.com/RegionallyFamous/wp-pinch) <br>
- [WP Pinch configuration guide](https://github.com/RegionallyFamous/wp-pinch/wiki/Configuration) <br>
- [WP Pinch security model](https://github.com/RegionallyFamous/wp-pinch/wiki/Security) <br>
- [WP Pinch error codes](https://github.com/RegionallyFamous/wp-pinch/wiki/Error-Codes) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Markdown, Configuration, API Calls] <br>
**Output Format:** [Markdown guidance with MCP tool-call instructions and configuration details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires WP_SITE_URL; WordPress credentials are configured in the MCP server, not in the skill.] <br>

## Skill Version(s): <br>
5.5.1 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
