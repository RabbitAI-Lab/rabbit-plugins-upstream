## Description:

Schedule, publish, and cross-post social media posts to X, LinkedIn, Instagram, Facebook, TikTok, Threads, YouTube, and Bluesky.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackvitick](https://clawhub.ai/user/jackvitick)

### License/Terms of Use:

MIT-0

## Use Case:

External users and social media operators use this skill to plan calendars, draft platform-specific posts, and schedule or publish approved content through Socialync-connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish or schedule posts to real social accounts after authorization.

Mitigation: Review the draft, target profile, platforms, and timing before approval; revoke Socialync access from account settings when the connection is no longer needed.

Risk: A post could be sent to the wrong brand profile or disconnected platform if preflight checks are skipped.

Mitigation: List profiles, check quota, and confirm connected platform health before creating or scheduling posts.

Risk: Retries or quota limits can create confusion about what was published or leave a batch incomplete.

Mitigation: Check scheduled posts and post history before retrying, then read back scheduled or published items after every write.

## Reference(s):

- [Socialync homepage](https://www.socialync.io)
- [Socialync MCP endpoint](https://mcp.socialync.io/mcp)
- [Platform playbook](artifact/platform-playbook.md)
- [Publishing reference](artifact/publishing.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, prose, and inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafting can run without an account; publishing requires a user-authorized Socialync connection and explicit confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
