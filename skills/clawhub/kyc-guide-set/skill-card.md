## Description:

Turn user-supplied account-opening material checklist lines into a four-to-eight still KYC guide set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn an approved KYC or account-opening materials checklist into a consistent still-image guide pack, with one still per named material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra account powers, including media generation, wallet spending, task access, artifact access, and cancellation.

Mitigation: Install only when those powers are acceptable for the account and environment; use the bundled authorization flow and keep the device credential local and private.

Risk: KYC-related prompts or selected files may be sent to Beatra during generation or upload workflows.

Mitigation: Send only the approved checklist lines and assets needed for the stills, and avoid including sensitive personal data that is not required for the output.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Disable automatic updates for the installation with `python3 scripts/mcp_client.py update --auto off` when review-before-update is required.

Risk: Generated stills may contain unreadable or incorrect small text and should not be treated as legal advice or an official KYC requirement.

Mitigation: Review visible text against the approved pack list, flag unreadable text, and keep missing facts out of the generated stills until the user supplies them.

Risk: Billable generation requests can consume credits, and careless retries after transport uncertainty can create duplicate work.

Mitigation: Use one opaque `client_request_id` per still, retry only identical frozen payloads with the same identity, and require new approval for changed work.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/kyc-guide-set)
- [KYC Materials Guide Pack Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown planning and approval text with JSON MCP payloads, shell commands, and generated still-image artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one still per named material, typically four to eight stills, with one billable generation request per still.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
