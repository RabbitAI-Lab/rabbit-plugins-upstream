## Description:

Enables agents to inspect Close connector schemas and run read, create, and update actions for Close CRM through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate Close CRM records through an OOMOL-connected account, including listing and fetching leads, contacts, opportunities, and tasks. With user confirmation, the skill can also create or update those CRM objects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Review the oo CLI installation source before use and prefer a verified, pinned, or signed installer path.

Risk: Create and update actions can modify Close CRM records.

Mitigation: Confirm the exact payload and expected effect with the user before allowing any write action to run.

## Reference(s):

- [Close homepage](https://www.close.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-close)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces oo CLI connector commands and interprets JSON responses; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
