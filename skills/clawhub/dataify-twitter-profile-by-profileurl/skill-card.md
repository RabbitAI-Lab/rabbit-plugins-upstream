## Description:

Collects an X/Twitter profile from a known profile URL and is not intended for posts, keyword search, or arbitrary X URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect X/Twitter profile data through Dataify from a known profile URL, wait for the asynchronous task, and return the collected result. Reviewers should note that the artifact also exposes broader username and post collection options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release advertises a narrow profile-URL workflow while also enabling username and post collection through Dataify.

Mitigation: Constrain normal use to the profile-URL tool unless the user explicitly requests a broader collection mode and accepts the scope and cost implications.

Risk: The skill requires a Dataify API token and submits scraping jobs to an external paid API.

Mitigation: Use session-scoped token setup where practical, never display the token, and confirm high-volume or materially costly collection scopes before execution.

## Reference(s):

- [Saved Dataify tool parameters](references/tool-params.json)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-twitter-profile-by-profileurl)
- [Dataify Builder API endpoint](https://scraperapi.dataify.com/builder)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task ID and resume command when asynchronous monitoring times out or is interrupted.]

## Skill Version(s):

1.3.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
