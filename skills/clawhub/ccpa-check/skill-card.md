## Description:

CCPA/CPRA Compliance Check assesses 12 core controls for businesses subject to California privacy law and can generate scored reports through CQDev cloud scoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External users, compliance teams, and developers use this skill to preview CCPA/CPRA check items and generate local self-check reports from yes/no/not-applicable responses. Scored checks require a free API key and send answers to compliancehub.cn.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored checks send compliance answers and the API key to compliancehub.cn.

Mitigation: Run scored checks only when the user accepts that data transfer, and confirm the destination before use.

Risk: The --login flow sends login credentials to compliancehub.cn and can write an API key to the local user configuration directory.

Mitigation: Use --login only as an explicit user action; prefer COMPLIANCEHUB_API_KEY on shared or CI systems.

Risk: Preview mode still attempts a public rule-library fetch before falling back to bundled check items.

Mitigation: Use network controls or a no-network sandbox when a no-network run is required.

Risk: The generated report is general compliance guidance and is not legal advice.

Mitigation: Review results with qualified counsel before relying on them for formal CCPA/CPRA compliance decisions.

## Reference(s):

- [CCPA Check ClawHub listing](https://clawhub.ai/wwumit/skills/ccpa-check)
- [API key reference](references/api_key.md)
- [CQDev compliance account page](https://compliancehub.cn/account.html?skill=ccpa-check)
- [CQDev compliance cloud](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [text, JSON, HTML, files, shell commands, guidance]

**Output Format:** [Markdown guidance with CLI commands; runtime reports can be text, JSON, or HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scored reports are produced locally after cloud evaluation; preview modes list the 12 check items without requiring an API key.]

## Skill Version(s):

2.0.3 (source: server release evidence, package.json, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
