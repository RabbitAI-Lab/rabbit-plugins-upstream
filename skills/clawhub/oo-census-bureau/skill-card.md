## Description: <br>
Enables an agent to search and read Census Bureau data through OOMOL's `census_bureau` connector and the `oo` CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to discover Census Data API datasets, inspect variables and variable groups, and query datasets through an OOMOL-connected Census Bureau account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires the OOMOL oo CLI, OOMOL sign-in, and a connected Census Bureau API key. <br>
Mitigation: Use it only in environments where those dependencies and credentials are approved, and rely on OOMOL's server-side credential handling rather than exposing raw tokens. <br>
Risk: Census Bureau connector requests may consume OOMOL billing credits or fail when credits are unavailable. <br>
Mitigation: Treat HTTP 402 or OOMOL_INSUFFICIENT_CREDIT responses as billing stops and resolve billing before retrying. <br>
Risk: Incorrect action payloads can produce failed or misleading Census dataset queries. <br>
Mitigation: Fetch the live connector schema for the selected action before building payloads and keep normal usage to the disclosed read-oriented actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-census-bureau) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Census Bureau homepage](https://www.census.gov) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
