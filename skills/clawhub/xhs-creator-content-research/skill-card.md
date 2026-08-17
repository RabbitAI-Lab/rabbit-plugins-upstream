## Description:

Supports Xiaohongshu (XHS) creator content research, including account post lists, recent publishing review, content-style analysis, benchmarking, and account tracking for brands, MCNs, content operators, and creators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External brands, MCNs, content operators, and creators use this skill to fetch read-only XHS creator post data and summarize recent content patterns, engagement signals, and follow-up research questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running a third-party npm CLI with SOCIALDATAX_API_KEY introduces local runtime and credential-handling risk.

Mitigation: Run it in a trusted environment, review the package source and permissions as needed, and provide only the intended SocialDataX API key.

Risk: Using unbounded pagination with --all can increase API cost and collection scope.

Mitigation: Prefer --pages or --max-items unless a full fetch is intentional.

## Reference(s):

- [SocialDataX AI](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-creator-content-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY plus node/npm; CLI calls can use bounded pagination with --pages or --max-items.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
