## Description:

Produce a short, copy-paste-ready TL;DR summary of any CLI command from its man page or --help text, so a human or coding agent can learn the essential options without scrolling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and coding agents use this skill to get a compact reminder of a local CLI command's purpose, usage, common flags, and an example before invoking or reviewing that command.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper may execute the requested local command with --help when no man-page content is available.

Mitigation: Use it only with trusted command names in trusted PATH environments, and review the proposed command summary before acting on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/tldr-cmd)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Plain text summary with command, description, usage, flags, and example fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires bash, sed, and man; may fall back to local command --help output.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
