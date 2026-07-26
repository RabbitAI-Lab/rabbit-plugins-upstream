## Description: <br>
AI-powered flashcard management with automated podcast generation and spaced-repetition study tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drgeld](https://clawhub.ai/user/drgeld) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and learning-focused agents use this skill to manage EchoDecks flashcard decks, run spaced-repetition review workflows, generate study cards from topics or text, and request podcast summaries from study material. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Study content, imported material, and podcast-generation inputs are sent to EchoDecks for processing. <br>
Mitigation: Install and use the skill only when EchoDecks is trusted for the material being processed. <br>
Risk: The EchoDecks API key could be exposed if it is pasted into prompts or deck content. <br>
Mitigation: Store ECHODECKS_API_KEY in the agent environment and avoid including it in user-visible content. <br>
Risk: Card and podcast generation can consume account credits or change account state. <br>
Mitigation: Review generation, review-submission, and account-changing actions before running them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/drgeld/skills/echodecks-ultimate) <br>
- [EchoDecks](https://echodecks.app) <br>
- [EchoDecks Settings](https://echodecks.app/settings) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ECHODECKS_API_KEY for authenticated EchoDecks API operations.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
