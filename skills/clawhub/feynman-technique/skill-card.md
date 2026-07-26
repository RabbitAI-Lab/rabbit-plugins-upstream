## Description: <br>
Guides an agent through the Feynman Technique to test whether a user genuinely understands a concept by producing a plain-language explanation, diagnosing gaps, and refining the explanation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and employees use this skill to test understanding of a specific concept before teaching, presenting, or making decisions. It guides an agent to elicit a plain-language explanation, diagnose jargon, circularity, hedges, and unjustified claims, then refine the explanation into a Feynman Understanding Audit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs the agent to fetch a remote replacement instruction file at runtime, which can change behavior after installation. <br>
Mitigation: Review this behavior before installation; in controlled environments, use the packaged instructions or treat remote content only as optional reference material. <br>
Risk: Simplifying concepts that are irreducibly formal can remove essential nuance. <br>
Mitigation: Redirect formal concepts or name the irreducible core instead of forcing a plain-language simplification. <br>


## Reference(s): <br>
- [Feynman Technique on ClawHub](https://clawhub.ai/deciqai/skills/feynman-technique) <br>
- [Primary sources](references/sources.md) <br>
- [Feynman and the Challenger O-Ring Investigation](examples/feynman-challenger-o-ring-1986.md) <br>
- [Freshman-Lecture Test and Spin-Statistics](examples/feynman-freshman-lecture-spin-statistics-1961.md) <br>
- [AI Jargon Audit Example](examples/feynman-ai-jargon-audit-2024-2026.md) <br>
- [The Feynman Lectures on Physics](https://www.feynmanlectures.caltech.edu/) <br>
- [Rogers Commission Appendix F](https://science.ksc.nasa.gov/shuttle/missions/51-l/docs/rogers-commission/Appendix-F.txt) <br>
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) <br>
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with a structured Feynman Understanding Audit] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask step-by-step questions in coach mode and stop for user responses.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
