## Description:

Operate screenshot.fyi through the OOMOL-connected oo CLI to capture website screenshots and return generated URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate screenshot.fyi via OOMOL's connected oo CLI, inspect the live connector schema, run screenshot actions, and return generated screenshot URLs without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the oo CLI installation path first, prefer official package-manager or verified installer steps, inspect downloaded scripts before execution, and avoid running installer commands automatically or from an elevated shell.

Risk: Screenshot actions depend on an OOMOL account connection, valid screenshot.fyi credentials, and available billing credits.

Mitigation: Run setup or account-repair steps only after matching authentication, connection, credential, app readiness, or billing errors appear.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-screenshot-fyi)
- [screenshot.fyi Homepage](https://www.screenshot.fyi)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; connector responses return JSON containing screenshot URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live screenshot_fyi connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
