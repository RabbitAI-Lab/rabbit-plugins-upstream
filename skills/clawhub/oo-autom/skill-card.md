## Description: <br>
Autom (autom.dev). Use this skill for ANY Autom request — searching and reading data. Whenever a task involves Autom, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to query Autom through an OOMOL-connected account, including supported Google countries, languages, locations, and account usage metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Autom usage checks can reveal account, quota, rate-limit, and API-key metadata. <br>
Mitigation: Run the skill only for users who intend agents to query Autom through their OOMOL-connected account, and avoid sharing returned account metadata outside the task context. <br>
Risk: First-time setup may require trusting the OOMOL CLI installation and login flow. <br>
Mitigation: Use the documented OOMOL CLI setup only when authentication or connection errors require it, and do not proactively run login or connection commands. <br>


## Reference(s): <br>
- [Autom homepage](https://www.autom.dev) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-autom) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses OOMOL CLI responses that may include JSON data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
