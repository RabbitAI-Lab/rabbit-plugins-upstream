## Description:

CallPage (callpage.io). Use this skill for ANY CallPage request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate CallPage through an OOMOL-connected account, including reading calls, users, and widgets and creating widget callback requests after confirming the payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer snippets can run remote code on the user's machine.

Mitigation: Do not allow an agent to run installer snippets automatically; install the oo CLI only from a trusted, verified source.

Risk: CallPage write actions can change account state.

Mitigation: Confirm the exact payload and intended effect with the user before running any write action.

## Reference(s):

- [CallPage Skill Page](https://clawhub.ai/oomol/skills/oo-callpage)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [CallPage homepage](https://www.callpage.io)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before building action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
