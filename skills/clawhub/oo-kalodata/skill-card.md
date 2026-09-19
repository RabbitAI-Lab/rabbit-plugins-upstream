## Description:

Kalodata helps agents search and read Kalodata TikTok analytics through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Kalodata TikTok ecommerce analytics through an OOMOL-connected account, including category, creator, livestream, product, shop, and video lookups and ranked lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote shell installer commands for the oo CLI.

Mitigation: Review official installation instructions, verify the installer source where possible, and require user approval before any setup or login step.

Risk: The skill depends on an OOMOL-connected Kalodata account and server-side credentials.

Mitigation: Use only accounts and connections the user has authorized, and avoid exposing raw credentials in prompts, logs, or generated files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-kalodata)
- [Kalodata Homepage](https://www.kalodata.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live Kalodata action schemas before running connector requests.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
