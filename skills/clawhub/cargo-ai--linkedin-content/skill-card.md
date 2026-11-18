## Description:

Drafts three weekly LinkedIn posts from a team's documented proof points and cadence log, then submits them for human review in one pull request; it never publishes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Go-to-market teams and company leaders use this skill to turn documented customer results, buyer objections, and recent insights into cited weekly LinkedIn drafts for a named author. The author reviews the pull request and decides whether to publish by hand.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One referenced script was only partly inspected, and the installation mechanism received a security note.

Mitigation: Review the skill instructions and installation steps before proceeding.

## Reference(s):

- [Draft format](references/post.md)
- [LinkedIn Content project homepage](https://github.com/getcargohq/gtm-skills/tree/main/linkedin-content)
- [ClawHub release page](https://clawhub.ai/cargo-ai/skills/linkedin-content)

## Skill Output:

**Output Type(s):** [Markdown, Files]

**Output Format:** [One Markdown file containing up to three weekly post drafts, hooks, cited source paths, and any unsupported draft type.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each draft is for one named author, under 1,300 characters, and grounded in listed files. The file is delivered in one pull request for review; nothing is published.]

## Skill Version(s):

0.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
