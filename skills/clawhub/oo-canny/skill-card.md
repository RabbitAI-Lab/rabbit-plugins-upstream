## Description:

Canny (canny.io). Use this skill for ANY Canny request: reading, creating, and updating data through the OOMOL Canny connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Canny connector schemas and run Canny actions for boards, posts, comments, and users through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can direct users to execute remote installer scripts.

Mitigation: Independently trust and verify the OOMOL CLI installer through an official, pinned, or signed distribution path before running installer commands.

Risk: Write actions can create or update Canny data.

Mitigation: Confirm the exact payload and intended effect with the user before running any action tagged as write or destructive.

## Reference(s):

- [Canny homepage](https://canny.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-canny)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Canny connector output wrapped as JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
