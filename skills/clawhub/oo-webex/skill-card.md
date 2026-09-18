## Description:

Webex lets an agent operate Webex through the OOMOL oo CLI to read, create, update, and delete meetings, rooms, teams, memberships, messages, people, recordings, transcripts, and summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to manage Webex collaboration workflows from an agent, including meetings, rooms, teams, memberships, messages, participants, recordings, transcripts, and summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends executing remote installer scripts directly in the shell.

Mitigation: Review the installer source and trust path before execution, or use a safer verified installation method for the oo CLI.

Risk: Write actions can create or modify Webex meetings, memberships, messages, rooms, teams, and team memberships.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write.

Risk: Destructive actions can delete Webex meetings, memberships, messages, rooms, teams, and team memberships.

Mitigation: Require explicit approval for the specific target before running any action tagged as destructive.

## Reference(s):

- [Webex homepage](https://www.webex.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands, JSON payload guidance, confirmation prompts for write or destructive actions, and setup guidance after authentication or connection failures.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
