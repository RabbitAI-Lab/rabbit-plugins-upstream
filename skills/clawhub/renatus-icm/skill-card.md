## Description: <br>
Manage Renatus event campaigns by setting up landing pages, running email blasts, handling guest registrations, exporting leads, and syncing unsubscribes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[earlvanze](https://clawhub.ai/user/earlvanze) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Independent Campaign Managers and operators use this skill to run Renatus event marketing workflows, including event page generation, commercial email sends, lead export, guest registration, order-entry reference checks, and unsubscribe synchronization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reuses a live browser session through local CDP access for Renatus operations. <br>
Mitigation: Use a dedicated Chrome or Brave profile, keep CDP bound to local access only, and close the debugging session when work is complete. <br>
Risk: The skill handles bulk lead records and exported CSV/JSON/log files that can contain personal data. <br>
Mitigation: Treat exports and logs as sensitive data, restrict access to the workspace, and delete or archive files according to the operator's data-retention policy. <br>
Risk: Some workflows can perform destructive lead operations or external campaign actions. <br>
Mitigation: Run dry-run or read preflight steps first, require explicit approval before writes, and verify the exact target lead, registration, unsubscribe, or order state before execution. <br>
Risk: Supabase and Renatus credentials can expose campaign data or administrative operations if over-scoped. <br>
Mitigation: Use least-privilege Supabase tokens, avoid production service_role keys for routine work, rotate exposed credentials, and verify the unsubscribe backend before publishing pages. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/earlvanze/skills/renatus-icm) <br>
- [Renatus ICM Workflows](references/workflows.md) <br>
- [Email Campaign Guide](references/email-campaign.md) <br>
- [Event Page Setup Guide](references/event-page-setup.md) <br>
- [Supabase Setup for Renatus ICM](references/supabase-setup.md) <br>
- [Renatus Back Office Order Entry API](references/order-entry-backoffice-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, generated HTML/templates, CSV/JSON exports, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include campaign files, lead exports, logs, and browser/CDP-driven operational steps.] <br>

## Skill Version(s): <br>
2.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
