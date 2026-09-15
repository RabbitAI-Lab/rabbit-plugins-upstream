## Description:

Use this skill to read, create, and update Tremendous data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Tremendous reward workflows from an agent, including inspecting live connector schemas, listing or retrieving Tremendous entities, creating orders, and generating reward links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path recommends remote installer commands, including pipe-to-shell execution.

Mitigation: Install the oo CLI only after independently verifying the installer source or using a reviewed installation method.

Risk: The create_order action can spend or allocate Tremendous rewards.

Mitigation: Confirm the exact payload, recipient, amount, funding source, and expected effect with the user before running the action.

Risk: The skill depends on OOMOL account connection and oo CLI behavior for credentialed Tremendous operations.

Mitigation: Confirm trust in OOMOL and the oo CLI before installation, and use an appropriately scoped connected Tremendous account.

## Reference(s):

- [Tremendous homepage](https://www.tremendous.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tremendous)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before requests and explicit confirmation before state-changing actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
