## Description:

GTM Coach helps founders run a weekly CMO-style go-to-market planning loop, choose one focused growth bet, and produce grounded GTM artifacts without publishing or sending on their behalf.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shujip](https://clawhub.ai/user/shujip)

### License/Terms of Use:

MIT-0

## Use Case:

External founders and operators use this skill to confirm their go-to-market stage, select one weekly growth bet, draft artifacts such as outreach, interview scripts, dashboards, scorecards, and Build-in-Public posts, and record learning in a workspace .gtm plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist itself and apply remote updates while handling a live project token.

Mitigation: Require explicit approval for persistence, update application, token storage, and NicheMatch loading; inspect remote updates before allowing them to overwrite local skill files.

Risk: Project tokens may be stored in workspace files if the agent follows the skill flow.

Mitigation: Keep .gtm/ and .nichematch/ gitignored, avoid committing tokens, and prefer a real secret store over .gtm/secrets.md.

Risk: Go-to-market recommendations may rely on incomplete or unverified project evidence.

Mitigation: Keep the founder in the approval loop and do not publish, send messages, spend money, or approve partnerships without explicit review.

## Reference(s):

- [ClawHub GTM Coach release page](https://clawhub.ai/shujip/skills/gtm-coach)
- [Nichestarter GTM Coach homepage](https://www.nichestarter.ai/gtm-coach)
- [Canonical GTM Coach skill bundle](https://www.nichestarter.ai/skills/gtm-coach/)
- [NicheReach Chrome extension](https://chromewebstore.google.com/detail/nichereach/meijkmdpgkfookehfglnkdcjgobheemp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with optional JSON plan files, HTML dashboard files, scorecard Markdown, Build-in-Public draft Markdown, and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local .gtm workspace files and skill installation commands; founder approval is required before publishing, sending messages, spending money, or approving partnerships.]

## Skill Version(s):

1.5.1 (source: frontmatter, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
