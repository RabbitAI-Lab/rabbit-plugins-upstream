## Description:

Leonardo.Ai (leonardo.ai). Use this skill for ANY Leonardo.Ai request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Leonardo.Ai through an OOMOL-connected account, including creating generation jobs, checking generation status, and listing production API models and parameter schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that can execute arbitrary code.

Mitigation: Install the oo CLI through a trusted, pinned, and verifiable method before using the skill; do not allow an agent to run remote installer commands automatically.

Risk: Creating Leonardo.Ai generation jobs can consume account credits or change account state.

Mitigation: Confirm the exact generation payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-leonardo-ai)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Leonardo.Ai Homepage](https://leonardo.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces oo CLI commands and JSON action payload guidance; connector responses are JSON.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
