## Description:

Jiminny lets an agent search and read Jiminny activity data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Jiminny activities, summaries, transcriptions, action items, scorecards, coaching feedback, comments, listens, users, and topic trigger data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends remote installer commands that could run arbitrary code if the oo CLI is missing.

Mitigation: Prefer a verified oo CLI installation path with pinned versions, checksums, signatures, or manual inspection before running installer commands.

Risk: Using the skill can query Jiminny business call transcripts, scorecards, comments, users, and related activity data through OOMOL.

Mitigation: Use connected accounts with appropriate authorization and review requested Jiminny data access before running connector actions.

## Reference(s):

- [Jiminny homepage](https://jiminny.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Jiminny skill](https://clawhub.ai/oomol/skills/oo-jiminny)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or connector responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data object and execution metadata when actions are run with JSON output.]

## Skill Version(s):

1.0.3 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
