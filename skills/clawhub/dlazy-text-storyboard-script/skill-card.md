## Description:

Generates detailed short-video storyboard scripts from user-provided themes, structured copy, or outlines while preserving spoken copy word for word.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and production teams use this skill to turn themes, outlines, or structured video copy into shot-by-shot storyboard scripts for short-form video production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a suspicious verdict because the skill claims text-only behavior while also installing and using a cloud media CLI.

Mitigation: Review the skill scope before installation and install it only when dLazy cloud media generation is acceptable.

Risk: The security guidance notes npm/npx execution, dLazy authentication, local API key storage, and possible prompt or file upload to dLazy services.

Mitigation: Use least-privilege API keys, rotate or revoke keys when needed, and avoid providing confidential copy unless it may be sent to dLazy services and repeated in output.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown storyboard script with basic video parameters and per-shot sections.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves user-provided spoken copy word for word and defaults missing video parameters to 9:16 at 720p.]

## Skill Version(s):

1.2.15 (source: ClawHub release metadata; artifact frontmatter reports 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
