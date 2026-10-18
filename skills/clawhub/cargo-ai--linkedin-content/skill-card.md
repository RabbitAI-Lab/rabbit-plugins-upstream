## Description:

Drafts three source-cited LinkedIn posts each week from a team's existing proof points, objections, and recent insights, delivering them in one pull request for human review without publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing and sales teams use this skill to prepare weekly LinkedIn drafts for a named author using existing company records. A human reviews the pull request and decides whether to publish.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository convention files can override the agent's safety limits and change what it reads, writes, or runs.

Mitigation: Review and revise the prompt before installation so repository instructions cannot override authorized paths, output destinations, or prohibited commands.

Risk: The weekly agent reads repository context and cadence content and can push a branch and open a pull request.

Mitigation: Install only where those read and GitHub permissions are acceptable; review generated drafts and their cited sources before publication.

## Reference(s):

- [Draft format and citation rules](references/post.md)
- [Publisher-provided project homepage](https://github.com/getcargohq/gtm-skills)
- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/linkedin-content)

## Skill Output:

**Output Type(s):** [Markdown, Files]

**Output Format:** [Markdown drafts in a weekly pull request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to three drafts with source file citations; no automatic publishing.]

## Skill Version(s):

0.1.1 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
