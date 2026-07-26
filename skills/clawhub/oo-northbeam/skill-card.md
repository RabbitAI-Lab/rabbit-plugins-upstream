## Description: <br>
Northbeam (northbeam.io) lets an agent search and read Northbeam data through an OOMOL-connected account instead of calling the Northbeam API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query Northbeam account data through the OOMOL oo CLI, including attribution models, metrics, breakdowns, and paginated spend records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose Northbeam spend and attribution data, which may be sensitive business information. <br>
Mitigation: Install it only for agents that should query the connected Northbeam account, and restrict access to users allowed to view that data. <br>
Risk: The OOMOL and Northbeam connection scopes determine what account data the agent can access. <br>
Mitigation: Review the OOMOL and Northbeam access scopes before installation and re-check them when credentials are renewed or reconnected. <br>
Risk: Future connector actions tagged as write or destructive could change or remove data if run without review. <br>
Mitigation: Inspect the live connector schema before building payloads and require explicit user approval for any write or destructive action. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-northbeam) <br>
- [Northbeam Homepage](https://www.northbeam.io) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text] <br>
**Output Format:** [Markdown guidance with shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before action payloads; returned spend and attribution data should be treated as sensitive business information.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
