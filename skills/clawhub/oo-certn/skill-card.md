## Description: <br>
Certn (certn.co). Use this skill for Certn requests that search and read data through the OOMOL Certn connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve and list Certn background-check cases, events, groups, packages, questionnaires, tags, and Client Portal users through an OOMOL-connected Certn account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Certn background-check data can contain sensitive personal information. <br>
Mitigation: Use only the intended OOMOL-connected Certn account, review case and user identifiers before execution, and avoid sharing returned data beyond the authorized task. <br>
Risk: First-time setup or connection steps can link the agent environment to a Certn account. <br>
Mitigation: Run authentication or account-connection steps only after an auth or connection failure and only when the user intends to connect that account. <br>


## Reference(s): <br>
- [ClawHub Certn skill page](https://clawhub.ai/oomol/skills/oo-certn) <br>
- [Certn homepage](https://certn.co) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects returned by the oo CLI.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
