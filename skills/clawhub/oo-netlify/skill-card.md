## Description:

Operate Netlify through an OOMOL-connected account to read, create, update, and delete Netlify resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to manage Netlify accounts, sites, deploys, builds, forms, and submissions through the oo CLI. It supports both read actions and state-changing deployment or deletion workflows when the user confirms the exact target and payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer commands that should not be run blindly.

Mitigation: Prefer a verified installer, pinned release, checksum, or manual inspection before installing the oo CLI.

Risk: Write and destructive Netlify actions can change deployments or delete submissions.

Mitigation: Confirm exact targets, payloads, and expected effects with the user before running write or destructive actions.

Risk: The skill depends on OOMOL brokering access to the user's Netlify account.

Mitigation: Use the skill only when the user trusts OOMOL for the connected Netlify credential.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-netlify)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Netlify homepage](https://www.netlify.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector actions that return JSON data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
