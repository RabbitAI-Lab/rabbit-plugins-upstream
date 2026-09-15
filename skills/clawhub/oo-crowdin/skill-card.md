## Description:

Crowdin helps agents read, create, and update Crowdin data through the OOMOL Crowdin connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Crowdin project structure and manage branches, directories, and source-file uploads through an OOMOL-connected Crowdin account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer execution for the oo CLI.

Mitigation: Prefer safer manual installation where possible and verify the installer source before running it.

Risk: Inline shell JSON payloads can be unsafe when values include user-controlled or Crowdin-provided text.

Mitigation: Pass payloads via a JSON file and fetch the live action schema before constructing command data.

Risk: Write actions can create Crowdin branches, directories, or uploaded source files.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Crowdin skill](https://clawhub.ai/oomol/skills/oo-crowdin)
- [Crowdin homepage](https://crowdin.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Crowdin action schemas before payload construction and returns connector responses as JSON when actions run.]

## Skill Version(s):

1.0.3 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
