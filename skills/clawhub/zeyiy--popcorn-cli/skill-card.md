## Description:

Popcorn CLI helps agents use the popcorn-cli command line tool to query Popcorn models, submit asynchronous image or video generation tasks, manage folders, upload resources, and check task results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zeyiy](https://clawhub.ai/user/zeyiy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to automate Popcorn media-generation workflows from the command line, including model selection, task submission, status polling, resource upload, and folder organization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and relies on an external npm CLI package.

Mitigation: Install only if the npm package publisher is trusted and review the package before deployment.

Risk: The Popcorn API key is stored in a local plaintext configuration file.

Mitigation: Restrict access to ~/.popcorn-cli/config.json, avoid shared machines and CI logs, use a limited API key where possible, and rotate the key if exposure is suspected.

Risk: Generation prompts, task parameters, selected uploaded files, and related metadata are sent to Popcorn services.

Mitigation: Do not include passwords, secrets, personal data, unauthorized customer data, or other confidential information in prompts, task parameters, uploaded files, logs, or shared artifacts.

## Reference(s):

- [Popcorn CLI installation guide](https://mangaforge-qa-1255521909.cos.ap-shanghai.myqcloud.com/docs/popcorn-cli/popcorn-cli-installation-guide.html)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Popcorn task IDs, session IDs, folder IDs, resource URLs, status summaries, and error summaries.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
