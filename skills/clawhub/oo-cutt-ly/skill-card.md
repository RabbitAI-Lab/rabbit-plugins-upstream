## Description:

Cuttly lets an agent operate Cuttly through an OOMOL-connected account to inspect action schemas, shorten URLs, and retrieve short-link analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Cuttly short links from an agent session through the OOMOL-connected oo CLI. It supports schema inspection, URL shortening, and click analytics retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes oo CLI installation commands that fetch and execute remote installer scripts.

Mitigation: Use a verified official source for oo CLI installation and avoid automatic pipe-to-shell execution where possible.

Risk: The shorten_url action changes Cuttly account state by creating a new short URL.

Mitigation: Confirm the destination URL, JSON payload, and intended account effect with the user before running the action.

Risk: Cuttly action data passes through OOMOL's connector service.

Mitigation: Review whether the destination URL, analytics, and account context are appropriate to send through the connector before execution.

## Reference(s):

- [Cuttly homepage](https://cutt.ly)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector response summaries containing Cuttly data and OOMOL execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
