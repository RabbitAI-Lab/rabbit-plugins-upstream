## Description: <br>
Manages EchoDecks flashcard decks, AI-generated cards, podcast study sessions, study links, reviews, credits, and learning statistics through the EchoDecks API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drgeld](https://clawhub.ai/user/drgeld) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Learners, educators, and agents use this skill to create and manage EchoDecks study decks, generate flashcards or podcasts from study material, and submit spaced-repetition reviews. It is also useful for checking account credits and study progress before starting content-generation actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Study prompts, deck content, and generated-card source text are sent to EchoDecks. <br>
Mitigation: Avoid submitting private health, business, personal, or otherwise sensitive content unless sharing it with EchoDecks is intended. <br>
Risk: The skill can create content, submit spaced-repetition reviews, and perform actions that change account data. <br>
Mitigation: Review agent actions before creating decks, generating content, or submitting reviews. <br>
Risk: AI card generation and podcast synthesis can consume EchoDecks account credits. <br>
Mitigation: Check credit balance and confirm cost-bearing actions before running card or podcast generation. <br>
Risk: The EchoDecks API key grants access to the connected account. <br>
Mitigation: Store ECHODECKS_API_KEY as a secret and do not paste it into prompts or shared logs. <br>


## Reference(s): <br>
- [EchoDecks API Documentation](artifact/API_DOCS.md) <br>
- [EchoDecks Skill README](artifact/README.md) <br>
- [EchoDecks Developer Settings](https://echodecks.app/settings/developer) <br>
- [EchoDecks](https://echodecks.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance and JSON API responses from the EchoDecks CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an ECHODECKS_API_KEY environment variable and may create content, submit reviews, or consume EchoDecks credits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
