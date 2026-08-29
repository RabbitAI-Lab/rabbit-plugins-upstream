## Description:

Create original songs, AI-generated music, lyrics-to-song tracks, instrumentals, background music, video soundtracks, jingles, multilingual songs, and reference-led arrangements from a clear creative brief.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and creators use this skill to turn themes, lyrics, scenes, or reference audio into a structured music brief and, when approved, reviewable AI-generated songs, instrumentals, background music, or soundtracks. The skill supports creative planning, lyrics preparation, model selection, Beatra music generation, task recovery, delivery, and focused revision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Beatra account authorization and stores a shared token under ~/.beatra.

Mitigation: Install only when the user trusts the Beatra authorization model; use the documented uninstall and disconnect workflow for credential cleanup.

Risk: Approved music generation can spend Beatra credits.

Mitigation: Show the model, title, lyrics or instrumental status, reference audio, controls, and one-generation scope before making a billable request.

Risk: The skill can upload selected local reference audio.

Mitigation: Upload only the intended FLAC, MP3, or WAV file through the bundled upload command and review what should carry over or change before generation.

Risk: The bundled client silently checks for and may install package updates by default.

Mitigation: Review the update behavior before installation and run the documented auto-update disable command if silent updates are not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/music-generation-studio)
- [Beatra skill homepage](https://beatra.ai/skills/music-generation-studio)
- [Intent and routing](references/intent-and-routing.md)
- [Creative brief and style](references/creative-brief-and-style.md)
- [Lyrics craft](references/lyrics-craft.md)
- [Vocal, language, and tags](references/vocal-language-and-tags.md)
- [Model routing](references/model-routing.md)
- [Music recipes](references/music-recipes.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Review and iteration](references/review-and-iteration.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and Beatra task result details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Beatra task IDs, audio clip URLs, artifact IDs, durations, MIME types, sizes, and net charged credits when generation succeeds.]

## Skill Version(s):

0.1.7 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
