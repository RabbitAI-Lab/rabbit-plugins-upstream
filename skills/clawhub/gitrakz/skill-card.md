## Description:

Drive a self-hosted gitrakz instance to install or run it, trigger and monitor GitHub activity syncs, query timelines and sessions, and run or export templates through its REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate a trusted, self-hosted gitrakz server: install or run it, start and monitor syncs, retrieve activity timelines and work sessions, and execute template exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help trigger Docker setup and installer workflows.

Mitigation: Inspect the installer before running it and prefer pinned release images for normal operation.

Risk: The gitrakz server uses GitHub activity access and may spend GitHub API rate limit during sync.

Mitigation: Use a read-scoped GitHub token and trigger sync only for the user-requested task.

Risk: An exposed gitrakz API can be open if no bearer token is configured.

Mitigation: Keep the API bound to localhost, or set GITRAKZ_AUTH_TOKEN before exposing it beyond a trusted machine.

Risk: Optional LLM features can send commit and diff-derived data to the configured model provider.

Mitigation: Leave LLM settings empty unless the user accepts that data flow and trusts the configured provider.

## Reference(s):

- [gitrakz setup guide](references/setup.md)
- [gitrakz source repository](https://github.com/psyb0t/gitrakz)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/gitrakz)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, REST API requests, and JSON-oriented examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl commands, Docker commands, configuration steps, API endpoint guidance, and export instructions.]

## Skill Version(s):

0.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
