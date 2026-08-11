## Description:

Popcorn CLI helps agents use the popcorn-cli command-line client to query available Popcorn models, submit asynchronous image and video generation tasks, upload and list media resources, manage folders, and check task status through a local API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zeyiy](https://clawhub.ai/user/zeyiy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to automate Popcorn media-generation workflows, including model discovery, task submission, result polling, media resource upload, and folder organization. It is intended for users who already trust the Popcorn backend and can protect the local API key configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local popcorn-cli configuration stores an API key in ~/.popcorn-cli/config.json.

Mitigation: Restrict access to the local configuration file, keep it out of repositories and logs, and rotate the API key if exposure is suspected.

Risk: Prompts, uploaded files, task IDs, result URLs, folder IDs, and generation parameters may be sent to or returned from the Popcorn backend.

Mitigation: Use the skill only with a trusted Popcorn backend and avoid submitting secrets, private data, or unauthorized customer material in prompts, uploads, or task parameters.

Risk: Generated media tasks are asynchronous, so submission responses do not contain final results.

Mitigation: Poll task status until a terminal state before using result URLs or reporting completion.

Risk: Resource and folder commands depend on the installed CLI version matching the documented behavior.

Mitigation: Verify the installed popcorn-cli version before relying on resource and folder workflows.

## Reference(s):

- [Popcorn CLI installation guide](https://mangaforge-qa-1255521909.cos.ap-shanghai.myqcloud.com/docs/popcorn-cli/popcorn-cli-installation-guide.html)
- [Popcorn CLI skill page](https://clawhub.ai/zeyiy/skills/popcorn-cli)
- [Publisher profile](https://clawhub.ai/user/zeyiy)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce command sequences for Popcorn model discovery, task submission, task polling, resource upload, resource search, and folder management.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter reports 0.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
