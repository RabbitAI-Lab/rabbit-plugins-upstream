## Description:

Short-form video market research via the Virlo API for viral niche research, trend tracking, creator vetting, hashtag, sound, and hook intelligence across TikTok, YouTube Shorts, and Instagram Reels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arod90](https://clawhub.ai/user/arod90)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, creators, agencies, and developers use this skill to query Virlo for short-form social intelligence, run niche or creator analyses, and set up recurring monitoring with cost-aware API guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Virlo API key and authorizes the agent to call the Virlo API.

Mitigation: Install only when the user is comfortable granting API access, keep the key in the configured environment variable, and avoid asking for or exposing the key in chat.

Risk: Normal use can trigger paid Virlo API calls, including one-shot searches, trend checks, deeper histories, and tracking cycles.

Mitigation: Confirm the intended endpoint, expected cost, and prepaid balance before paid calls; check Virlo billing headers and handle insufficient-balance responses without retrying.

Risk: Recurring monitors, tracking cadences, and autopilot behavior can continue collecting data or widening collection over time.

Mitigation: Confirm cadence, target, and autonomy settings before enabling recurring behavior, and review proposals, pauses, deletions, or collection-depth changes before applying them.

Risk: Asynchronous results may be incomplete while secondary jobs are still running.

Mitigation: Check finalized status, pending jobs, confidence fields, and per-item intelligence status before presenting analysis as complete or actionable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/arod90/skills/short-form-market-research-brain)
- [Virlo API Documentation](https://dev.virlo.ai/docs)
- [Virlo Agent Playbook](https://dev.virlo.ai/agent-playbook.txt)
- [Virlo Pricing](https://dev.virlo.ai/pricing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl commands, JSON request examples, and summarized market-research findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires VIRLO_API_KEY and can make paid Virlo API calls for searches, monitoring, tracking, and deeper analyses.]

## Skill Version(s):

1.12.0 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
