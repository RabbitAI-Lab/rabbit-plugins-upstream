## Description:

PhantomBuster helps agents inspect and operate PhantomBuster agents, containers, and organization data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read PhantomBuster organization, agent, and container information, and to launch or stop PhantomBuster agents when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Initial setup can execute a remote oo CLI installer before use.

Mitigation: Install the oo CLI from a verified source and avoid unattended pipe-to-shell setup.

Risk: The skill can launch or stop PhantomBuster agents, which may change account state.

Mitigation: Review the live action schema, confirm the exact payload and target, and require explicit approval before write or stop actions.

Risk: Use relies on OOMOL as the broker for the connected PhantomBuster account.

Mitigation: Install only when that trust model is acceptable and review the connected PhantomBuster account state and scopes before use.

## Reference(s):

- [ClawHub PhantomBuster Skill Page](https://clawhub.ai/oomol/skills/oo-phantombuster)
- [PhantomBuster Homepage](https://phantombuster.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing PhantomBuster connector payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
