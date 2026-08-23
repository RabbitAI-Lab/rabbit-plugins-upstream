## Description:

This skill helps agents analyze Ozon keyword demand with Qinghu AI data, compare keyword trends and related products, and turn the results into keyword lists and product-selection guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and ecommerce analysts use this skill to research Ozon search demand, inspect keyword trends, identify related products, and decide which products or listing optimizations to prioritize.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Ozon keyword and product research queries to Qinghu's third-party API.

Mitigation: Users should be comfortable sharing those queries with Qinghu before installing or invoking the skill.

Risk: The skill uses a Qinghu token from user input or environment variables.

Mitigation: Provide only an intended Qinghu API token and avoid exposing unrelated credentials.

Risk: Some API calls may consume Qinghu points.

Mitigation: The skill should ask for confirmation before paid calls and report consumption from the response envelope.

Risk: Larger result sets can be written as local export files.

Mitigation: Review generated export files before sharing them outside the local environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-keyword-picker)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown recommendations with optional exported table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include concise previews, links to local exports for larger datasets, and Qinghu point consumption notes when paid API calls are made.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
