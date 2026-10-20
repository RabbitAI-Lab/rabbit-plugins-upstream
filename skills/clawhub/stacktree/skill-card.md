## Description:

Helps an agent publish and update HTML pages on Stacktree and share them through unlisted links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stevysmith](https://clawhub.ai/user/stevysmith)

### License/Terms of Use:

MIT-0

## Use Case:

Personal agents and their users publish briefs, dashboards, reports, and other HTML pages to shareable links, then update or manage those pages as needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing a page sends its contents to Stacktree, potentially exposing secrets, regulated data, or personal information.

Mitigation: Review and approve page contents before upload; remove sensitive information.

Risk: Sending an owner email discloses the address to Stacktree and triggers email notifications.

Mitigation: Obtain explicit consent before sending any email address.

Risk: Claim tokens, receipt URLs, API keys, and wallet keys can grant access to pages or payments if disclosed.

Mitigation: Store them as credentials; do not include them in shared pages, chat transcripts, or command arguments.

Risk: Paid publishing can spend USDC, while activity lookups and deletion can reveal page activity or remove a page.

Mitigation: Require explicit approval for payments, activity lookups, and page deletion; verify payment terms before paying.

## Reference(s):

- [stacktree on ClawHub](https://clawhub.ai/stevysmith/skills/stacktree)
- [Stacktree documentation map](https://stacktr.ee/agent.txt)
- [Stacktree payment documentation](https://stacktr.ee/x402.md)
- [Stacktree authentication documentation](https://stacktr.ee/auth.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [HTML source, page links, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Free anonymous pages expire after 24 hours unless claimed; paid pages and updates may require credentials.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
