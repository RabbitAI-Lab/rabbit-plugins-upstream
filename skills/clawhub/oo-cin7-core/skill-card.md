## Description:

Cin7 Core helps agents use the OOMOL-connected oo CLI to inspect Cin7 Core action schemas and retrieve account, customer, and product data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and business operators use this skill to query Cin7 Core through an authenticated OOMOL connector. It is focused on reading company settings, customers, and products after inspecting the live connector schema for each action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance includes remote installer commands that could run unverified installation scripts.

Mitigation: Install the oo CLI through a verified, version-pinned method before using the skill, and avoid executing remote installer commands as written.

Risk: Future connector actions tagged as write or destructive could modify Cin7 Core data.

Mitigation: Confirm the exact payload, target records, and expected effect with the user before running any write action, and require explicit approval for destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-cin7-core)
- [Cin7 Core Homepage](https://www.cin7.com/solutions/core/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Credentials are handled through the OOMOL connector; the skill tells agents to inspect live action schemas before constructing payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
