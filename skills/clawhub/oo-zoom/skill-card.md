## Description:

Zoom (zoom.com). Use this skill for ANY Zoom request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect Zoom connector schemas, retrieve Zoom user and meeting information, and create or update Zoom meetings through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary says the setup instructions ask users or agents to run unverified remote installer scripts directly.

Mitigation: Prefer a verified or signed installer path, inspect the installer first, and avoid elevated privileges unless clearly required.

Risk: The skill can create or update Zoom meetings through the connected account.

Mitigation: Confirm the exact meeting-create or meeting-update payload and expected effect with the user before allowing write actions.

Risk: Zoom requests pass through the OOMOL connector.

Mitigation: Install only if the user trusts OOMOL and is comfortable using the OOMOL-connected Zoom account for the requested actions.

## Reference(s):

- [ClawHub Zoom skill page](https://clawhub.ai/oomol/skills/oo-zoom)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Zoom homepage](https://www.zoom.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Zoom connector action schemas, JSON request payloads, and confirmation prompts for write operations.]

## Skill Version(s):

1.0.4 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
