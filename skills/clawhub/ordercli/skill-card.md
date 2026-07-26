## Description: <br>
Foodora-only CLI for checking past orders and active order status (Deliveroo WIP). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to guide use of ordercli for Foodora order lookup, active order tracking, history inspection, and guarded reorder workflows. Deliveroo support is described as work in progress. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill documents importing Chrome cookies and browser sessions, which can expose sensitive Foodora login data. <br>
Mitigation: Install only if the publisher is trusted; prefer password-stdin or an isolated browser profile, and review how imported sessions are stored and removed before use. <br>
Risk: Reorder commands can change a cart or prepare a repeat purchase. <br>
Mitigation: Preview reorder actions first and require explicit confirmation before running commands that alter carts or orders. <br>


## Reference(s): <br>
- [Ordercli homepage](https://ordercli.sh) <br>
- [ClawHub skill listing](https://clawhub.ai/steipete/skills/ordercli) <br>
- [Foodora Austria](https://www.foodora.at/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that use account credentials, browser profiles, cookies, or session data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
