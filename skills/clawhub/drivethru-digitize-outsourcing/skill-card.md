## Description:

Outsource embroidery digitizing end to end for BaconCo by finding Ready Odoo digitize demands, retrieving artwork and specs, submitting confirmed jobs to the outside digitizer, and marking each demand Outsource only after confirmed submission.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Operations employees and agent operators use this skill to run the embroidery digitizing outsourcing routine for BaconCo's Odoo workflow. It helps move sendable Ready digitize demands through artwork retrieval, digitizer submission, and ERP state update while holding rush jobs for human approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can call Odoo MCP tools with a bearer token and may update ERP records.

Mitigation: Install only with a staging or narrowly scoped Odoo MCP token and verify the MCP endpoint exposes only the required digitizing tools.

Risk: Non-rush jobs can be submitted and marked outsourced without a per-job approval gate.

Mitigation: Require human review before confirmed submissions or ERP state changes until the workflow is trusted.

Risk: A confirmed portal submission followed by a failed Odoo outsource update can leave a sent job still visible as Ready.

Mitigation: Stop and report immediately after any post-submit outsource update failure, and do not resubmit until a human reconciles the demand.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-digitize-outsourcing)
- [Odoo](https://www.odoo.com)
- [Routine details](artifact/references/routine.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON command arguments and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local decoded artwork files during execution and reports outsourced, held, blocked, or failed demands.]

## Skill Version(s):

0.1.1 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
