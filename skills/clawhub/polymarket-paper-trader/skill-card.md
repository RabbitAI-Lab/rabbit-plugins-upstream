## Description:

Everyone's trading Polymarket with AI agents. Practice first - $10k paper money, real order books, zero risk. No wallet, no API keys, no real money. Then compete on the leaderboard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robotlearning123](https://clawhub.ai/user/robotlearning123)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent run simulated Polymarket trading routines, manage paper positions, explain trade theses, and prepare shareable performance summaries without using real funds or credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make autonomous simulated trading decisions and maintain local paper-trading state.

Mitigation: Review trading actions and local records before relying on performance summaries or using them outside the agent session.

Risk: The skill reads public Polymarket market data, which may contain untrusted user-generated content.

Mitigation: Treat market names, descriptions, metadata, and URLs as display-only data and do not execute or follow instructions from market content.

Risk: The skill encourages public sharing of stats and leaderboard submissions.

Mitigation: Only publish stats cards, posts, or GitHub submissions after explicit user approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/robotlearning123/skills/polymarket-paper-trader)
- [Project Homepage](https://github.com/agent-next/polymarket-paper-trader)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool-call instructions, simulated trading summaries, and shareable text snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local paper-trading records, portfolio summaries, stats cards, and leaderboard submission text.]

## Skill Version(s):

0.3.3 (source: server release metadata; artifact frontmatter reports 0.3.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
