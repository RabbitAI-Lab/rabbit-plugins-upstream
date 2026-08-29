## Description:

This skill helps agents access and manage Zola wedding-planning data, including vendors, budgets, guests, seating, RSVPs, registry items, and gifts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to review and update Zola wedding-planning records across vendors, budget, guest lists, seating, events, RSVPs, registry, and gifts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change wedding-planning records, including vendors, guests, seating, events, invitations, budgets, registry, and gifts.

Mitigation: Require explicit user confirmation before delete, bulk invite, budget, vendor, guest, seating, event, registry, or gift-tracking changes.

Risk: Broad activation language may enable the skill for many wedding-planning requests.

Mitigation: Enable it only for intentional Zola workflows and confirm the target account, event, guest, vendor, or registry item before acting.

Risk: Wedding-planning records can include sensitive personal and financial details.

Mitigation: Limit use to users who are comfortable granting the agent access to Zola data and avoid sharing retrieved details outside the intended workflow.

## Reference(s):

- [ClawHub zola skill page](https://clawhub.ai/chrischall/skills/zola)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown summaries of Zola planning records and requested changes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.8.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
