## Description:

Cuttly (cutt.ly). Use this skill for ANY Cuttly request - reading, creating, and updating data. Whenever a task involves Cuttly, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cuttly links through an OOMOL-connected account, including creating short URLs and retrieving click analytics while relying on server-side credential handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup instructions could execute arbitrary local code if run without review.

Mitigation: Use an official, version-pinned installer or manually review the download before installation; avoid running pipe-to-shell commands blindly.

Risk: The shorten_url action changes Cuttly account state by creating a new short URL.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cutt-ly)
- [Cuttly homepage](https://cutt.ly)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Cuttly action results as JSON data with execution metadata.]

## Skill Version(s):

1.0.4 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
