## Description:

Audio search tool: searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search for royalty-free background music by short English style keywords and retrieve track URLs and metadata for selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and task parameters are sent to dLazy's hosted service.

Mitigation: Use the skill only when the user is comfortable sending those queries to dLazy.

Risk: The skill stores a dLazy API key locally when configured with login or auth commands.

Mitigation: Use a revocable API key, rotate or revoke it from the dLazy dashboard when needed, and prefer per-invocation environment variables when persistent local configuration is not desired.

Risk: Using --save writes returned assets to a local path selected by the caller.

Mitigation: Save only to intentional paths and review the destination before running download commands.

Risk: The artifact includes generic CLI documentation that can be confusing for this audio search workflow.

Mitigation: Prefer the search_audio command help and the --query option shown in the artifact when invoking the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [JSON results with track URLs and metadata, plus Markdown guidance for setup and errors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search queries should use 2-3 short English style keywords; each hit's track URL is returned in the url field.]

## Skill Version(s):

1.3.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
