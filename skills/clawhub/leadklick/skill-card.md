## Description: <br>
Automate lead capture in Supabase with Make.com email workflows, manage lead status and conversations, and track auto-reply delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[big-roman123](https://clawhub.ai/user/big-roman123) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and sales operations teams use this skill to let agents capture leads, store contact and conversation records, update lifecycle status, and check automated email reply status through a Supabase-backed workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a broad Supabase service-role key. <br>
Mitigation: Use a dedicated or tightly controlled Supabase project, keep the key server-side, and rotate it if exposed. <br>
Risk: The skill stores contact details and conversation content and can trigger automated email outreach. <br>
Mitigation: Confirm consent and applicable outreach requirements before storing contact records or sending automated replies through Make.com or Resend. <br>
Risk: Lead deletion can remove records from the backing database. <br>
Mitigation: Review or disable the deleteLead capability unless deletion is explicitly required and access is restricted. <br>
Risk: Multi-organization isolation depends on correct org IDs and database policy assumptions. <br>
Mitigation: Verify organization isolation and Row Level Security behavior before using shared or production data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/big-roman123/skills/leadklick) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Configuration] <br>
**Output Format:** [Structured JSON-like action results with TypeScript usage examples and configuration fields.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Supabase project URL, service-role key, organization UUID, and optional default lead priority.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, package.json, skill.json, SKILL.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
