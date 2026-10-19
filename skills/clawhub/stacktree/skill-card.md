## Description:

Publishes agent-created HTML as shareable Stacktree pages and helps manage their links, updates, and access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stevysmith](https://clawhub.ai/user/stevysmith)

### License/Terms of Use:

MIT-0

## Use Case:

People using personal agents can publish briefs, dashboards, reports, and other HTML pages to a shareable link, then update or manage those pages when authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing sends page contents to an external service, potentially exposing private or sensitive material.

Mitigation: Review content before upload; do not publish private, regulated, client, or secret-bearing material without explicit approval.

Risk: Paid publishing or account provisioning can spend funds.

Mitigation: Confirm each paid action with the user before proceeding.

Risk: Claim tokens, API keys, wallet signatures, and local wallet keys can grant access to pages or funds.

Mitigation: Keep credentials out of transcripts and logs; never expose the local wallet key to the agent conversation.

Risk: Page replacement or deletion can change or remove a shared page; viewer activity and email addresses are sensitive.

Mitigation: Confirm before replacing or deleting pages, sending an email address, or checking viewer activity.

## Reference(s):

- [Stacktree skill release](https://clawhub.ai/stevysmith/skills/stacktree)
- [Stacktree paid publishing guide](https://stacktr.ee/x402.md)
- [Stacktree authentication guide](https://stacktr.ee/auth.md)
- [Stacktree agent overview](https://stacktr.ee/agent.txt)

## Skill Output:

**Output Type(s):** [HTML, Markdown, Shell commands, Guidance]

**Output Format:** [HTML pages, published URLs, and text instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Page links may expire; authorized updates can retain the same URL.]

## Skill Version(s):

1.0.4 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
