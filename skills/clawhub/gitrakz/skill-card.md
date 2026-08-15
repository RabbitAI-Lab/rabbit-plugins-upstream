## Description:

Drive a self-hosted gitrakz instance to sync GitHub activity into local SQLite, inspect timelines and work sessions, and run deterministic templates that export to CSV, PDF, or JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install, run, and query a trusted self-hosted gitrakz service for GitHub activity timelines, work-session summaries, template runs, and exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local service reads and stores GitHub activity and depends on a GitHub token.

Mitigation: Use a least-privilege GitHub token, run only against a trusted gitrakz instance, and avoid searching the workspace for secrets.

Risk: The gitrakz API may be open when GITRAKZ_AUTH_TOKEN is unset or exposed beyond localhost.

Mitigation: Keep the service bound to localhost by default, or protect the API with GITRAKZ_AUTH_TOKEN before exposing it.

Risk: Optional LLM template features can send commit metadata or diffs to the configured provider.

Mitigation: Leave LLM settings empty unless the user accepts that data flow and trusts the configured provider.

## Reference(s):

- [gitrakz setup reference](references/setup.md)
- [gitrakz ClawHub release page](https://clawhub.ai/psyb0t/skills/gitrakz)
- [gitrakz project homepage](https://github.com/psyb0t/gitrakz)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline bash commands and REST API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON request or response examples for gitrakz REST endpoints.]

## Skill Version(s):

0.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
