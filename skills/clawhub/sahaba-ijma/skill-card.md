## Description:

Searches Dorar Al-Sunniyah for reports about Sahaba consensus and sayings, returning source, narrator, scholar, page or number, and authenticity status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[m7madash](https://clawhub.ai/user/m7madash)

### License/Terms of Use:

MIT-0

## Use Case:

External users and researchers use this skill to run Arabic Dorar.net searches for narrated reports about Sahaba consensus or sayings and review returned sourcing and grading details. It supports reference lookup; users should rely on the returned grading, source metadata, and their own review for religious conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A crafted search query can be interpreted as local Python code before the Dorar.net search runs.

Mitigation: Use only trusted search terms until query encoding is fixed to pass input as a Python argument or environment value instead of embedding it in inline Python code.

Risk: The skill depends on live Dorar.net network lookup and returned authenticity metadata.

Mitigation: Review returned narrator, source, page or number, and grading details before relying on a result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/m7madash/skills/sahaba-ijma)
- [Dorar Al-Sunniyah API endpoint](https://dorar.net/dorar_api.json?skey=QUERY&callback=?)
- [Dorar hadith search](https://dorar.net/hadith/search?q=QUERY)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Plain text search results with source and authenticity fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are fetched from Dorar.net for the provided Arabic query and printed as numbered entries.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
