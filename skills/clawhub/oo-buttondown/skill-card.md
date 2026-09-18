## Description:

Buttondown (buttondown.com). Use this skill for ANY Buttondown request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Buttondown through an OOMOL-connected account, including subscriber, tag, newsletter, and account workflows. It supports read, write, and destructive Buttondown actions with schema inspection and user confirmation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can execute an unverified internet installer on the user's machine.

Mitigation: Install only after manually reviewing the official OOMOL installation instructions and installer contents; do not have an agent run the curl-to-bash or PowerShell iex installer automatically.

Risk: Write and destructive Buttondown actions can change or delete subscriber and tag data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running actions marked write or destructive.

## Reference(s):

- [Buttondown homepage](https://buttondown.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-buttondown)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Buttondown action results returned by the oo CLI as JSON.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
