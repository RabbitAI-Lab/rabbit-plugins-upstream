## Description:

App Store Connect lets agents read, create, update, and delete App Store Connect data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release operators use this skill to manage App Store Connect apps, TestFlight, App Store metadata, Game Center, in-app purchases, subscriptions, account resources, and Xcode Cloud workflows from an agent session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change, publish, release, overwrite, or delete App Store Connect account data.

Mitigation: Require explicit user confirmation for every state-changing action, including untagged actions that send, publish, release, reorder, or redeliver content.

Risk: Blind pipe-to-shell installation of the oo CLI can execute unreviewed installer code.

Mitigation: Use an inspected, pinned, or otherwise verified oo CLI installation path before running connector commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-app-store-connect)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [App Store Connect](https://appstoreconnect.apple.com/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON request/response payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses include connector data and execution metadata; live action schemas should be inspected before building payloads.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
