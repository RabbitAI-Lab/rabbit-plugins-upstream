## Description:

Guides agents and operators through storing encrypted scripts and running them through MGC Blackbox with explicit user authorization and no plaintext script exposure to the AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zkeviny](https://clawhub.ai/user/zkeviny)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure local MGC Blackbox workflows for encrypted script storage, blackbox execution, runtime parameter passing, credential access from scripts, and script sealing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill teaches opaque stored script execution, so agents may not be able to inspect script behavior before execution.

Mitigation: Approve each script only after independently verifying its source, contents, purpose, and network behavior.

Risk: Stored scripts may access local resources or MGC credentials.

Mitigation: Limit credential availability, run only trusted scripts, and require explicit user authorization before storing or executing any script.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zkeviny/skills/secure-script-runner)
- [MGC Blackbox Repository](https://github.com/zkeviny/MGC-Blackbox)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with Python, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user authorization before script storage or execution; the skill states that agents receive execution results rather than script plaintext or stdout.]

## Skill Version(s):

1.1.0 (source: server release metadata, SKILL.md frontmatter, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
