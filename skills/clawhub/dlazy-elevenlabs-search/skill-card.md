## Description:

Search the ElevenLabs voice library by keyword, source, and category, with playable previews for matched voices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creators use this skill to find ElevenLabs voices by descriptor, source, and category, then compare playable previews before text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the documented dLazy login and authentication commands do not match the advertised ElevenLabs voice search purpose; it did not establish how authentication works.

Mitigation: Review the CLI and verify its authentication and data handling before configuring a dLazy API key or making requests.

## Reference(s):

- [CLI project link in release metadata](https://github.com/dlazy-ai/cli)
- [CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [JSON, Audio preview links]

**Output Format:** [JSON voice search results with playable preview links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the search descriptor and voice source and category filters.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
