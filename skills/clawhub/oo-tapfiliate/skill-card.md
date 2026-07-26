## Description: <br>
Tapfiliate (tapfiliate.com). Use this skill for ANY Tapfiliate request: reading, creating, and updating data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Tapfiliate through an OOMOL-connected account, including affiliate, affiliate group, click, conversion, program, commission, and reporting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confirmed write actions can modify Tapfiliate affiliate, click, or conversion records. <br>
Mitigation: Review the exact proposed payload and expected account effect before approving create or conversion actions. <br>
Risk: The skill depends on an OOMOL-connected Tapfiliate account and the oo CLI being installed, authenticated, and connected. <br>
Mitigation: Install it only when the agent should use that connected account, and use first-time setup or connection recovery only after an auth or connection failure. <br>


## Reference(s): <br>
- [Tapfiliate homepage](https://tapfiliate.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tapfiliate) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands are intended for the oo CLI and may return JSON responses from Tapfiliate connector actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
