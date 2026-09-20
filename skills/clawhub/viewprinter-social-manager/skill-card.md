## Description:

ViewPrinter Social Manager helps an agent manage connected ViewPrinter social accounts for scheduling and publishing posts, handling media, managing account groups, and reading performance results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1vmgm](https://clawhub.ai/user/1vmgm)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill through a connected ViewPrinter account to publish or schedule social posts, upload and manage media, manage destination groups, and review account or post performance. It is intended only for ViewPrinter-supported workflows where the user has connected accounts and approved the posting action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish or schedule posts to real connected social accounts.

Mitigation: Review the post content, destination accounts or groups, and exact scheduled time before allowing a publish or schedule action.

Risk: The skill can permanently delete stored ViewPrinter media.

Mitigation: Confirm the intended media item before deletion and treat media deletion as irreversible.

Risk: Listing media or posts can read broad workspace data.

Mitigation: Use the skill only when the user intends to work inside connected ViewPrinter workspaces and report returned data without expanding the scope.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/1vmgm/skills/viewprinter-social-manager)
- [ViewPrinter MCP endpoint](https://viewprinter.tech/api/mcp)
- [Platforms first rule](artifact/references/rules/platforms-first.md)
- [Scheduling rule](artifact/references/rules/scheduling.md)
- [Media upload rule](artifact/references/rules/media-upload.md)
- [Destinations rule](artifact/references/rules/destinations.md)
- [Amend and cancel rule](artifact/references/rules/amend-and-cancel.md)
- [Connecting rule](artifact/references/rules/connecting.md)
- [Reading results rule](artifact/references/rules/reading-results.md)
- [Drafts rule](artifact/references/rules/drafts.md)
- [Refusals rule](artifact/references/rules/refusals.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, API calls]

**Output Format:** [Plain text or Markdown responses with ViewPrinter MCP tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May schedule or publish to real connected social accounts, read workspace media and post data, and delete stored media when the user requests it.]

## Skill Version(s):

1.1.2 (source: server release metadata; artifact frontmatter says 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
