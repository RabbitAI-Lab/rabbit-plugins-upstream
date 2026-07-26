## Description: <br>
Automates lead capture and tracking with Supabase storage and Make.com email workflows, managing lead conversations from new to qualified status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[big-roman123](https://clawhub.ai/user/big-roman123) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Sales and customer-facing teams use this skill through an agent to capture interested contacts, store lead details, trigger first-response email automation, and track qualification status. Developers configuring the skill connect it to a protected Supabase project and Make.com workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Personal lead details and conversation history are stored in an external Supabase database. <br>
Mitigation: Notify users before storing or emailing their details, define retention rules, and enable appropriate Supabase access controls and audit logging. <br>
Risk: The required Supabase service role key can grant broad database access. <br>
Mitigation: Store the key only as a protected secret, keep it out of agent-visible and client-side contexts, and dedicate the Supabase environment to this workflow. <br>
Risk: Automated email workflows may send messages based on captured lead data. <br>
Mitigation: Review Make.com and Resend data handling, use approved templates, and gate auto-replies on consent or approved lead-capture triggers. <br>
Risk: Lead deletion is implemented as a hard delete. <br>
Mitigation: Require confirmation for destructive actions or add soft-delete, backup, and recovery controls before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/big-roman123/skills/sales-bot) <br>
- [Publisher profile](https://clawhub.ai/user/big-roman123) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Configuration, Guidance] <br>
**Output Format:** [Structured JSON objects for lead records, conversation history, status updates, automation checks, and analytics.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Supabase credentials and organization configuration; writes and reads external lead and conversation state.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, skill.json, package.json, SKILL.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
