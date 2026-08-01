## Description: <br>
This skill helps an agent use a Zola MCP server to read and manage wedding planning data, including vendors, budgets, guests, RSVPs, seating, registry, gifts, and marketplace discovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users can use this skill when they want an agent to help inspect or manage Zola wedding planning data, including guest lists, RSVPs, vendor details, budgets, seating, registry items, and gifts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive wedding planning information such as guest lists, addresses, RSVPs, vendor conversations, registry data, and gifts. <br>
Mitigation: Install only when this data access is intended, treat the data as sensitive, and limit use to trusted agent sessions. <br>
Risk: The skill exposes write-capable actions for guest, vendor, budget, seating, event, invitation, and inquiry workflows. <br>
Mitigation: Require explicit user confirmation before add, update, remove, invite, seat-assignment, booking, or bulk-change actions. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Text, Guidance] <br>
**Output Format:** [MCP tool calls with text summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can read and modify Zola planning data through the exposed MCP tools.] <br>

## Skill Version(s): <br>
1.6.6 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
