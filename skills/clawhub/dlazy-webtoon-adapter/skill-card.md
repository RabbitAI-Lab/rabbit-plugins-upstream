## Description:

Adapts web-novel material into Chinese webtoon production outputs, including genre intake, plot breakdowns, episode tagging, per-episode scripts, and optional dLazy CLI generation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, and content teams use this skill to turn web-novel chapters or revision notes into structured Chinese webtoon adaptation material. The workflow supports plot breakdown, episode tagging, script drafting, consistency checks, and guided generation steps through dLazy services when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, novel material, and selected media files may be sent to dLazy hosted services.

Mitigation: Do not submit sensitive, confidential, or rights-restricted material unless that upload is intended and authorized.

Risk: API keys may be stored in the local dLazy CLI configuration.

Mitigation: Prefer per-run DLAZY_API_KEY environment variables where practical, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Using the skill may require installing and running a third-party npm CLI.

Mitigation: Review the npm package and exact pinned version before installation, and run generation commands only after confirming the intended inputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown conversation text with optional inline shell commands and generated media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and dLazy API credentials when using hosted generation commands.]

## Skill Version(s):

1.3.15 (source: server release evidence; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
