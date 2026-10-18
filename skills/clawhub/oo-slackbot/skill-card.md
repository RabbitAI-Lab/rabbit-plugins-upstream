## Description:

Uses an OOMOL-connected account to read and manage Slack conversations, messages, reactions, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Slack users and teams use this skill to retrieve workspace information and manage messages, reactions, and files through a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer scripts that execute code locally.

Mitigation: Review the OOMOL CLI source and installer before use; prefer a pinned or verified installation method.

Risk: The connected account can access workspace data and perform state-changing or destructive Slack actions.

Mitigation: Check connection scopes and obtain explicit confirmation of targets and payloads before posts, uploads, updates, deletes, or reactions.

## Reference(s):

- [Slack Bot on ClawHub](https://clawhub.ai/oomol/skills/oo-slackbot)
- [OOMOL CLI source](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Text or Markdown summaries of Slack actions and structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain Slack messages, user details, file metadata, or action status.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
