## Description:

Guides an agent through using curl to access the Crown Town Compost customer portal for pickup history, invoices, upcoming service days, skips, account details, and related portal pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Crown Town Compost customer portal data from a shell, including service history, billing history, environmental impact, service calendar state, and account pages. It also documents write-capable POST flows, which should be reviewed and confirmed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an authenticated portal session in a local cookie jar that gives shell-level access to the user's Crown Town Compost account.

Mitigation: Treat the cookie jar like a password, keep it in a restricted location, remove it when finished, and avoid sharing logs or terminal output that may expose session material.

Risk: The documented POST flows can change account state, including skipped service days, account details, support messages, missed-pickup reports, and cancellation-related requests.

Mitigation: Require explicit user confirmation before any write-capable POST and re-read the relevant portal page afterward to verify the intended change.

Risk: Billing endpoints can expose invoice, receipt, and hosted payment links.

Mitigation: Use the shell flow for inspection only and open payment actions in a browser rather than scripting payment or card-entry workflows.

## Reference(s):

- [Crown Town Compost endpoint reference](references/endpoints.md)
- [Crown Town Compost customer portal](https://portal.crowntowncompost.com)
- [ClawHub skill release page](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON endpoint examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided Crown Town Compost credentials and confirmation before write-capable portal POSTs.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
