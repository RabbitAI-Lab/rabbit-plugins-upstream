## Description:

Outsources embroidery digitizing for BaconCo by reading Odoo digitize.demand records, sending ready embroidery jobs to an outside digitizer, updating Odoo state, and filing returned stitch packages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Operations employees and agents use this skill to run the embroidery digitizing outsourcing loop for BaconCo. It sends ready Odoo digitize.demand records to the digitizing vendor, receives completed stitch files, and records worksheet details back in Odoo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change Odoo digitizing records and submit jobs to a vendor account.

Mitigation: Install it only in environments where those actions are authorized, and restrict the Odoo MCP token to the required digitizing tools when possible.

Risk: Returned customer and job files may remain on local persistent agent storage.

Mitigation: Define retention, access review, and deletion procedures for the local job archive before use.

Risk: A confirmed vendor submission followed by a failed Odoo state update can create a sent-but-unmarked job.

Mitigation: Stop and report reconciliation needs after any post-submission Odoo update failure; do not resubmit automatically.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-digitize-outsourcing)
- [Odoo](https://www.odoo.com)
- [Routine details](references/routine.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Files]

**Output Format:** [Markdown status summaries, JSON tool payloads, and archived vendor files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can update Odoo digitizing records, submit vendor jobs, upload returned DST and PDF files, and maintain a local persistent job archive.]

## Skill Version(s):

0.5.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
