## Description: <br>
Stop Slop Zh helps agents review and revise Chinese prose to reduce common AI-like writing patterns such as cliches, formulaic structure, abstract phrasing, nominalizations, and punctuation tells. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leeguooooo](https://clawhub.ai/user/leeguooooo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, writers, editors, and developers use this skill when drafting, reviewing, or polishing Chinese text for human readers. It guides an agent to identify AI-like wording, sentence structures, punctuation habits, and over-generalized claims, then revise without inventing unsupported facts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can over-apply style cleanup to technical, legal, academic, official, or bilingual writing where formal phrasing or exact wording may be intentional. <br>
Mitigation: Treat its suggestions as review guidance in those contexts and keep wording that is required for precision, compliance, convention, or the author's voice. <br>
Risk: Rewriting abstract claims into concrete details can create unsupported facts if the agent fills in numbers, names, or examples without evidence. <br>
Mitigation: Use only source-backed details; otherwise keep a plainer statement, remove the claim, or leave an explicit placeholder for the author to supply the fact. <br>


## Reference(s): <br>
- [Source repository](https://github.com/leeguooooo/stop-slop-zh) <br>
- [ClawHub skill page](https://clawhub.ai/leeguooooo/skills/stop-slop-zh) <br>
- [Chinese AI phrase checklist](artifact/references/phrases.md) <br>
- [Chinese AI structure checklist](artifact/references/structures.md) <br>
- [Chinese AI punctuation checklist](artifact/references/punctuation.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or plain text review and revision guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include rewritten Chinese prose, scoring notes, checklist findings, and placeholders for author-supplied facts.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
