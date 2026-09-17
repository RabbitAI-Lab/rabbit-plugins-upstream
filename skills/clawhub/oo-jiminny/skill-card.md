## Description:

Jiminny helps agents search and read Jiminny activity data through an OOMOL-connected account using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Jiminny activities, summaries, transcriptions, action items, scorecards, coaching feedback, comments, listens, questions, topic triggers, and organization users through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer one-liners for the oo CLI.

Mitigation: Review the installer source and delivery path before installing; prefer an independently verified or signed installation method when available.

Risk: Jiminny responses can include sensitive activity, transcript, coaching, scorecard, comment, and organization user data.

Mitigation: Use the skill only with an authorized OOMOL-connected Jiminny account and share returned data according to the organization's access and data-handling policies.

## Reference(s):

- [Jiminny homepage](https://jiminny.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Jiminny skill on ClawHub](https://clawhub.ai/oomol/skills/oo-jiminny)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Jiminny data returned by the oo CLI as JSON.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
