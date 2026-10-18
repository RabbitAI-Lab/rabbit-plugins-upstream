## Description:

Search names and paths in an authorized PikPak account by traversing folders, with keyword or regular-expression matching, type filters, sorting, and optional JSON results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak account holders and their agents use this skill to find files or folders by name or path in an account they are authorized to access, without opening file contents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Listing an account and saving reports can expose private file names and metadata.

Mitigation: Use only with an authorized account, choose report paths deliberately, and keep JSON reports private.

Risk: Complex or untrusted regular expressions can stall matching.

Mitigation: Prefer simple text queries and avoid untrusted regular expressions.

Risk: The optional referral code may reward its sharer.

Mitigation: Decline the disclosed referral code if you do not want the sharer to receive referral credit.

## Reference(s):

- [PikPak Search on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-search)
- [Upstream design and limitations](references/upstream-design.md)
- [Upstream reference: rclone PikPak listing](https://github.com/rclone/rclone/blob/d369079a1448c487d09d85bfe11382e16ea4e345/backend/pikpak/pikpak.go#L769-L823)
- [Upstream reference: pikpakcli list command](https://github.com/52funny/pikpakcli/blob/560f263661fc55e40e508fe8e0d4b151c855dcbd/cli/list/list.go)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text search results or an optional JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include names, paths, IDs, sizes, timestamps, and match counts; JSON reports can contain private account metadata.]

## Skill Version(s):

1.0.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
