## Description:

Outsources embroidery digitizing for BaconCo by reading ready Odoo digitize demands, gathering artwork and specifications, coordinating external digitizer submission, and marking demands outsourced only after confirmed submission.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Operations agents and developers use this skill to automate the ERP side of embroidery digitizing outsourcing: find sendable Odoo demands, download required artwork files, prepare the digitizer brief, coordinate submission, and update Odoo after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Odoo MCP token may allow production or broad ERP actions.

Mitigation: Use a scoped MCP endpoint limited to the intended digitizing tools, prefer staging during validation, and require operator review before state changes unless the automation is explicitly approved.

Risk: Customer artwork can be downloaded locally and submitted to an outside digitizer.

Mitigation: Treat artwork as sensitive customer data, submit only under the organization's vendor approval policy, and clean up downloaded files after use.

Risk: A confirmed vendor submission followed by a failed Odoo update can create duplicate-submission risk on retry.

Mitigation: Update each demand immediately after a confirmed submission; if the Odoo update fails, stop and reconcile manually rather than resubmitting.

## Reference(s):

- [Routine details](artifact/references/routine.md)
- [Odoo](https://www.odoo.com)
- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-digitize-outsourcing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON snippets, and concise status reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ODOO_MCP_URL and ODOO_MCP_TOKEN; coordinates with a separate digitizer submission skill.]

## Skill Version(s):

0.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
