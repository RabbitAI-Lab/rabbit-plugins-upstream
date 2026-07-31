## Description: <br>
Envoy helps agents operate Envoy through an OOMOL-connected account for reading, creating, and updating Envoy data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to work with Envoy employee, location, sign-in flow, and invite data through OOMOL's Envoy connector instead of calling the Envoy API directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Envoy reads can expose sensitive workplace information such as employee, invite, location, and sign-in flow data. <br>
Mitigation: Install only when agents should access the connected Envoy account, keep the Envoy connection least-privileged, and treat list or search results as sensitive. <br>
Risk: Actions that change Envoy data can modify records if given an incorrect payload. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running any write action. <br>
Risk: Connection scope or credential problems can lead agents toward unnecessary setup or reconnection steps. <br>
Mitigation: Use first-time setup only after an authentication, scope, credential, app, or billing error occurs. <br>


## Reference(s): <br>
- [ClawHub Envoy skill](https://clawhub.ai/oomol/skills/oo-envoy) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Envoy homepage](https://envoy.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include Envoy connector results containing workplace data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: skill metadata and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
