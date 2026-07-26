## Description: <br>
Guided first-run demo for the Cargo CLI that takes a fresh workspace to about 25 buyer-persona-matched leads with a cost receipt in under two minutes, then offers to save the search as a recurring play. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cargo-ai](https://clawhub.ai/user/cargo-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, sales operators, and GTM teams use this skill to demonstrate Cargo from a new workspace by sourcing buyer-persona-matched leads, showing a spend receipt, and optionally saving the search as a weekly play. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use connected lead providers and spend credits while retrieving prospect data. <br>
Mitigation: Keep the quickstart on the capped low-cost path and require explicit user approval before any higher-cost fallback runs. <br>
Risk: Demo lead output is temporarily written under /tmp. <br>
Mitigation: Treat the temporary files as prospect data and remove or protect them when the demo is complete. <br>
Risk: Saving the search as a weekly play can continue using provider data and credits. <br>
Mitigation: Create the recurring play only after explicit user consent, and review or disable the schedule when it is no longer needed. <br>


## Reference(s): <br>
- [Cargo Quickstart on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-quickstart) <br>
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands, lead tables, receipts, and next-step guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the Cargo CLI and a Cargo account; may use connected lead providers and credits.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
