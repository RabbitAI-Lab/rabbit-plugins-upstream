## Description:

Helps agents access and analyze CallRail calls and manage tracking numbers, companies, and tags through an authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and developers use this skill to review CallRail call activity and analytics, organize calls with tags, and manage authorized tracking resources. Optional automations require separate review and approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: New connections, changes to CallRail data, or persistent automation may affect the wrong account or continue beyond a one-off request.

Mitigation: Confirm the target account and obtain explicit approval for each connection, write, function, trigger, or destination.

Risk: Exposed API keys or broad access can disclose connected business data.

Mitigation: Prefer OAuth login, select only needed access, and never print, store, or share API keys.

Risk: Local event handlers may execute code on untrusted event data.

Mitigation: Avoid local execution unless the user has reviewed the script and separately approved running it.

## Reference(s):

- [Maton homepage](https://maton.ai)
- [CallRail API documentation](https://apidocs.callrail.com/)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account, network access, and an authorized CallRail connection.]

## Skill Version(s):

1.2.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
