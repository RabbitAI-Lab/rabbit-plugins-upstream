## Description:

Searches dknowc trusted-intelligence services for authoritative Chinese legal, policy, standards, government-service, subsidy, tax-benefit, and compliance materials, then returns source-backed answers with clickable provenance HTML and clean Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, legal and policy researchers, and business users use this skill to retrieve and verify authoritative Chinese laws, policies, standards, public-service requirements, subsidies, tax incentives, and compliance evidence through dknowc.cn services.

### Deployment Geography for Use:

Global; content and service coverage are focused on Chinese laws, policies, standards, and government-service materials.

## Known Risks and Mitigations:

Risk: The setup flow can collect a phone number and SMS code and return a live API key through agent output.

Mitigation: Prefer configuring DKNOWC_API_KEY through a trusted secret or environment mechanism; avoid running the registration helper in shared terminals, CI, or logged sessions, and do not persist the key unless explicitly intended.

Risk: Queries, task context, and retrieved-material requests are sent to dknowc.cn services.

Mitigation: Install and use the skill only if the user is comfortable using dknowc.cn services, and avoid submitting unnecessary confidential information.

Risk: Legal, policy, standards, tax, subsidy, or compliance outputs may be used for consequential decisions.

Mitigation: Review the clickable provenance HTML and authoritative source links, and confirm material decisions with the relevant authority or qualified professional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-trusted-search)
- [dknowc MaaS platform](https://platform.dknowc.cn/)
- [Trusted search API endpoint](https://open.dknowc.cn/dependable/search)
- [Deep search API endpoint](https://open.dknowc.cn/api/services/deep-query/v2)

## Skill Output:

**Output Type(s):** [text, markdown, HTML, SVG, JSON, shell commands, configuration guidance]

**Output Format:** [Markdown answers with citation markers, clickable HTML provenance reports, clean Markdown files, JSON API outputs, and optional SVG visualizations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY; makes network calls to dknowc.cn services; deep search is used only on explicit request or confirmation.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
