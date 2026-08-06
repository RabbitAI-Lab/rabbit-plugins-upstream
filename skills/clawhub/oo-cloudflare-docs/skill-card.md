## Description: <br>
Cloudflare Docs helps agents search and read Cloudflare documentation through the OOMOL cloudflare_docs connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to search Cloudflare documentation and retrieve the Pages to Workers migration guide through an OOMOL connector-backed workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill routes documentation lookups through the OOMOL oo CLI and may require an OOMOL login or provider connection. <br>
Mitigation: Confirm the user is comfortable using OOMOL for documentation access before setup, and only run setup commands when an auth or connection error requires them. <br>
Risk: Connector action schemas can change over time, which may make stale payload assumptions incorrect. <br>
Mitigation: Inspect the live connector schema with `oo connector schema` before constructing or running an action payload. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cloudflare-docs) <br>
- [Cloudflare Docs homepage](https://developers.cloudflare.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses may include JSON data and an execution ID under meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
