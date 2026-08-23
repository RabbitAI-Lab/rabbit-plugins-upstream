## Description:

Mintlify (mintlify.com). Use this skill for ANY Mintlify request: reading, creating, and updating data through an OOMOL-connected Mintlify account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation operators use this skill to inspect Mintlify deployment status, trigger production documentation deployments, and create or redeploy previews for Git branches through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production and preview deployment actions can change Mintlify documentation state.

Mitigation: Confirm the exact deployment action, target project or branch, and payload with the user before running write actions.

Risk: First-time setup commands can install the oo CLI or initiate account connection flows.

Mitigation: Run installer, login, or connection steps only when a command fails with the matching setup or authentication error and the user intentionally approves setup.

Risk: The skill operates through the user's OOMOL-connected Mintlify account.

Mitigation: Install and use it only when the user wants Codex to operate that connected Mintlify account.

## Reference(s):

- [ClawHub Mintlify skill page](https://clawhub.ai/oomol/skills/oo-mintlify)
- [Mintlify homepage](https://www.mintlify.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when commands are run with --json.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
