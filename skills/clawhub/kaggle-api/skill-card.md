## Description:

Kaggle API integration with managed authentication for accessing Kaggle datasets, models, competitions, and kernels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search, list, download, and interact with Kaggle resources through Maton-managed authentication. It is suited for Kaggle dataset, model, competition, and notebook workflows where read/list calls should be preferred and account-changing actions require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kaggle access is brokered through Maton and may create persistent local authentication state.

Mitigation: Prefer OAuth login and verify authentication with the CLI rather than inspecting stored credentials.

Risk: Creating a new Kaggle connection or performing account-changing actions can affect the user's Kaggle account.

Mitigation: Confirm any new connection or account-changing action with the user before execution.

Risk: Raw API-key mode exposes a long-lived Maton credential when the CLI cannot be used.

Mitigation: Avoid raw API-key mode unless installation is impossible, and never print, log, persist, or pass the key on a command line.

## Reference(s):

- [Kaggle Skill on ClawHub](https://clawhub.ai/byungkyu/skills/kaggle-api)
- [Maton](https://maton.ai)
- [Kaggle API Documentation](https://www.kaggle.com/docs/api)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Kaggle Models](https://www.kaggle.com/models)
- [Kaggle Competitions](https://www.kaggle.com/competitions)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance, Code]

**Output Format:** [Markdown with inline shell commands, JSON request and response examples, and SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Kaggle API requests and binary download responses through Maton-managed authentication.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
