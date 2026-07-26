## Description: <br>
Document360 (document360.com). Use this skill for ANY Document360 request — searching and reading data. Whenever a task involves Document360, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, developers, and agents use this skill to search and read Document360 workspaces through an OOMOL-connected account. It supports workspace discovery, category retrieval, article listing, and workspace search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The broad Document360 trigger routes Document360 search and read tasks through the user's OOMOL-connected account. <br>
Mitigation: Install only when agents should access Document360 through that account, and review requested actions before execution. <br>
Risk: First-time setup may install the oo CLI or require OOMOL sign-in and a Document360 connection. <br>
Mitigation: Review setup steps before allowing them and run them only after an authentication, connection, or missing-CLI failure. <br>


## Reference(s): <br>
- [Document360 homepage](https://document360.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-document360) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
