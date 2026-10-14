## Description:

Helps agents use a connected Cheaper Inference account to create chat completions, create messages, and list available models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users with a connected Cheaper Inference account can request chat completions or messages and discover available models through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests executing a downloaded installer script directly.

Mitigation: Review the installation source and prefer a verified installer or official package manager before running any downloaded script.

Risk: Chat and message requests send prompt content to Cheaper Inference through OOMOL and may consume account credit.

Mitigation: Avoid sending sensitive content without authorization and confirm the expected credit usage before submitting requests.

## Reference(s):

- [Cheaper Inference skill on ClawHub](https://clawhub.ai/oomol/skills/oo-cheaperinference)
- [Cheaper Inference](https://cheaperinference.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Markdown guidance and JSON action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses and model listings depend on the connected account.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
