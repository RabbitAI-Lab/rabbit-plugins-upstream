## Description:

Make (formerly Integromat) API integration with managed authentication for managing scenarios, organizations, teams, connections, data stores, hooks, and templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to administer Make accounts through Maton, automate workflows, manage scenarios and related resources, and integrate apps while keeping write actions behind explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or change persistent Make automations and related resources that continue operating after the conversation ends.

Mitigation: Review the target resource, payload, and intended effect with the user before any write action, and confirm starts, creates, updates, deletes, hooks, functions, triggers, and destinations explicitly.

Risk: Raw Maton API keys are long-lived credentials that can leak through environment exposure, logs, shell history, crash dumps, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI, use raw API keys only when the CLI cannot be used, and never print, persist, log, or pass the key on a command line.

Risk: Ambiguous Maton accounts or Make connections can route reads or writes to the wrong account.

Mitigation: List and verify available connections first, specify the intended connection or profile when more than one exists, and default to read or list operations before proposing changes.

## Reference(s):

- [Make Skill on ClawHub](https://clawhub.ai/byungkyu/skills/make-api)
- [Maton Homepage](https://maton.ai)
- [Make API Documentation](https://developers.make.com/api-documentation)
- [Make API Reference](https://developers.make.com/api-documentation/api-reference)
- [Make Help Center](https://www.make.com/en/help)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and API endpoint guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on Maton CLI or raw HTTPS calls, managed authentication, least-privilege account selection, and explicit approval before writes or persistent automation changes.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
