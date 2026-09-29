## Description:

Helps agents manage connected ViewPrinter social accounts, including posts, media, account groups, and performance reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1vmgm](https://clawhub.ai/user/1vmgm)

### License/Terms of Use:

MIT-0

## Use Case:

People managing connected ViewPrinter accounts use this skill to prepare and publish social posts, manage media and account groups, and review account and post performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing to public accounts cannot be recalled, and deleting hosted media permanently removes its bytes.

Mitigation: Confirm the content, destinations, timing, and deletion target with the user before taking these actions.

Risk: Listing posts or media can expose information across the user's ViewPrinter workspaces.

Mitigation: Use the skill only for connected ViewPrinter work the user requests and disclose only relevant results.

Risk: An ambiguous retry could publish the same post twice.

Mitigation: Check whether the post already exists and reuse its idempotency key when retrying.

## Reference(s):

- [ViewPrinter Social Manager on ClawHub](https://clawhub.ai/1vmgm/skills/viewprinter-social-manager)
- [Platform capabilities](references/rules/platforms-first.md)
- [Scheduling and approvals](references/rules/scheduling.md)
- [Media upload and deletion](references/rules/media-upload.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, API calls]

**Output Format:** [Text responses and structured ViewPrinter tool requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports publication outcomes and metrics by destination.]

## Skill Version(s):

1.3.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
