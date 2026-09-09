## Description:

Searches Pixabay Music through dLazy and returns royalty-free track URLs and metadata for selecting background music.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search for royalty-free background music with short English style keywords and receive track URLs and metadata for selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the dLazy CLI globally persists a third-party package and binary on the user's system.

Mitigation: Review the dLazy CLI source or npm package before use, and prefer the pinned npx invocation when a global install is not needed.

Risk: Authentication stores a dLazy API key in the user's local CLI configuration or accepts it through an environment variable.

Mitigation: Use scoped organization keys, protect the local config, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: Passing local files to dLazy media fields can upload those files to dLazy-hosted storage.

Mitigation: Only pass local file paths when upload is intended, and avoid including sensitive files in skill invocations.

Risk: The artifact includes some generic CLI examples that may not match the search_audio command's documented query flag.

Mitigation: Use `dlazy search_audio -h` and the documented `--query` form before invoking the command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; searches work best with 2-3 short English style keywords.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
