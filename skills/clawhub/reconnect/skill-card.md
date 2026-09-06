## Description:

Reconnect helps agents find relevant professional contacts, prepare reviewable shortlists, and track explicitly authorized LinkedIn outreach across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and professionals use this skill to research peers, collaborators, mentors, event contacts, and existing contacts, then review evidence and continue authorized outreach batches without losing state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use public professional profile research and authenticated browser sessions for LinkedIn actions after user approval.

Mitigation: Require explicit approval for each outreach scope, review every batch, keep LinkedIn work sequential, and stop on warnings, limits, verification challenges, or account uncertainty.

Risk: Project records are stored in a local unencrypted ledger.

Mitigation: Keep project databases outside the installed skill, use private filesystem locations, avoid committing personal data, and rely on operating-system access controls.

Risk: Identity matches, relevance scores, and browser observations may be incomplete or wrong.

Mitigation: Review supporting and conflicting evidence before outreach, live-verify profile state, and preserve uncertain outcomes for reconciliation instead of retrying blindly.

## Reference(s):

- [Reconnect Skill Page](https://clawhub.ai/antreasantoniou/skills/reconnect)
- [Release Notes](docs/release-notes.md)
- [Discovery and Identity Resolution](references/discovery.md)
- [Authorized LinkedIn Work](references/linkedin.md)
- [Start from a Networking Goal](references/network-plan.md)
- [Private Tracking and Commands](references/tracking.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local, unencrypted project ledgers when the user chooses to run the optional helper.]

## Skill Version(s):

0.1.0-rc.2 (source: VERSION, release notes, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
