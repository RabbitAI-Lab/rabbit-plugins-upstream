## Description:

Sherpa helps agents retrieve personalized travel restrictions, document requirements, and visa requirement summaries through an OOMOL-connected Sherpa account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up trip-specific travel restrictions, document requirements, and visa requirement summaries for a traveler itinerary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the user's OOMOL-connected Sherpa account for travel requirement lookups.

Mitigation: Install and run it only when that account use is intended, and review the oo CLI setup and account connection steps before first-time setup.

Risk: Connector action schemas may differ from assumptions in a prompt or previous run.

Mitigation: Inspect the live Sherpa action schema before constructing each connector payload.

Risk: Future Sherpa connector actions may be labeled write or destructive.

Mitigation: Confirm the exact payload and expected effect with the user before running any write or destructive action.

## Reference(s):

- [Sherpa homepage](https://www.joinsherpa.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Markdown, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; connector responses may return JSON data or Markdown trip summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, an authenticated OOMOL account, and a connected Sherpa account.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
