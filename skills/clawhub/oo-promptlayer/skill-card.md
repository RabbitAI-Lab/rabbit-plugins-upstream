## Description:

Helps agents use an OOMOL-connected PromptLayer account to search and read prompt templates, logged requests, Tables, sheets, and rows through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect PromptLayer prompt assets and request logs from an authenticated workspace through OOMOL's connector flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to execute an unpinned remote installer script for the oo CLI.

Mitigation: Review the setup section before installing, use a trusted and verifiable installer flow, and do not allow an agent to run the remote installer automatically unless the local code-execution risk is accepted.

## Reference(s):

- [PromptLayer homepage](https://promptlayer.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-promptlayer)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON responses returned by oo connector actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
