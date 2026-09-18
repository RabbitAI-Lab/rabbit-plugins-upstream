## Description:

Rollbar (rollbar.com). Use this skill for ANY Rollbar request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support engineers use this skill to operate Rollbar through an OOMOL-connected account, including reading projects, items, occurrences, deploys, environments, and item occurrence history. It can also guide Rollbar write actions when the user confirms the payload and intended effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes pipe-to-shell installer commands that can execute downloaded code without verification.

Mitigation: Prefer a verified or package-manager installation method, and only run installer commands after trusting the OOMOL installer path.

Risk: Rollbar write or destructive actions can modify or remove service data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before allowing write or destructive actions.

## Reference(s):

- [ClawHub Rollbar Skill](https://clawhub.ai/oomol/skills/oo-rollbar)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Rollbar Homepage](https://rollbar.com)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON when actions are run with the documented --json flag.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
