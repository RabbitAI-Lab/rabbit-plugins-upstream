## Description:

Searches Pixabay Music for royalty-free background tracks using short English style keywords and returns track URLs with metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find royalty-free background music candidates by style, duration, and result count through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires running the dLazy npm CLI with the user's local permissions.

Mitigation: Prefer the pinned npx or local install path, review the package/source link before use, and avoid global installation when it is not needed.

Risk: dLazy API keys are credentials and may be stored in the local CLI config.

Mitigation: Use per-invocation environment variables when appropriate, restrict local config access, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Search inputs and any provided local media paths may be sent to dLazy endpoints.

Mitigation: Do not pass sensitive prompts or local file paths unless upload to the dLazy service is intended.

Risk: The security summary notes inconsistent command documentation around this narrow audio-search skill.

Mitigation: Check `dlazy search_audio -h`, prefer documented audio-search flags such as `--query`, and use `--dry-run` before live API calls when available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill returns dLazy CLI command guidance and JSON-shaped audio search results with track URLs and metadata.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
