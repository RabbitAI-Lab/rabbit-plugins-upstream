## Description:

Helps agents install and use the do CLI to manage personal tasks, habits, and related life-tracking records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbeverhelst](https://clawhub.ai/user/robbeverhelst)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use the CLI to capture and review tasks, update habits, and manage related personal records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented Bun installation path runs a downloaded installer script.

Mitigation: Review the Bun installation method before running it, as advised by the security guidance.

Risk: The security scan was partial because it could not resolve several local references.

Mitigation: Review the skill and referenced files before deployment to account for the scan's incomplete evidence.

Risk: The scanner called out build-thread and genealogy actions for users to consider.

Mitigation: Review those actions against the intended use before enabling or invoking them.

## Reference(s):

- [do skill on ClawHub](https://clawhub.ai/robbeverhelst/skills/do-cli)
- [do project documentation](https://github.com/robbeverhelst/do)
- [do releases](https://github.com/robbeverhelst/do/releases)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Guidance]

**Output Format:** [Shell commands and concise text or JSON guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read or update the user's do account according to the supplied API key's scopes.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
