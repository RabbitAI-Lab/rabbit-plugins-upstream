## Description:

Orimon enables an agent to send text messages to an Orimon chatbot through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Orimon from an agent session, inspect the live connector schema, send chatbot messages, and handle account connection setup only when commands fail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes an unpinned remote installer executed through the shell.

Mitigation: Review the skill before installation; prefer installing the oo CLI from reviewed documentation or a pinned, verified package, and connect only the intended Orimon account.

## Reference(s):

- [Orimon homepage](https://orimon.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-orimon)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Orimon connector JSON responses that include data and an execution id.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
