## Description: <br>
A Chinese-language six-mode writing and thinking skill for polishing text, identifying strengths, critically testing plans, reviewing records, creating channel-specific content, and generating cross-domain idea cards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[156554395](https://clawhub.ai/user/156554395) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to route Chinese-language writing and thinking requests into six bounded modes: polish, comment, interrogate, review, create, and sprout. It is intended for user-provided text, notes, ideas, or explicitly provided file paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: File-path inputs in review, creation, or idea-development modes can expose unrelated private material if the user points the agent at broad or sensitive paths. <br>
Mitigation: Use pasted material or paths only for content intentionally shared with the agent; avoid credentials, private system files, and unrelated personal archives. <br>
Risk: Critical review and content creation outputs depend on the completeness and accuracy of the user-provided material. <br>
Mitigation: Review generated critiques, drafts, and idea cards against the original material before acting on or publishing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/156554395/skills/dedao-thinking-skills) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [polish.md](artifact/polish.md) <br>
- [comment.md](artifact/comment.md) <br>
- [interrogate.md](artifact/interrogate.md) <br>
- [review.md](artifact/review.md) <br>
- [create.md](artifact/create.md) <br>
- [sprout.md](artifact/sprout.md) <br>
- [evals.json](artifact/evals.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Chinese-language plain text or Markdown responses, including polished copy, critiques, retrospectives, content drafts, and idea cards.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Mode-specific length and structure constraints apply; review, creation, and sprout modes require pasted material or file paths supplied by the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
