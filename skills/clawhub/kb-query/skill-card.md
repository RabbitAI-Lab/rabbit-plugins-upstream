## Description: <br>
Answer Research KB questions from a team Gitea-backed knowledge base with OpenClaw-led evidence selection, stable citations, optional reference attachments, and optional high-value Q&A persistence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[myd2002](https://clawhub.ai/user/myd2002) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and team knowledge-base users use this skill to answer Research KB questions by selecting bounded Gitea-backed KB evidence, citing stable pages, and optionally persisting reusable Q&A when policy allows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read a team KB and may write curated Q&A pages to a Gitea repository when persistence is enabled. <br>
Mitigation: Install only where a bot account is intended to access the team KB, use a least-privilege Gitea token scoped to the target repository, and keep answerPolicy.writeHighValueAnswerToQa off unless persistence is desired. <br>
Risk: Attachment storage paths and temporary references could expose unintended files or be mistaken for stable knowledge-base sources. <br>
Mitigation: Limit backend storagePath values to approved upload or shared directories, and treat attachments as temporary context rather than stable citation sources. <br>
Risk: Answers may be unsupported when fetched KB evidence is insufficient. <br>
Mitigation: Require fetched evidence pages for knowledgeSufficient=true, cite only evidence pages returned by fetch, and state when the knowledge base cannot answer the question. <br>


## Reference(s): <br>
- [Kb Query ClawHub listing](https://clawhub.ai/myd2002/skills/kb-query) <br>
- [myd2002 publisher profile](https://clawhub.ai/user/myd2002) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Markdown answers and JSON result files with citations, source metadata, optional QA page changes, errors, and commit IDs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses bounded KB evidence pages and optional temporary attachment previews; optional Q&A persistence is gated by answerPolicy.writeHighValueAnswerToQa.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
