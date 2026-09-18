## Description:

AddressZen helps agents search partial address queries, check AddressZen key availability, and retrieve USA-formatted address records through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to operate AddressZen through an OOMOL-connected account for address autocomplete, key availability checks, and USA address retrieval without handling raw API credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands executed directly in a shell.

Mitigation: Install the OOMOL CLI only from a trusted distribution path, verify signatures or checksums where available, and avoid running pipe-to-shell installers from an elevated shell.

Risk: AddressZen actions depend on an authenticated OOMOL account and connected AddressZen credentials.

Mitigation: Use setup and reconnection steps only after an auth or connection failure, and avoid exposing raw credentials in prompts or command payloads.

## Reference(s):

- [AddressZen homepage](https://addresszen.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [AddressZen ClawHub skill page](https://clawhub.ai/oomol/skills/oo-addresszen)
- [OOMOL ClawHub publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON responses from AddressZen connector actions when commands are executed.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
