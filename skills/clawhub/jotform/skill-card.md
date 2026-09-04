## Description:

JotForm API integration with managed OAuth for creating forms, managing submissions, and accessing form data through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to help users work with JotForm accounts through Maton, including reading form metadata, retrieving submissions, creating forms, and managing webhooks. It is intended for JotForm workflows where OAuth-backed API access and explicit confirmation for write actions are required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton acts as the OAuth/API gateway for the connected JotForm account.

Mitigation: Install only if Maton is trusted for this account, review requested scopes before connecting, and prefer OAuth over long-lived API keys.

Risk: Write, delete, webhook, or account-changing operations can modify JotForm resources.

Mitigation: Require explicit user confirmation before any modifying operation and verify the target account, resource, and payload first.

## Reference(s):

- [JotForm Skill Page](https://clawhub.ai/byungkyu/skills/jotform)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [JotForm API Overview](https://api.jotform.com/docs/)
- [JotForm User Forms](https://api.jotform.com/docs/#user-forms)
- [JotForm Form Submissions](https://api.jotform.com/docs/#form-id-submissions)
- [JotForm Webhooks](https://api.jotform.com/docs/#form-id-webhooks)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and API path guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended to guide Maton CLI or SDK use for JotForm API access.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
