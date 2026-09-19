## Description:

GraphHopper helps agents inspect live action schemas and run routing, matrix, isochrone, geocoding, and profile-listing requests through an OOMOL-connected GraphHopper account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer GraphHopper-related requests by validating action inputs, running GraphHopper connector actions, and returning route, matrix, isochrone, geocoding, or profile results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell installers for the OOMOL CLI without built-in verification.

Mitigation: Use a trusted, reviewed, version-pinned installation path with checksum or signature verification, and do not let an agent run curl-to-bash or Invoke-Expression installers automatically.

## Reference(s):

- [GraphHopper homepage](https://www.graphhopper.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub GraphHopper skill page](https://clawhub.ai/oomol/skills/oo-graphhopper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before requests; command responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: evidence release version and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
