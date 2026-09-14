## Description:

Guides an agent to generate short-video spoken scripts with contrast hooks, resonant story structure, colloquial delivery, and personal IP positioning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content teams use this skill to draft short-video spoken scripts for character stories, audience pain points, and personal IP viewpoint content. The skill can also guide dLazy CLI setup and external generation workflows when users intentionally choose that path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is presented as a spoken-script helper but can lead an agent to install and run an external dLazy CLI workflow.

Mitigation: Review the skill before installation and enable it only when the external dLazy workflow is intended.

Risk: The dLazy CLI workflow requires API authentication and may store a reusable API key in local configuration.

Mitigation: Use scoped credentials where possible, protect the local configuration file, and rotate or revoke keys from the dLazy dashboard when access is no longer needed.

Risk: Prompts and supplied local image, video, or audio paths may be sent or uploaded to dLazy services.

Mitigation: Do not provide sensitive prompts or media unless external processing is acceptable and the user has the right to upload the content.

Risk: Installing or invoking npm packages introduces third-party package and account dependencies.

Mitigation: Review the referenced npm package and source repository, and prefer pinned or approved installation paths in managed environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with optional shell command snippets and generated media URLs when the dLazy CLI workflow is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should follow the seven-step spoken-script structure unless the user requests a different presentation.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
