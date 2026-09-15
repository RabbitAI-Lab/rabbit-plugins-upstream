## Description:

Lacuna enables an agent to search and read Lacuna machine-learning research map data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and external users use this skill to search Lacuna's machine-learning research map and retrieve papers, research directions, authors, hypotheses, and related research context through connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags the fallback CLI setup because it asks users to run an unverified remote installer directly in a shell.

Mitigation: Install the oo CLI independently from a trusted source, prefer signed or checksummed packages, and do not let an agent run installation commands automatically.

Risk: Authentication gives the skill access through the signed-in OOMOL account.

Mitigation: Sign in only when you intentionally want this skill to use that account, and do not run authentication proactively.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lacuna)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Lacuna homepage](https://lacuna.tiptreesystems.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Lacuna icon](https://static.oomol.com/logo/third-party/lacuna.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.2 (source: server evidence release version and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
