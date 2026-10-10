## Description:

Helps agents search Shopee's T+1 brand data by category or brand name and rank brands by product count, recent sales volume, revenue, or shop count.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and market researchers use the skill to find and compare brands within supported marketplaces and categories using recent brand metrics.

### Deployment Geography for Use:

Global; brand data covers Shopee markets in Taiwan, Malaysia, Indonesia, Thailand, the Philippines, Singapore, Vietnam, and Brazil.

## Known Risks and Mitigations:

Risk: Brand lookups may make paid Qinghu API calls.

Mitigation: Check the per-call estimate and obtain user approval before spending credits.

Risk: The tool uses a Qinghu API token for authenticated requests.

Mitigation: Store the token securely and avoid disclosing it in agent output or shared files.

Risk: The skill may install or upgrade qhkit or Node on the host.

Mitigation: Prefer a pinned, preinstalled qhkit version in a controlled environment; review host changes before installing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shopee-brand-list)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise brand rankings and summaries; table files for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shopee data is updated T+1; results depend on the requested site and date.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
