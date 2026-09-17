## Description:

Ecologi (ecologi.com). Use this skill for ANY Ecologi request: searching, reading impact data, and running Ecologi account actions through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate an OOMOL-connected Ecologi account, retrieve carbon, habitat, tree, and total impact summaries, and prepare confirmed purchase actions for Ecologi projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Purchase actions can spend money or change Ecologi account state.

Mitigation: Confirm the exact action, payload, quantity, unit, live or test mode, and expected cost with the user before running any purchase command.

Risk: Remote installer one-liners can execute unreviewed code.

Mitigation: Use the installer only after independently verifying and trusting the OOMOL CLI distribution path.

Risk: Live connector schemas may change over time.

Mitigation: Inspect the live action schema before constructing each payload and match the command input to that schema.

## Reference(s):

- [ClawHub Ecologi skill page](https://clawhub.ai/oomol/skills/oo-ecologi)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Ecologi homepage](https://ecologi.com)
- [OOMOL Ecologi connection](https://console.oomol.com/app-connections?provider=ecologi)
- [Ecologi icon](https://static.oomol.com/logo/third-party/ecologi.png)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI schema-inspection commands, connector run commands, account impact summaries, and purchase-confirmation prompts.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
