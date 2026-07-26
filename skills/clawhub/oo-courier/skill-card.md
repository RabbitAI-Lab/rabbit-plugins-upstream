## Description: <br>
Courier (courier.com). Use this skill for Courier requests that read, create, update, delete, and send data through the OOMOL Courier connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent manage Courier profiles, subscription lists, list subscriptions, and message sending through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send Courier messages and change or delete Courier profiles and subscription lists through the connected OOMOL account. <br>
Mitigation: Require exact target and payload confirmation before approving any write or destructive action. <br>
Risk: Incorrect payloads can affect unintended recipients, profiles, or lists. <br>
Mitigation: Fetch the live action schema before constructing payloads and confirm the intended effect with the user. <br>


## Reference(s): <br>
- [Courier homepage](https://www.courier.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-courier) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; Courier action responses are JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
