## Description:

Temu US Ads API gateway for creating, modifying, inspecting, and reporting on Temu search recommendation ads through LinkFox Partner US Ads scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu sellers, operators, and developers use this skill to automate US advertising workflows including ad creation, budget and ROAS changes, eligibility checks, reports, and operation logs.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill routes Temu Ads requests through the LinkFox gateway and requires LinkFox and Temu credentials.

Mitigation: Install only when the LinkFox gateway is trusted and use least-privilege Temu tokens for the required ads workflow.

Risk: Temu access tokens may be stored locally for reuse.

Mitigation: Avoid shared machines, protect or relocate the token store, and review ~/.linkfox for stored credentials.

Risk: Scripts persist full API responses to local linkfox/ data files.

Mitigation: Review linkfox/ output files for sensitive account, ad, or report data and delete or secure them according to local policy.

Risk: The workflow can change advertising budgets, ROAS settings, status, or paid account actions.

Mitigation: Manually confirm budget changes, ad deletion or pause actions, and any paid order or recharge flow before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-ads-us)
- [API reference](references/api.md)
- [Temu accessToken authorization](references/access-token.md)
- [Partner US Ads catalog](references/partner-us-catalog.md)
- [Ads API documentation index](references/apis/README.md)
- [Create ads Partner documentation](https://partner-us.temu.com/documentation?menu_code=1e72b5cceef545ec8f9652b9e56dd054&sub_menu_code=7bc9231776304158a895e41a816b7805)
- [Modify ads Partner documentation](https://partner-us.temu.com/documentation?menu_code=1e72b5cceef545ec8f9652b9e56dd054&sub_menu_code=0b7140898262428eb8a4b28609112651)
- [Mall ad reports Partner documentation](https://partner-us.temu.com/documentation?menu_code=1e72b5cceef545ec8f9652b9e56dd054&sub_menu_code=595f05856989480aa03abd58da203047)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; scripts emit JSON to stdout and saved JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are saved under linkfox/<date>/<session>/data; large responses are summarized unless --inline is used.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
