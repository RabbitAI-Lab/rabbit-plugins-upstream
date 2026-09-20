## Description:

fal.ai sync-lipsync v3 generates a new video where a speaker's lip movement matches a supplied audio track, supporting dubbing, localization, and virtual presenter re-syncing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and localization teams use this skill to run dLazy's hosted sync-lipsync-3 workflow from an agent. It takes source video and audio inputs and returns hosted or saved generated media for dubbing, localization, and virtual-presenter workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided media paths may be uploaded to dLazy-hosted storage for generation.

Mitigation: Use only media appropriate for the dLazy service, review service terms, and avoid submitting sensitive content unless authorized.

Risk: Authentication may persist an API key in the local dLazy CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable or npx for per-invocation usage when persistent local credentials or global installs are not desired.

Risk: The artifact documentation has minor inconsistencies in sample output and examples.

Mitigation: Run dlazy sync-lipsync-3 -h and prefer the command's current help output when constructing invocations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown instructions with bash command examples and JSON result envelopes; generated media is returned as hosted URLs and can be saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; local video and audio paths may be uploaded to dLazy-hosted media storage for processing.]

## Skill Version(s):

1.3.18 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
