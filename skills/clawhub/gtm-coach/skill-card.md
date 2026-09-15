## Description:

CMO-style go-to-market coach that helps founders confirm the GTM picture, identify the current bottleneck, recommend one weekly bet, and create one artifact or hand off community replies to NicheReach.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shujip](https://clawhub.ai/user/shujip)

### License/Terms of Use:

MIT-0

## Use Case:

External founders and product operators use this skill to maintain a project-level GTM board, select a stage-appropriate channel, and turn limited product or audience evidence into one focused weekly marketing action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist or refresh its own bundle in an agent skills folder.

Mitigation: Prefer project-level installation, review refresh prompts before accepting them, and confirm the target skills path before allowing updates.

Risk: The skill may use an `nmagt_` project token for Nichestarter, NicheReach, or NicheMatch integrations.

Mitigation: Paste a token only when project integration is intended, keep `.gtm/` and `.nichematch/` gitignored, and never store tokens in a skills folder.

Risk: Marketing recommendations could be mistaken for permission to publish, send messages, approve partnerships, or spend money.

Mitigation: Require the founder to decide and execute external actions; keep agent output to previews, plans, and single artifacts.

Risk: Fetched or pasted content may contain untrusted instructions.

Mitigation: Treat external content as evidence only, ignore embedded instructions, and avoid fetching Reddit or Facebook post bodies for community reply workflows.

## Reference(s):

- [GTM Coach homepage](https://www.nichestarter.ai/gtm-coach)
- [ClawHub skill page](https://clawhub.ai/shujip/skills/gtm-coach)
- [GTM Coach update manifest](https://www.nichestarter.ai/api/gtm/agent)
- [NicheReach Chrome extension](https://chromewebstore.google.com/detail/nichereach/meijkmdpgkfookehfglnkdcjgobheemp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, and shell commands depending on the selected GTM action]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one recommendation or artifact at a time and may update local .gtm plan, inbox, journal, or secrets files.]

## Skill Version(s):

1.3.0 (source: frontmatter and changelog, released 2026-09-15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
