## Description:

Helps exchange and check Meta user tokens, store the renewed token in gateway configuration, and remind the owner before expiry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thinhbuiii](https://clawhub.ai/user/thinhbuiii)

### License/Terms of Use:

MIT-0

## Use Case:

Gateway owners and operators use this skill to check and renew Meta user tokens, update gateway configuration, and monitor token expiry without changing ads data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Token exchange and configuration changes handle powerful credentials that could be exposed or misused.

Mitigation: Require explicit owner confirmation before reading configuration or exchanging or saving tokens; use only the minimum required Meta scopes and never print credentials in chat or logs.

Risk: Editing gateway configuration, restarting the service, or scheduling checks can disrupt an existing deployment.

Mitigation: Confirm each change with the owner, back up the configuration, preserve existing settings, and verify token status after restart.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thinhbuiii/skills/meta-long-lived-token)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and token status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports validity and expiry without disclosing token values.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
