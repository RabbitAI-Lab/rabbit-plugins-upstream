## Description:

Grades tomato and strawberry ripeness from fruit images, videos, or URLs by using AI vision to assess color, colored-area ratio, gloss, and relative size, then returns structured grading results and harvest guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External growers, greenhouse operators, garden users, and agricultural cooperatives use this skill to grade tomato or strawberry ripeness from images or videos and review report history. Developers and agents can invoke the bundled script to submit media or URLs to the service and return structured analysis, report links, or historical report lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fruit images, videos, URLs, and report-history requests are sent to the LifeEmergence/SMYX cloud service.

Mitigation: Use the skill only with media and URLs that are appropriate for that cloud service, and review the configured endpoints before installation or execution.

Risk: The skill creates or reuses a local identity and stores account tokens in a workspace SQLite database.

Mitigation: Treat the workspace data directory as credential-bearing storage, restrict access to it, and clear local identity or token records when they are no longer needed.

Risk: Development or LAN endpoint configuration is present in the artifact.

Mitigation: Confirm the active configuration uses the intended production endpoint before running the skill in a shared or commercial environment.

Risk: Ripeness grades and harvest advice are visual decision-support outputs rather than a substitute for enterprise grading standards.

Mitigation: Review results against local crop quality requirements before using them for commercial grading or harvest decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fruit-ripeness-grading-analysis)
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown prose and tables with JSON-style structured analysis results, report links, and optional saved text output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The script supports basic, standard, and JSON detail modes and can write results to a user-specified output file.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
