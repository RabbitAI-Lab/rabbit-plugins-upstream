## Description:

Collect structured Crunchbase company profiles from one or more known Crunchbase company URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit known Crunchbase organization URLs to Dataify, wait for the asynchronous collection task, and return structured company profile results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Dataify API token and sends requested company targets to Dataify.

Mitigation: Install only when that credential and target data sharing are acceptable, keep the token in environment variables, and never paste the token into chat.

Risk: Generated curl commands and user-supplied values can be unsafe when inputs are not trusted or shell-escaped.

Mitigation: Review generated commands before execution, use trusted inputs, and prefer direct script submission or preview mode over manually editing shell commands.

Risk: The artifact includes broader scraping workflows and keyword modes beyond the Crunchbase URL-focused release description.

Mitigation: Use only the Crunchbase organization URL workflow for this release and avoid generic research or keyword modes unless separately reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-crunchbase-company-by-url)
- [Tool parameter catalog](references/tool-params.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN and may return a task ID with a resume command if collection does not complete within the wait window.]

## Skill Version(s):

1.3.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
