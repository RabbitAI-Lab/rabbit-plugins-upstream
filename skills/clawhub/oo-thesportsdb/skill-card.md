## Description:

Helps agents retrieve TheSportsDB scores, schedules, catalogs, and details about leagues, teams, players, events, and venues through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can look up sports entities, schedules, live scores, and catalog data using a connected TheSportsDB account. Name-based entity search requires a Premium API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests piping a remotely downloaded installer directly into a shell.

Mitigation: Review installation instructions and prefer a trusted package manager or an installer verified by source review, signatures, or checksums; do not run the one-line installer blindly.

## Reference(s):

- [TheSportsDB skill on ClawHub](https://clawhub.ai/oomol/skills/oo-thesportsdb)
- [TheSportsDB](https://www.thesportsdb.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Plain text or Markdown summaries of TheSportsDB results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the connected account and TheSportsDB availability; name search requires a Premium API key.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
