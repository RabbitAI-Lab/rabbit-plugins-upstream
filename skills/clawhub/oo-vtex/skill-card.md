## Description: <br>
VTEX (vtex.com). Use this skill for ANY VTEX request — searching and reading data. Whenever a task involves VTEX, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect VTEX connector schemas and run read-only VTEX catalog actions through an OOMOL-connected account, including product lookup, brand listing, category tree retrieval, product/SKU ID listing, and storefront product search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on the OOMOL oo CLI and a connected VTEX account; running setup or connection commands can change local authentication state or account connections. <br>
Mitigation: Only install the CLI, sign in, or connect VTEX after explicit user approval or when a command fails with the documented setup or authentication error. <br>
Risk: Future connector actions may include write or destructive operations even though the current disclosed action list is read-only. <br>
Mitigation: Inspect the live action schema before building payloads and get explicit approval before running any action tagged write or destructive. <br>


## Reference(s): <br>
- [VTEX homepage](https://vtex.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [VTEX connection setup](https://console.oomol.com/app-connections?provider=vtex) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector run responses are JSON objects with data and meta.executionId fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
