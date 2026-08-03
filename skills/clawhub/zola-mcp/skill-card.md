## Description: <br>
Provides MCP tools for Zola wedding planning data, including vendors, budgets, guests, seating, RSVPs, events, registry items, gifts, and marketplace discovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to read and manage wedding-planning information in Zola accounts, including vendors, budgets, guests, seating, RSVPs, events, registry items, gifts, and marketplace discovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tools can change real Zola account data, including guests, vendors, budgets, seating, RSVPs, invitations, and registry-related records. <br>
Mitigation: Require explicit user confirmation before invoking write or destructive actions, and review proposed changes before submission. <br>
Risk: The security review found unclear safety boundaries around account-changing actions. <br>
Mitigation: Review the skill carefully before installation and restrict use to intended Zola wedding-planning tasks. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, API calls, guidance] <br>
**Output Format:** [Markdown or plain text responses with MCP tool-call results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May access or modify real Zola wedding-planning data; confirmation is recommended before account-changing actions.] <br>

## Skill Version(s): <br>
1.7.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
