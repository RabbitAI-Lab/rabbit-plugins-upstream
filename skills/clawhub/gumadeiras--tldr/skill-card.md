## Description:

Simplified man pages from tldr-pages. Use this to quickly understand CLI tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gumadeiras](https://clawhub.ai/user/gumadeiras)

### License/Terms of Use:


## Use Case:

Developers, engineers, and CLI users use this skill to get concise command examples and short command-line documentation through the tldr CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: tldr pages are concise and may omit complete or authoritative command details.

Mitigation: Use tldr for quick examples, then fall back to man or --help when exact behavior, flags, or safety-sensitive details matter.

Risk: The skill depends on the local tldr executable being installed and available on PATH.

Mitigation: Verify the tldr binary is installed before enabling the skill for agents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gumadeiras/skills/tldr)
- [tldr-pages project](https://github.com/tldr-pages/tldr)

## Skill Output:

**Output Type(s):** [guidance, shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the local tldr executable; agents may fall back to man or --help when a tldr page is missing or insufficient.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
