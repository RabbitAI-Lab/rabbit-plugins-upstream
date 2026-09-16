## Description:

国内法规调研 helps agents retrieve Chinese domestic laws, regulations, and administrative materials, summarize legislative background and compliance points, and return source-linked Chinese reports for business and personal legal research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, legal teams, compliance teams, and individuals use this skill to research Chinese domestic legal and regulatory questions. It produces source-linked research reports on applicable rules, legislative context, compliance obligations, enforcement practice, and practical next steps.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill relies on Cue's external service and a separately cloned runner.

Mitigation: Pin and inspect the runner before use, review updates before installation, and pause use when Cue service health checks fail.

Risk: Cue API credentials may be stored in ~/.cue/config.json.

Mitigation: Protect the config file with restrictive filesystem permissions and rotate the key if it may have been exposed.

Risk: Legal facts submitted in prompts are sent to Cue for research.

Mitigation: Avoid submitting sensitive legal facts unless authorized and comfortable using Cue, and redact unnecessary personal or confidential details.

Risk: Generated legal research can be incomplete or unsuitable as legal advice.

Mitigation: Verify cited sources directly and consult qualified counsel before relying on the report for legal or compliance decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-domestic-regulation)
- [Cue playbook](https://cuecue.cn/playbook)
- [Cue API key management](https://cuecue.cn/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese Markdown reports with source links, local file paths, and optional shell commands for setup and conversion.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are written to a local Markdown file and, when the runner returns a conversation ID, include a Cue share link.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence; artifact frontmatter reports 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
