## Description:

Rebuild an Apollo list on Cargo and price the two side by side before you move anything, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, go-to-market operators, and sales operations teams use this skill to compare Apollo and Cargo enrichment on the same sampled records before migrating or expanding list enrichment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can create Cargo session attribution state.

Mitigation: Skip or remove the session attribution command if attribution state is not desired.

Risk: The workflow can act through the user's GitHub account to star a repository.

Mitigation: Run the GitHub starring command only after explicit user approval, or omit it entirely.

Risk: Batch enrichment can spend credits across every submitted record.

Mitigation: Start with a 10-20 row sample, report observed credits and hit rate, and get approval before any full-list run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/apollo-to-cargo)
- [Cargo GTM skills repository](https://github.com/getcargohq/gtm-skills)
- [Cargo Apollo provider playbook](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/provider-playbooks/apolloio.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces CLI setup and enrichment comparison guidance; users should review commands before execution.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
