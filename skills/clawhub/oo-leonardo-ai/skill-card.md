## Description:

Leonardo.Ai helps agents use an OOMOL-connected Leonardo.Ai account to inspect schemas, create generation jobs, and retrieve model or generation information through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Leonardo.Ai through an OOMOL-connected account, including creating generation jobs, checking generation status, and listing available production API models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Review installation before use, prefer a verified and versioned oo CLI installation path with integrity checks, and do not allow an agent to run remote installer commands automatically.

Risk: The `create_generation` action changes Leonardo.Ai state and may consume account credits.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions, and check billing state before retrying after credit-related errors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-leonardo-ai)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Leonardo.Ai homepage](https://leonardo.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; generated job responses are returned as JSON by the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
