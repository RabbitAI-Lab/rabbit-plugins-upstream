## Description: <br>
Gorgias (gorgias.com). Use this skill for Gorgias searching and read-only data retrieval through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect Gorgias account, ticket, customer, tag, and user data through OOMOL's Gorgias connector. The skill is intended for read/search workflows and directs agents to inspect live connector schemas before running actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retrieve sensitive Gorgias ticket, customer, account, tag, and user data from a connected account. <br>
Mitigation: Treat lookup results as sensitive, confirm ambiguous requests before running them, and install only when the user intends to allow read access through OOMOL. <br>
Risk: Setup commands and authentication flows can change the user's local CLI state or connect an external account. <br>
Mitigation: Run the CLI installer, authentication flow, or connection URL only when setup is explicitly chosen or when a matching command failure requires it. <br>


## Reference(s): <br>
- [ClawHub Gorgias Skill](https://clawhub.ai/oomol/skills/oo-gorgias) <br>
- [Gorgias Homepage](https://www.gorgias.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions run successfully.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
