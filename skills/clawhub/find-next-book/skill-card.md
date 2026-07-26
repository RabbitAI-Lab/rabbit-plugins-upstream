## Description: <br>
Recommend the next book to read by combining the user's current request with relevant conversation context, available long-term memory, reading history, and verified book information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fov6363](https://clawhub.ai/user/fov6363) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Readers, knowledge workers, and other external users use this skill to choose one timely next book based on their current request, relevant memory, reading history, and verified book evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Personalized recommendations may draw on long-term memory or reading history. <br>
Mitigation: Use only relevant memory, generalize sensitive details, and expose only the recommendation signals actually used. <br>
Risk: Book facts, editions, or availability may be stale or incorrect. <br>
Mitigation: Verify title, author, premise, edition-sensitive claims, and availability against reliable current sources before presenting the recommendation. <br>
Risk: The default prompt and response template are in Chinese, which may not match every user's preferred language. <br>
Mitigation: Ask for or follow the user's preferred language when it differs from the default. <br>


## Reference(s): <br>
- [Recommendation Rubric](references/recommendation-rubric.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/fov6363/skills/find-next-book) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown response with concise recommendation sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides one primary book recommendation, up to two alternatives when useful, source-backed uncertainty notes, and practical reading guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
