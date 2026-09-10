## Description:

Collect structured GitHub repository information from one or more known repository URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to prepare Dataify Builder requests for GitHub repository collection, submit the task, wait for completion when requested, and return the collected JSON result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broader GitHub and search-style collection paths than the repository-URL name suggests.

Mitigation: Use the repository-URL collection path unless the user explicitly requests another available Dataify tool.

Risk: Generated curl commands and task submissions depend on user-provided URLs and parameters.

Mitigation: Review generated commands before execution and avoid running commands built from untrusted input.

Risk: The skill uses a Dataify API token and includes guidance for persistent shell profile storage.

Mitigation: Prefer a session-scoped DATAIFY_API_TOKEN and rotate the token if it may have appeared in logs or command history.

## Reference(s):

- [Tool parameter catalog](artifact/references/tool-params.json)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-github-repository-by-repo-url)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit paid Dataify tasks, wait for asynchronous completion, and summarize large JSON payloads while preserving access to raw results.]

## Skill Version(s):

1.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
