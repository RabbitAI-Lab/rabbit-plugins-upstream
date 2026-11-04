## Description:

Analyzes reptile video uploads or URLs and returns a structured health report with potential concerns and care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners use the skill to review reptile videos for visible health concerns and receive a structured report with care suggestions. They can also retrieve prior reports from the service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The no-analysis option may not prevent video uploads, and report accounts may be mixed in a shared workspace.

Mitigation: Wait for fixes to the no-analysis behavior and identity isolation before using the skill in a shared workspace.

Risk: Videos are uploaded to Life Emergence services, account details and tokens can persist locally, and the client cannot verify the stated immediate video deletion.

Mitigation: Treat video uploads as external data sharing; request clearer enrollment, credential handling, and deletion assurances before use.

## Reference(s):

- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crawl-analysis)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured health report in text or JSON; Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include potential health warnings, care suggestions, and report links. Results are informational and do not replace a reptile veterinarian's assessment.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
