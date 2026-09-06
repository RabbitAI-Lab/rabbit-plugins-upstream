## Description:

Zep enables agents to read, create, update, and delete Zep users, threads, messages, and context through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Zep project data, users, conversation threads, messages, and thread context through the oo CLI with OOMOL-managed credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change Zep state, including users, threads, messages, metadata, and ontology settings.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

Risk: Destructive actions can delete Zep users, threads, memory, and associated graph artifacts.

Mitigation: Require explicit approval for the target resource before running delete_user or delete_thread.

Risk: The skill operates through the user's OOMOL-connected Zep account.

Mitigation: Install and use it only when the agent is expected to manage Zep data for that connected account.

## Reference(s):

- [Zep homepage](https://www.getzep.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zep)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector responses containing Zep data and execution metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
