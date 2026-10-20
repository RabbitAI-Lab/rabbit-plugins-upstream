## Description:

Guides agents using Popcorn CLI to generate images and videos, upload assets, manage folders, and check task results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[baomihuatop](https://clawhub.ai/user/baomihuatop)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Popcorn CLI to find available models, submit image and video generation tasks, retrieve results, and organize uploaded resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Popcorn API key is stored in a local configuration file.

Mitigation: Restrict access to the config file, never log or share the key, and rotate it if exposed.

Risk: Prompts, generation settings, and uploaded files are sent to Popcorn's remote service.

Mitigation: Only submit content approved for upload; exclude confidential prompts, private customer data, and sensitive files.

## Reference(s):

- [Popcorn CLI installation guide](https://mangaforge-qa-1255521909.cos.ap-shanghai.myqcloud.com/docs/popcorn-cli/popcorn-cli-installation-guide.html)
- [Popcorn CLI on ClawHub](https://clawhub.ai/baomihuatop/skills/popcorn-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands and task-status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation tasks are asynchronous; results require a follow-up task lookup.]

## Skill Version(s):

0.2.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
