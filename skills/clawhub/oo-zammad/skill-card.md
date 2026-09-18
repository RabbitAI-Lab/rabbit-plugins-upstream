## Description:

Zammad helps an agent read, create, and update Zammad tickets and users through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, support teams, and developers use this skill to operate connected Zammad accounts through the oo CLI. It supports inspecting live action schemas, reading and searching tickets and users, creating and updating tickets, and adding ticket articles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute immediately.

Mitigation: Review the setup path before installing; prefer an official package manager, signed release, or manually downloaded and verified installer, and do not let an agent run the remote installer automatically.

Risk: Zammad write actions can create or update tickets and ticket articles.

Mitigation: Confirm the exact JSON payload and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zammad)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Zammad homepage](https://zammad.com/en)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON payload examples, and JSON command results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill asks the agent to inspect live connector schemas before constructing action payloads and to confirm state-changing Zammad writes before execution.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
