## Description:

Audio search tool that searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to find royalty-free background music by issuing short English style queries and reviewing returned track metadata and URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and account credentials are sent to the dLazy hosted service.

Mitigation: Install and use the skill only if that data sharing is acceptable, and authenticate through the documented dLazy CLI flow.

Risk: The CLI can write files locally when invoked with save options.

Mitigation: Use save options only when a local download is intended and review the target path before execution.

Risk: Documentation drift can cause incorrect invocation details.

Mitigation: Prefer the documented search query option and check `dlazy search_audio -h` before running commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results include audio track URLs and metadata; the CLI can optionally save returned assets to a local path when requested.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
