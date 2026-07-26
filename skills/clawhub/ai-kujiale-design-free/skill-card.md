## Description: <br>
Ai Kujiale Design Free guides an agent through a Kujiale-based interior design workflow for floorplan search, style selection, layout generation, and static rendering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Homeowners, interior design users, and agents use this skill to search Kujiale floorplans, choose a style, generate a room layout, and produce static render images for lightweight renovation previews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Kujiale access tokens could be exposed if copied into shared files or version control. <br>
Mitigation: Store the token only in local configuration or environment variables, keep it out of version control, and rotate it if exposure is suspected. <br>
Risk: Layout generation may consume Kujiale account quota or he dou. <br>
Mitigation: Confirm the selected floorplan, style, and layout action with the user before approving any quota-consuming step. <br>
Risk: The workflow relies on shell commands that interact with Kujiale services. <br>
Mitigation: Review each proposed command and token-bearing invocation before execution, especially when running in a shared workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-kujiale-design-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and static render result instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a user-provided Kujiale access token and requires confirmation before quota-consuming layout work.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
