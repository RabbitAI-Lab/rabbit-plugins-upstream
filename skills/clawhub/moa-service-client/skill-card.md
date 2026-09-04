## Description:

MOA Service Client helps agents submit repository-pinned technical-design briefs to an internal MOA Service, monitor asynchronous runs, diagnose failures, and download verified artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrewxu12138](https://clawhub.ai/user/andrewxu12138)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized MOA operators use this skill to create repository-pinned technical-design runs from detailed briefs, monitor them to terminal status, diagnose allowed failures, and retrieve verified review artifacts without modifying source repositories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release ships sensitive local credentials.

Mitigation: Remove the shipped credentials.local.env token before installation and provision MOA_TOKEN through the runtime environment or a secret manager.

Risk: The skill includes broad operator and admin diagnostic capabilities.

Mitigation: Limit admin and diagnostic commands to authorized operators; ordinary users should use the create, run, status, wait, and result workflows.

Risk: Design prompts, repository URLs, commit IDs, callback URLs, and downloaded artifacts are exchanged with the configured MOA service.

Mitigation: Treat these values as service-exchanged data, use only approved endpoints and callbacks, and verify artifact hashes before relying on downloaded results.

## Reference(s):

- [MOA Service Agent Guide](AGENT_GUIDE.md)
- [MOA HTTP Contract](references/http-contract.md)
- [MOA Operations and Failure Playbook](references/operations.md)
- [MOA Callback Guide](references/callbacks.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands; client responses are JSON and downloaded artifacts can include Markdown, JSON, XLSX, and manifest files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires pinned repository URLs and exact commit SHAs; successful downloads verify advertised SHA-256 hashes.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
