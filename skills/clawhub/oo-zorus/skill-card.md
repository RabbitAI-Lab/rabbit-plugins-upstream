## Description:

Zorus helps agents search and read Zorus unblock requests, customers, endpoints, groups, and policies through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support teams use this skill to answer Zorus account questions by searching active unblock requests, customers, endpoints, groups, and policies without handling raw credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes running a remote oo CLI installer script without embedded verification instructions.

Mitigation: Install the oo CLI only from official OOMOL documentation, verify any available checksum or signature, and approve setup before connector commands run against a Zorus account.

Risk: Connector calls can expose Zorus customer, endpoint, group, policy, and unblock-request data to the agent session.

Mitigation: Use the documented read-only search actions, inspect each live action schema before execution, and avoid sharing results beyond the user's requested scope.

## Reference(s):

- [Zorus homepage](https://www.zorustech.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Zorus skill page](https://clawhub.ai/oomol/skills/oo-zorus)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect the live connector schema before running read-only Zorus search actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
