## Description:

CMO-style go-to-market coach that helps founders confirm positioning, identify the current bottleneck, choose one weekly GTM bet, and create one marketing artifact or hand off community replies to NicheReach.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shujip](https://clawhub.ai/user/shujip)

### License/Terms of Use:

MIT-0

## Use Case:

External founders and operators use this agent skill to run a lightweight GTM board, preserve local GTM state, choose one channel bet for the week, and draft a bounded artifact such as positioning, outreach, launch copy, or campaign guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can silently update persisted agent instructions at the start of a new session.

Mitigation: Review the updated skill bundle before use and prefer a project-level install where changes are easier to inspect.

Risk: The skill stores a reusable project token in a local plaintext workspace file.

Mitigation: Use only trusted workspaces, keep workspace secret files out of version control and indexing, and rotate or revoke the token if the workspace may have been exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shujip/skills/gtm-coach)
- [Publisher profile](https://clawhub.ai/user/shujip)
- [GTM Coach homepage](https://www.nichestarter.ai/gtm-coach)
- [Canonical GTM Coach skill bundle](https://www.nichestarter.ai/skills/gtm-coach/)
- [Nichestarter agent manifest](https://www.nichestarter.ai/api/gtm/agent)
- [NicheReach](https://www.nichestarter.ai/reach)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise prose, structured GTM board sections, JSON state files, and inline shell commands when installation or persistence is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one bounded recommendation or artifact at a time; Reddit and Facebook replies are handed off to NicheReach instead of drafted in the agent.]

## Skill Version(s):

1.4.1 (source: frontmatter, changelog, server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
