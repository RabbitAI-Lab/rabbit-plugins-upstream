## Description:

Lets go-to-market teams ask questions from Slack, request reviewable repository changes, capture useful threads, and approve work handed to deployed agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations, sales leadership, and go-to-market engineering teams use a Slack agent to query their repository and workspace, propose and review changes through pull requests, and approve operational work in a thread.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Slack channel access can expose private repository or workspace information in shared or customer channels.

Mitigation: Replace all-channel access with an internal channel allowlist, or verify the bot is absent from every shared and customer channel before installation.

Risk: Repository permissions may allow changes beyond the intended project.

Mitigation: Review and restrict the GitHub connector scope before deployment.

Risk: Excessive workspace permissions could let Slack requests change resources.

Mitigation: Keep the service user on the viewer role.

Risk: Capturing Slack threads in the repository may retain sensitive conversation content.

Mitigation: Require review and redaction before capturing threads.

Risk: Installing an unpinned Cargo CLI version can change deployed behavior unexpectedly.

Mitigation: Pin and review the Cargo CLI version used for installation.

## Reference(s):

- [Ask Cargo skill listing](https://clawhub.ai/cargo-ai/skills/ask-cargo)
- [Cargo GTM skills homepage (listed in metadata)](https://github.com/getcargohq/gtm-skills)
- [Agent roster reference](artifact/references/roster.md)
- [Slack capture reference](artifact/references/capture-entry.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Slack thread replies and reviewable repository pull requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers cite their sources; changes remain unmerged; work requiring approval is proposed in the Slack thread before execution.]

## Skill Version(s):

0.2.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
