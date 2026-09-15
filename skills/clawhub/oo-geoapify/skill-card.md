## Description:

Geoapify lets agents use an OOMOL-connected Geoapify account for address autocomplete, geocoding, routing, and route matrix workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Geoapify through their OOMOL-connected account for address lookup, geocoding, routing, and route matrix tasks without handling raw API keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified internet installer commands that can execute local code.

Mitigation: Review installer commands before use, prefer a verified package or pinned release, and run them only when OOMOL's installer delivery path is trusted.

Risk: Actions marked write can change Geoapify state through an authenticated OOMOL-connected account.

Mitigation: Fetch the live action schema first and confirm the exact payload and effect with the user before running write actions.

## Reference(s):

- [ClawHub Geoapify skill page](https://clawhub.ai/oomol/skills/oo-geoapify)
- [Geoapify homepage](https://www.geoapify.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
