## Description:

国内法规调研 helps agents retrieve domestic Chinese laws, regulations, administrative orders, legislative background, and compliance points from public sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, compliance, and policy users use this skill to research domestic Chinese regulatory materials, summarize compliance obligations, and produce source-linked reports for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented command pattern can allow untrusted query text to execute as shell code.

Mitigation: Invoke the runner with an argument-array or another shell-free method, and avoid passing raw user text through shell interpolation.

Risk: The skill requires a Cue API key and the artifact does not provide enough protection guidance for that secret.

Mitigation: Treat the Cue API key as a secret, keep it out of logs and repositories, and restrict access to the local config file.

Risk: Queries are sent to Cue, and the security guidance says to use the skill only for queries the user is comfortable sending there.

Mitigation: Review the skill before installing and avoid submitting confidential or sensitive legal/compliance questions unless that disclosure is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-domestic-regulation)
- [Cue API key page](https://cuecue.cn/hub/api-key)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [National Laws and Regulations Database](https://flk.npc.gov.cn)
- [State Council of China](https://www.gov.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese Markdown report with source links, plus shell command and configuration snippets for setup and execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are written to a local Markdown file path; optional conversion to DOCX or PDF is described in the artifact.]

## Skill Version(s):

1.0.5 (source: server release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
