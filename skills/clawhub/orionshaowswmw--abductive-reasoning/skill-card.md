## Description:

Helps agents explain surprising observations by generating multiple hypotheses, scoring them on coverage, simplicity, prior plausibility, and predictive power, then selecting a provisional best explanation with a discriminating test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, operators, and other agent users apply this skill when diagnosing bugs, outages, anomalies, symptoms, or uncertain events where several explanations are possible. It structures the work into candidate generation, comparative scoring, provisional selection, and a concrete test that can change the conclusion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make a plausible explanation feel more certain than the evidence supports, especially in medical, legal, investigative, personnel, financial, or reputational contexts.

Mitigation: Use it to organize hypotheses, questions, tests, and update triggers; require independent evidence, expert review, and appropriate authority before consequential decisions or accusations.

Risk: A user or agent may stop after the first explanation that fits the facts.

Mitigation: Require at least three candidate hypotheses plus an unknown placeholder, compare each against coverage, simplicity, prior plausibility, and predictive power, and state the closest rival.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/abductive-reasoning)
- [Sources - abductive-reasoning](references/sources.md)
- [Peirce, the Wine Cellar, and the Watch - 1879](examples/peirce-the-wine-cellar-and-the-watch-1879.md)
- [The Discovery of Neptune from Uranus Anomalies - 1846](examples/the-discovery-of-neptune-from-uranus-anomalies-1846.md)
- [Psychology of Intelligence Analysis](https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text]

**Output Format:** [Markdown abductive inference with hypothesis candidates, a scoring table, a best-explanation summary, a discriminating test, and an update trigger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code, shell commands, credential access, persistence, or hidden data access are described in the release evidence.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
