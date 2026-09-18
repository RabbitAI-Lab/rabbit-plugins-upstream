## Description:

Lever helps agents use an OOMOL-connected Lever account to read opportunities, postings, and notes and create opportunity notes through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting and talent operations users can ask an agent to inspect Lever candidates, postings, opportunity notes, and related recruiting records through an authenticated OOMOL connection. The skill also supports creating opportunity notes after the agent confirms the intended payload and effect with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that can execute arbitrary code if the installer source is not trusted or verified.

Mitigation: Review the setup path before installation and prefer a pinned, signed, or package-manager installation method.

Risk: The create_opportunity_note action changes Lever data.

Mitigation: Confirm the exact payload and intended effect with the user before allowing the write action to run.

## Reference(s):

- [ClawHub Lever skill listing](https://clawhub.ai/oomol/skills/oo-lever)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Lever homepage](https://www.lever.co)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before running actions and to confirm state-changing Lever note creation before execution.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
