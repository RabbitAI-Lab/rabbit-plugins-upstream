## Description:

Helps Taobao and Tmall merchants, shop designers, and e-commerce operators turn product photos, category rules, campaign requirements, selling points, brand constraints, and prohibited terms into main-image plans, ad-image variants, AI-HIVE generation commands, and mobile-readiness checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, e-commerce operators, and designers use this skill to plan Taobao/Tmall main images, through-train ad images, campaign variants, prompt sets, runnable AI-HIVE commands, and acceptance checklists. It is aimed at commercial content production where product facts, rights to source media, platform constraints, budget, and manual review are part of the workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE API keys may be supplied through environment variables, command-line arguments, or a local config file.

Mitigation: Use scoped credentials where possible, avoid placing secrets in prompts or committed files, and verify local config file permissions before sharing the workspace.

Risk: Product images, reference media, prompts, and other campaign material may be uploaded to AI-HIVE during generation workflows.

Mitigation: Upload only media the user has rights to use, remove secrets or sensitive personal data, and get explicit approval before sending reference assets to the service.

Risk: Generation tasks may incur cost and can run asynchronously in batches.

Mitigation: Confirm routing mode, model choice, pricing snapshot, prompt, batch size, and review criteria before submitting tasks; start with a small sample before batch generation.

Risk: E-commerce outputs can contain unsupported product claims, misleading performance promises, or platform-rule issues.

Mitigation: Keep claims grounded in supplied product facts, reject fabricated certifications or testimonials, and perform human review against platform and brand requirements before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/taobao-main-image-studio-ai-hive)
- [AI-HIVE chat and API key access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with JSON files and inline bash/Python commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create blueprint JSON files, submit AI-HIVE generation tasks, poll asynchronous results, and download generated media when the user supplies credentials and confirms potentially billable parameters.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
