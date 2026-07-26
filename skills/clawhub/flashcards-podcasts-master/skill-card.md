## Description: <br>
Manage flashcards, generate AI-based cards, create audio podcasts, and track study progress using EchoDecks API integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drgeld](https://clawhub.ai/user/drgeld) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Learners and study-focused agents use this skill to manage EchoDecks decks and cards, generate flashcards and podcasts, retrieve study links, and submit review outcomes through the EchoDecks API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends study materials, deck data, review activity, and account-related requests to EchoDecks. <br>
Mitigation: Install only if you trust EchoDecks with this data, and avoid submitting secrets, regulated data, or other sensitive content in generation inputs. <br>
Risk: Generation and review actions may modify the EchoDecks account or consume credits. <br>
Mitigation: Review proposed deck, generation, podcast, and study-review actions before execution and monitor credit usage. <br>
Risk: The skill depends on an EchoDecks API key. <br>
Mitigation: Keep ECHODECKS_API_KEY private, store it in the environment, and rotate it if exposure is suspected. <br>


## Reference(s): <br>
- [EchoDecks API Documentation](artifact/API_DOCS.md) <br>
- [EchoDecks Website](https://echodecks.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [JSON responses and concise text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an ECHODECKS_API_KEY and may return account, deck, card, podcast, study-link, credit-balance, and review-status data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
