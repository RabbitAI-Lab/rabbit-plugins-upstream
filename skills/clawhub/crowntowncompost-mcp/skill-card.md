## Description:

Accesses the Crown Town Compost customer portal from shell-based workflows to retrieve service, billing, account, and scheduling information and prepare portal requests with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators with Crown Town Compost portal accounts use this skill to script authenticated portal access for pickup history, invoices, upcoming service days, account details, and carefully reviewed account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable real account changes and persistent login cookies.

Mitigation: Require explicit approval before service skips, profile changes, support messages, cancellation steps, or other write actions; re-read portal state after any accepted write.

Risk: Cookie jars and exported billing CSVs may expose account or billing data.

Mitigation: Store cookie jars with restrictive permissions or in temporary files, delete them after use, and treat exported billing CSVs as sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)
- [Crown Town Compost portal](https://portal.crowntowncompost.com)
- [Endpoint reference](artifact/references/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl commands and parsing guidance for authenticated portal requests.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
