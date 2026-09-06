## Description:

Collect structured GitHub repository information from one or more known repository URLs; do not use for GitHub code search or arbitrary webpages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to prepare and run Dataify Builder requests for collecting structured data from known GitHub repository URLs, then wait for and return the collected result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the workflow broadens a repository-URL skill into GitHub URL/search collection using an external API token and paid task submission.

Mitigation: Use repository URL collection by default and require explicit confirmation before running search URL or generic URL modes or any scope that materially changes credit use.

Risk: The skill sends GitHub targets to Dataify using DATAIFY_API_TOKEN.

Mitigation: Verify only that DATAIFY_API_TOKEN is present, never print or ask users to paste the token, and run only user-approved collection targets.

Risk: Interrupted monitoring can lead to accidental duplicate paid submissions if the original task is resubmitted.

Mitigation: Capture and return the task ID with a resume command whenever monitoring times out or is interrupted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-github-repository-by-repo-url)
- [Tool parameter catalog](artifact/references/tool-params.json)
- [Dataify Builder API endpoint](https://scraperapi.dataify.com/builder)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown with shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task ID and resume command if monitoring times out or is interrupted.]

## Skill Version(s):

1.3.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
