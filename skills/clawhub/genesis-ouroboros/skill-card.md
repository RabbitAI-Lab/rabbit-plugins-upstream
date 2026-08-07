## Description:

Genesis Ouroboros helps an agent clarify requirements, review existing solutions, and generate a constitution-centered scaffold for a new self-evolving agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckyz10](https://clawhub.ai/user/luckyz10)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to create a new agent scaffold with a single constitution, a Claude pointer file, and the initial skills requested by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic lesson persistence can save secrets, private context, or unwanted behavior changes into generated agent skills.

Mitigation: For sensitive projects, set distill_mode to confirm and review lesson or script changes before accepting them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luckyz10/skills/genesis-ouroboros)
- [Server-resolved GitHub source](https://github.com/LuckyZ10/genesis-ouroboros/tree/main/genesis-ouroboros)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown and file-content guidance for agent scaffold files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces only the requested scaffold essentials: AGENTS.md, CLAUDE.md, and one or two core skills.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
