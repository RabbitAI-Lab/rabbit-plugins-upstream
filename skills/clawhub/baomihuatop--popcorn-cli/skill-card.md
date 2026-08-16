## Description:

Popcorn CLI helps agents use the popcorn-cli command line tool to query available Popcorn image and video models, submit asynchronous generation tasks, and check task status by session or task ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[baomihuatop](https://clawhub.ai/user/baomihuatop)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation engineers, and agents use this skill to automate Popcorn image and video generation workflows from the command line. It supports model discovery, task submission, and polling for generated results while keeping API-key and remote-transmission handling visible to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, task parameters, session identifiers, and generation settings are sent to the remote Popcorn backend.

Mitigation: Avoid submitting secrets, personal data, or unauthorized customer information in prompts or task parameters; treat returned IDs, URLs, and errors as sensitive workflow data.

Risk: The API key is stored locally in ~/.popcorn-cli/config.json.

Mitigation: Restrict access to the user home directory and config file, keep the config out of repositories and logs, and rotate the key if exposure is suspected.

Risk: The unpinned npm package currently includes file-upload and folder-management capabilities beyond the submitted skill artifact.

Mitigation: Verify the installed popcorn-cli version and available command set before use, and deploy only in environments where those broader CLI capabilities are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/baomihuatop/skills/popcorn-cli)
- [Server-resolved GitHub provenance](https://github.com/baomihuatop/popcorn-cli)
- [Popcorn CLI installation guide](https://mangaforge-qa-1255521909.cos.ap-shanghai.myqcloud.com/docs/popcorn-cli/popcorn-cli-installation-guide.html)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command outputs may include task IDs, session IDs, result URLs, and error messages that should be handled as sensitive workflow data.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter says 0.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
