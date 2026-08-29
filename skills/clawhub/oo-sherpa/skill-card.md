## Description:

Sherpa helps agents query personalized travel restrictions, visa requirements, required documents, and trip summaries through an OOMOL-connected Sherpa account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Travel advisors, support teams, and developers use this skill to look up personalized travel restrictions, visa and document requirements, and concise trip summaries for a user's itinerary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an OOMOL-connected Sherpa account to query travel and visa information for user itineraries.

Mitigation: Install and invoke it only for intentional Sherpa travel-information lookups, and confirm the itinerary details before running connector actions.

Risk: Connector access depends on local oo CLI authentication and an active Sherpa connection.

Mitigation: Review the one-time CLI installation and account-connection steps before installation, and run setup only after an auth or connection failure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-sherpa)
- [Sherpa Homepage](https://www.joinsherpa.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands; connector responses may be JSON or Markdown depending on the action.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before request payloads; no files are produced by default.]

## Skill Version(s):

1.0.1 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
