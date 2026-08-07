## Description:

Draft and publish X posts on a weighted pillar schedule, with drafts always routed to the user for approval before posting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[soos3d](https://clawhub.ai/user/soos3d)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to draft, review, and publish approved posts for their own X account, including repo demos, technical insights, self-replies with links, and optional media. It can also draft reply options for user-supplied post links and file user-approved photos into a local posting library.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish through the user's X API token or logged-in browser session.

Mitigation: Keep the Telegram approval target configured correctly, leave it empty for draft-only mode, and review each approval package before sending the ship command.

Risk: The skill stores local posting history, drafts, metrics, media, and photo-library state.

Mitigation: Review the local postflight-state directory as part of deployment and keep only media and history that the account owner is comfortable retaining.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/soos3d/skills/postflight)
- [Publisher profile](https://clawhub.ai/user/soos3d)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown messages, local state files, shell command guidance, and approved X post text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user approval before publishing; browser fallback supports single text posts only.]

## Skill Version(s):

1.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
