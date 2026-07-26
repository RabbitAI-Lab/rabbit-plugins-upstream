## Description: <br>
Ai Assistant analyzes long commercial and legal documents to extract structure, assumptions, risks, version differences, and decision-focused improvement suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and business reviewers use this skill to prepare structured reviews of contracts, legal memoranda, proposals, policies, negotiation drafts, and multi-version document changes. It supports risk spotting and decision preparation but does not replace licensed legal advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad command execution for document handling. <br>
Mitigation: Use it only in an agent environment where command execution is disabled or requires explicit approval. <br>
Risk: The skill accepts callback URLs that could receive sensitive document-derived information. <br>
Mitigation: Use callback URLs only when you control the destination and understand what data will be sent. <br>
Risk: The skill analyzes sensitive legal and business documents and may produce incorrect or overconfident conclusions. <br>
Mitigation: Treat outputs as review preparation, require human review, and escalate legal, tax, compliance, or signing decisions to qualified counsel. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-assistant) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands] <br>
**Output Format:** [Markdown with structured analysis sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include document assessments, core-logic summaries, risk lists, structure-improvement suggestions, version comparisons, uncertainty notes, and recommended next steps.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
