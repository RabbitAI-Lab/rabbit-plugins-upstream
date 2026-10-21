## Description:

Searches for stock video footage by keyword through the dLazy CLI and returns video URLs and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and agents use this skill to find stock video footage by keyword, filter results by category or duration, and review video URLs and metadata for sourcing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pixabay-search framing may suggest a direct Pixabay request, but searches are sent through dLazy services.

Mitigation: Review the returned footage's origin and usage terms, and decide whether using dLazy's hosted service is acceptable.

Risk: Queries and parameters go to dLazy, and local media paths passed to the CLI may upload those files.

Mitigation: Avoid sensitive search terms and pass local media paths only when an upload is intended.

Risk: Using the external CLI requires a dLazy API key that may be saved locally.

Mitigation: Review the CLI before installing, protect the local key, and rotate or revoke it if exposed.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with video URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the dLazy API; the CLI returns JSON.]

## Skill Version(s):

1.3.33 (source: server-resolved release; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
