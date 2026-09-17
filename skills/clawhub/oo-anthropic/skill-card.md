## Description:

Operates Anthropic through an OOMOL-connected account using the oo CLI to count message tokens, create non-streaming messages, and retrieve model information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route Anthropic work through an OOMOL-connected account instead of handling raw API tokens directly. It supports token counting, non-streaming message creation, model lookup, and model listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts, which the security evidence flags as suspicious when unverified.

Mitigation: Review the installer path before installation, prefer pinned, signed, or checksum-verified oo CLI releases, and avoid running remote installer commands from an elevated shell.

Risk: The create_message action is state-changing and may consume account resources or send unintended Anthropic requests.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and inspect the live action schema before constructing the request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-anthropic)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Anthropic homepage](https://www.anthropic.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before request construction and returns connector responses as JSON when actions are executed.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
