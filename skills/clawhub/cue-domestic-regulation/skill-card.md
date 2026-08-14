## Description:

国内法规调研 helps agents retrieve Chinese domestic laws, regulations, administrative orders, legislative background, and compliance points from public regulatory sources through the Cue service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, compliance, and regulatory research users can use this skill to request Chinese domestic regulation research, receive a structured Chinese Markdown report, and trace conclusions back to cited public sources. It is useful for new-rule monitoring, compliance self-checks, legislative-background research, industry regulatory mapping, and administrative-enforcement basis checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User regulatory research questions are sent to Cue's external service.

Mitigation: Confirm external-service use is acceptable before running the skill, and avoid sending confidential client facts, trade secrets, or privileged legal details.

Risk: The Cue API key is stored locally and used for authenticated requests.

Mitigation: Store the key only in the expected local config file or environment variable, protect local filesystem access, and rotate the key if exposure is suspected.

Risk: The report may omit non-public guidance, incomplete local rules, or unavailable source material, and it is not legal advice.

Mitigation: Review cited sources directly and have qualified legal or compliance reviewers validate conclusions before relying on them for decisions.

## Reference(s):

- [Cue API Key](https://cuecue.cn/api-key)
- [Cue Skills Runner](https://github.com/sensedeal/cue-skills)
- [Cue Skills Runner Gitee Mirror](https://gitee.com/sensedeal/cue-skills)
- [National Laws and Regulations Database](https://flk.npc.gov.cn)
- [State Council and Government Publications](https://www.gov.cn)
- [Ministry of Justice](https://www.moj.gov.cn)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese Markdown report with source links and optional shell commands for setup, health checks, execution, and format conversion]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are written to a local Markdown file path and may be converted to Word or PDF with pandoc.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
