## Description:

Dorar Hadith searches Dorar hadith records by Arabic text or Dorar ID and returns source and authenticity details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[m7madash](https://clawhub.ai/user/m7madash)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search hadith text or Dorar IDs and review narrator, source, page, and grading information before quoting or sharing a hadith.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A specially crafted query can execute local Python code through the query encoding step.

Mitigation: Avoid untrusted or copied query text until the script encodes input through a safe argument or stdin-based method.

Risk: Search terms are sent to the documented Dorar endpoint.

Mitigation: Use only query text suitable for submission to dorar.net and review local policy before use in sensitive contexts.

## Reference(s):

- [Dorar Hadith on ClawHub](https://clawhub.ai/m7madash/skills/dorar-hadith)
- [Dorar API endpoint](https://dorar.net/dorar_api.json?skey=QUERY&callback=?)
- [Dorar search page](https://dorar.net/hadith/search?q=QUERY)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with shell commands and formatted text results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include hadith text, narrator, scholar, source, page or number, authenticity grading, and a Dorar search link when available.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
