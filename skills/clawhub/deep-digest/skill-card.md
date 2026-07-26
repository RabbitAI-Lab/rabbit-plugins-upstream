## Description: <br>
Extracts cognitive patterns, key insights, and action signals from text such as messages, notes, articles, and conversations, producing structured digests across facts, patterns, and action signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heshengshi](https://clawhub.ai/user/heshengshi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to turn long-form or conversational text into concise markdown digests with factual summaries, recurring patterns, hidden assumptions, and prioritized follow-up actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can include the user's raw input in generated prompts and command output. <br>
Mitigation: Use only text you are allowed to process, and avoid secrets, credentials, regulated data, confidential conversations, or third-party private content. <br>
Risk: The release under-discloses that raw submitted text may be echoed in output. <br>
Mitigation: Review outputs before sharing them and redact or suppress raw prompt text if adapting the skill for sensitive workflows. <br>


## Reference(s): <br>
- [Deep Digest on ClawHub](https://clawhub.ai/heshengshi/skills/deep-digest) <br>
- [Artifact skill documentation](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown digest with sections for facts, pattern findings, and signals/actions; the runner may also emit JSON workflow metadata.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports full, facts-only, patterns-only, and signals-only modes, with optional evaluator veto settings.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
