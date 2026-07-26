## Description: <br>
Helps local staffing agency owners or operators prepare a TempGuru partner inquiry, frame W-2 event staffing coverage, use optional TempGuru MCP lookups, and route the inquiry by email or phone. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kissmyabs32](https://clawhub.ai/user/kissmyabs32) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External staffing agency owners and operators use this skill to understand TempGuru's partner model, compare their markets and event roles against TempGuru coverage, benchmark client bill-rate ranges, and draft a partner inquiry for review before sending. <br>

### Deployment Geography for Use: <br>
United States and Canada <br>

## Known Risks and Mitigations: <br>
Risk: A partner inquiry email could be sent with incorrect recipient, subject, market, role, W-2, or capacity details. <br>
Mitigation: Require user review and confirmation before sending; offer the email draft or phone channel for manual follow-up. <br>
Risk: A staffing agency partner inquiry could be misrouted through the buyer quote workflow. <br>
Mitigation: Use only the disclosed partner email or phone channel for agency inquiries, and do not submit partner requests through request_quote. <br>
Risk: The agent could overstate vetting criteria, partner economics, acceptance, order volume, exclusivity, or timelines. <br>
Mitigation: Limit guidance to the documented W-2 baseline and structural partner model; leave vetting details and economics to a TempGuru coordinator. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kissmyabs32/skills/tempguru-staffing-agency-partner-growth) <br>
- [TempGuru MCP endpoint](https://mcp.tempguru.co/mcp) <br>
- [TempGuru AI developer docs](https://tempguru.co/ai) <br>
- [TempGuru machine-readable overview](https://tempguru.co/llms.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, API calls] <br>
**Output Format:** [Markdown or plain text guidance with a user-reviewed email draft] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include read-only TempGuru MCP lookup results; the partner inquiry email should be reviewed by the user before sending.] <br>

## Skill Version(s): <br>
1.5.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
