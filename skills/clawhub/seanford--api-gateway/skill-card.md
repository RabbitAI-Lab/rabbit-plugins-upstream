## Description:

Connect to 100+ APIs including Google Workspace, Microsoft 365, GitHub, Notion, Slack, Airtable, and HubSpot through Maton-managed OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanford](https://clawhub.ai/user/seanford)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to call native third-party API endpoints through Maton-managed OAuth connections and manage those connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad live-service action capability, including deletion, posting, file, admin, and business-data operations.

Mitigation: Verify the selected connection and require explicit confirmation before deletes, public posts, financial or admin changes, and bulk mutations.

Risk: Authorized third-party connections may expose more access than a task requires.

Mitigation: Use the narrowest OAuth scopes available and keep access limited to user-authorized connections.

Risk: Leaking MATON_API_KEY could let another party use the Maton gateway for the account.

Mitigation: Keep MATON_API_KEY in the environment or secret store and never print, log, or share it.

Risk: Pre-signed media upload URLs may point outside the gateway path.

Mitigation: Validate the upload destination before sending local files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seanford/skills/api-gateway)
- [Maton homepage](https://maton.ai)
- [Maton API Reference](https://www.maton.ai/docs/api-reference)
- [Skill source](SKILL.md)
- [License](LICENSE.txt)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Python and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API requests and JSON responses when executed by an agent with a valid MATON_API_KEY and user-authorized connections.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
