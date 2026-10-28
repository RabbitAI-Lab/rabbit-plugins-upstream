## Description:

Analyzes a source video and returns a Seedance 2.0 replication bundle containing a first frame, audio, and video output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to analyze a source video and prepare a Seedance 2.0 replication bundle for a video generation workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media and prompts are uploaded to dLazy for processing.

Mitigation: Use only media and prompts you are comfortable sharing with the service.

Risk: Processing may consume paid credits.

Mitigation: Use --dry-run to preview the payload and cost estimate before calling the API.

Risk: The API key is stored locally in the CLI configuration.

Mitigation: Protect access to the local configuration and rotate or revoke the key if needed.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Media assets, Text guidance]

**Output Format:** [JSON result with generated media outputs and hosted asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier; generated asset URLs are hosted by dLazy.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
