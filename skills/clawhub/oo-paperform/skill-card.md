## Description: <br>
Paperform lets agents search and read Paperform data through the OOMOL oo CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and users with OOMOL-connected Paperform accounts use this skill to list accessible forms and retrieve form data such as fields, submissions, partial submissions, products, and coupons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Paperform data through the user's OOMOL-connected account. <br>
Mitigation: Install and use it only when an agent is authorized to access that Paperform data. <br>
Risk: First-time setup may require running the OOMOL oo CLI installer if the CLI is missing. <br>
Mitigation: Review the OOMOL installer source before running the one-time setup command. <br>


## Reference(s): <br>
- [ClawHub Paperform skill](https://clawhub.ai/oomol/skills/oo-paperform) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Paperform homepage](https://paperform.co) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, text, json, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fetches live connector schemas before actions; Paperform actions described by the artifact are read-only get and list operations.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
