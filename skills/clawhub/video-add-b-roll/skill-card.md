## Description:

Use when a talking-head, interview, documentary, or explanatory video needs deliberate transcript-timed visual cutaways from local media or Pexels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitetowerai](https://clawhub.ai/user/whitetowerai)

### License/Terms of Use:

MIT-0

## Use Case:

Video editors, creators, and production agents use this skill to plan, acquire, review, normalize, and verify transcript-timed B-roll cutaways for an already-understood video project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes local media and writes plans, caches, review artifacts, and final render metadata into the project.

Mitigation: Install it only for projects where that local file processing is expected, and review generated artifacts before sharing them outside the project.

Risk: Pexels access uses a local API key and network calls.

Mitigation: Keep the API key in the local environment or skill .env file, never in chat, command arguments, logs, URLs, plans, or review artifacts.

Risk: Generated review and provenance artifacts can expose local source paths or media provenance details.

Mitigation: Avoid distributing those artifacts when local paths, creator details, or rights information are sensitive.

Risk: B-roll choices can be misleading if media does not match the transcript claim or has weak provenance.

Mitigation: Use the required candidate analysis, explicit review gates, provenance checks, and skip behavior when no relevant candidate is available.

## Reference(s):

- [B-Roll Rules](artifact/reference/broll-rules.md)
- [Example B-Roll Plan](artifact/examples/example-broll-plan.json)
- [Example Candidate Ranking](artifact/examples/example-candidate-ranking.json)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, markdown]

**Output Format:** [Markdown instructions with command snippets and structured JSON review, ranking, plan, and receipt artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project-local B-roll plans, candidate analysis and ranking records, review pages, normalized media metadata, verification summaries, and provenance-bound receipts.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
