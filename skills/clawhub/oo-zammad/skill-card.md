## Description:

Zammad (zammad.com). Use this skill for ANY Zammad request: reading, creating, and updating data through the OOMOL oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Support, operations, and engineering teams use this skill to let an agent retrieve Zammad account, ticket, article, and user information, then create ticket content or update ticket fields after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticket creation, article creation, and ticket updates can change support data visible to an organization or its customers.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running any write action.

Risk: The skill acts through the user's connected Zammad account.

Mitigation: Install and use it only when the user trusts OOMOL and intends the agent to operate with that connected account.

## Reference(s):

- [Zammad homepage](https://zammad.com/en)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zammad)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
