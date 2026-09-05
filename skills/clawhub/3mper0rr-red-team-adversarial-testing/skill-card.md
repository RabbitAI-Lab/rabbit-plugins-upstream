## Description:

Guides authorized adversarial testing and red-team evaluation of AI models, including prompt injection, jailbreak, tool abuse, exfiltration simulation, and reporting workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[3mper0rr](https://clawhub.ai/user/3mper0rr)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security engineers, and AI assurance teams use this skill to plan and document authorized red-team evaluations of AI systems. It helps map attack surfaces, build test corpora, record results, and produce a final vulnerability report with recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill concerns adversarial testing techniques that could be misapplied outside an authorized assessment.

Mitigation: Use only on systems the operator owns or has explicit permission to test.

Risk: Prompt injection and simulated exfiltration tests can expose sensitive data if real secrets are placed into test corpora or reports.

Mitigation: Keep test data scoped to the assessment and avoid including real secrets in generated corpora or reports.

Risk: Attack corpus content could drift from evaluation into harmful operational guidance.

Mitigation: Keep payloads limited to defensive evaluation and avoid functional malware or real-world harmful content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/3mper0rr/skills/3mper0rr-red-team-adversarial-testing)
- [Publisher profile](https://clawhub.ai/user/3mper0rr)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Markdown reports with JSONL attack corpus and CSV test results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces mapped surfaces, threat models, attack corpora, test results, and final recommendations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
