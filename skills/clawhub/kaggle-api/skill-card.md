## Description:

Kaggle API integration with managed authentication for accessing datasets, models, competitions, and kernels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search, download, and interact with Kaggle resources through a Maton-managed connection while keeping authentication scoped to the user's account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Kaggle through the user's connected account.

Mitigation: Use OAuth where possible, select least-privilege scopes, specify the intended connection when more than one exists, and delete unused connections.

Risk: Write operations or new connections can change account state or grant access.

Mitigation: Require explicit user approval before creating a connection or running POST, PUT, PATCH, or DELETE calls.

Risk: Optional functions and triggers can create persistent automation or event forwarding.

Mitigation: Keep trigger destinations scoped to trusted hosts, deploy functions with restrictive network policy unless explicitly justified, and remove unused automations.

## Reference(s):

- [Kaggle API Documentation](https://www.kaggle.com/docs/api)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Kaggle Models](https://www.kaggle.com/models)
- [Kaggle Competitions](https://www.kaggle.com/competitions)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/maton/skills/kaggle-api)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, text]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide authenticated Kaggle API calls, connection management, and optional Maton function or trigger setup.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
