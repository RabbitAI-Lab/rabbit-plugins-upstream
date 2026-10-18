## Description:

Uses an OOMOL-connected account to list API Route models and request non-streaming chat completions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect available API Route models and request chat completions through their connected OOMOL account without handling raw API keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chat completion requests send prompt data externally and incur charges.

Mitigation: Get explicit approval for the prompt and model before making a billed request, and avoid sending sensitive data without authorization.

Risk: The setup instructions include one-line remote installer commands.

Mitigation: Install the oo CLI through a verified method rather than executing a piped installer without review.

## Reference(s):

- [API Route skill release](https://clawhub.ai/oomol/skills/oo-api-route)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [API Route](https://www.api-route.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Text or Markdown guidance with shell commands and JSON action responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chat completions are non-streaming; model listings return available model IDs.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
