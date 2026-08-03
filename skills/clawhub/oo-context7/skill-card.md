## Description: <br>
Context7 (context7.com). Use this skill for Context7 documentation search and retrieval through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical users use this skill to search Context7 libraries and retrieve documentation context or code snippets from an OOMOL-connected Context7 account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User prompts and documentation queries may be sent through the OOMOL/Context7 connector. <br>
Mitigation: Avoid sensitive private queries unless the user is comfortable sending that context through the connected external service. <br>
Risk: First-time setup or recovery commands can initiate authentication, connection, or billing workflows. <br>
Mitigation: Run setup steps only after a matching command failure and review the oo CLI setup before first use. <br>
Risk: Connector payloads can become incorrect if Context7 action contracts change. <br>
Mitigation: Inspect the live connector schema before each action and build payloads from the returned contract. <br>


## Reference(s): <br>
- [Context7 homepage](https://context7.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-context7) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and retrieved documentation context] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Context7 search results, documentation excerpts, code snippets, and setup or recovery guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
