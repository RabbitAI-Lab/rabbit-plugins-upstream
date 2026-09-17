## Description:

Wappalyzer helps agents run OOMOL-connected Wappalyzer actions for website technology lookup, subdomain discovery, credit balance checks, and email verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to ask an agent for Wappalyzer-backed website intelligence, subdomain discovery, account credit checks, and email verification through an already connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts executed directly in a shell without verification.

Mitigation: Review before installation; prefer a signed, pinned, or separately verified oo CLI release path and avoid running setup commands from an elevated shell.

Risk: Normal use depends on account connection and billing state outside the skill.

Mitigation: Run Wappalyzer actions only after the user has installed the CLI, signed in, connected Wappalyzer, and resolved any billing or credential errors.

## Reference(s):

- [Wappalyzer homepage](https://www.wappalyzer.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wappalyzer)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal operation relies on an installed, signed-in oo CLI and a connected Wappalyzer account; live action schemas should be inspected before constructing payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
