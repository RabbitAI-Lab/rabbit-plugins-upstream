## Description: <br>
Perform instant crypto swaps via ChangeNOW and earn affiliate commissions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yakelb0815](https://clawhub.ai/user/yakelb0815) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to estimate or create ChangeNOW crypto swap transactions while including the configured affiliate partner ID for commission tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live transaction mode is financial activity and may route swaps through an affiliate-enabled workflow. <br>
Mitigation: Use estimate mode first, compare fees if needed, and verify the asset, network, amount, destination address, affiliate involvement, and pay-in address before sending crypto. <br>
Risk: The ChangeNOW API key is sensitive configuration. <br>
Mitigation: Keep CHANGENOW_API_KEY private and provide it through environment or secret configuration rather than sharing it in prompts or logs. <br>


## Reference(s): <br>
- [ChangeNOW API endpoint](https://api.changenow.io/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with bash examples; script output is JSON plus transaction guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CHANGENOW_API_KEY; live transaction mode can return a pay-in address for a crypto swap routed with the affiliate link ID.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
