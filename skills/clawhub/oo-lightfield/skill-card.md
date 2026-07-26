## Description: <br>
Lightfield lets agents search and read Lightfield accounts, contacts, opportunities, custom object records, and API key metadata through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when an agent needs read-only access to Lightfield CRM-style data through the OOMOL CLI. It supports listing and retrieving Lightfield accounts, contacts, opportunities, custom object records, object definitions, and connected API key metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The broad trigger wording can cause an agent to use connected Lightfield account access for casual questions that do not require live data. <br>
Mitigation: Use the skill only when the user asks to search, list, validate, or read Lightfield data from the connected account. <br>
Risk: Connector results can expose business records such as accounts, contacts, opportunities, and custom object records. <br>
Mitigation: Treat returned data as connected-account data and avoid unnecessary retrieval or disclosure beyond the user's Lightfield task. <br>
Risk: Action payloads may be incorrect if an agent relies on stale assumptions about connector inputs. <br>
Mitigation: Fetch the live action schema with oo connector schema before constructing each oo connector run payload. <br>


## Reference(s): <br>
- [Lightfield homepage](https://lightfield.app) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lightfield) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before action execution; connector responses are JSON objects containing data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
