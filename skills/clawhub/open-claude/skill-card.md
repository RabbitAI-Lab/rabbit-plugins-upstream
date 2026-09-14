## Description:

Opens Brave browser to Claude AI (Anthropic). Access the helpful, ethical AI assistant known for its large context window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to open Claude in the Brave browser from natural-language trigger phrases when they want to start a Claude session quickly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad natural-language trigger phrases may open a Brave tab unintentionally.

Mitigation: Review and narrow trigger phrases before installation if accidental launches would disrupt the user workflow.

Risk: The Windows launch path uses shell=True.

Mitigation: Review or modify the launcher before Windows deployment to avoid shell=True where possible.

## Reference(s):

- [Claude](https://claude.ai)
- [Brave Browser](https://brave.com)
- [ClawHub Skill Page](https://clawhub.ai/ruchir17-cmd/skills/open-claude)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Browser launch action with a short terminal status message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Brave browser, internet access, and a Claude account.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
