## Description:

Converts a Claude Code session into a blog post, case study, or Reddit post

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill after a meaningful Claude Code session to turn git history, file changes, test output, metrics, and conversation context into shareable engineering posts. It supports blog posts, case studies, social threads, and Reddit posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated posts can expose repository history, diffs, test output, metrics, or conversation details that were not intended for public release.

Mitigation: Review every draft before sharing and remove secrets, private roadmap details, customer or internal identifiers, unreleased work, and unintended conversation-derived claims.

Risk: Published drafts may contain unsupported metrics or claims about what happened in the session.

Mitigation: Use the skill's proof-of-work and verification steps, keep evidence for concrete claims, and remove claims that cannot be verified.

Risk: External community posts may be misaligned with subreddit or forum expectations.

Mitigation: Confirm the target community's rules and norms before posting, and prepare links or setup details as follow-up material instead of overloading the main post.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-session-to-post)
- [Homepage listed in ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/scribe)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown drafts with inline shell command snippets and publication notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include blog, case study, social thread, Reddit post, quality-gate report, and first-comment content depending on the selected format.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
