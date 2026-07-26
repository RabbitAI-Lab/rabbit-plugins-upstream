## Description: <br>
EchoDecks integrates with the EchoDecks API for flashcard management, study sessions, and AI-generated flashcards and podcast summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drgeld](https://clawhub.ai/user/drgeld) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and study-focused agents use this skill to list decks and due cards, submit spaced-repetition reviews, generate flashcards from topics or text, generate podcasts from decks, and retrieve user study statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Decks, notes, topics, and raw text provided to generation or study workflows are processed by EchoDecks. <br>
Mitigation: Avoid confidential, regulated, or personal material unless the user's EchoDecks use permits that processing. <br>
Risk: Card review submission and card or podcast generation can change study state or spend EchoDecks credits. <br>
Mitigation: Ask the agent to confirm before submitting reviews or running credit-spending generation actions. <br>


## Reference(s): <br>
- [EchoDecks ClawHub Skill Page](https://clawhub.ai/drgeld/skills/echodecks) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration] <br>
**Output Format:** [JSON API responses with command-line usage and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ECHODECKS_API_KEY; generation and review actions may send study content to EchoDecks and spend credits.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
