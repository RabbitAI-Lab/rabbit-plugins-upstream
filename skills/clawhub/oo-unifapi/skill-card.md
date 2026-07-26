## Description: <br>
UnifAPI (unifapi.com) lets agents handle reading, creating, and updating data through the OOMOL `oo` CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect live UnifAPI action schemas, build matching JSON payloads, and run social, SEO, GEO, page rendering, link extraction, hotel, and ID conversion actions through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate many UnifAPI actions across social, SEO, GEO, rendering, and utility data sources through an OOMOL-connected account. <br>
Mitigation: Install it only when that account-level access is intended, and review requested actions and payloads before execution. <br>
Risk: Actions tagged `[write]` or with unclear write labeling may change UnifAPI state or have effects beyond simple reads. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running any tagged write action, and treat ambiguous labels cautiously. <br>
Risk: First-time setup can install the `oo` CLI and connect UnifAPI credentials through OOMOL. <br>
Mitigation: Run setup only after an authentication or connection failure requires it, and avoid proactively opening login or connection flows. <br>


## Reference(s): <br>
- [UnifAPI homepage](https://unifapi.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-unifapi) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses from `oo connector run` are JSON objects with `data` and `meta.executionId` fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
