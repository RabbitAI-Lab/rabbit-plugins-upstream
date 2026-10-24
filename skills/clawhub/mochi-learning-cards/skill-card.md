## Description:

Create evidence-backed Chinese or English flashcards from supplied local text, verify exact source quotes, and export safe Markdown, Anki TSV and a manual review checklist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

Learners and educators use this skill to turn supplied Chinese or English source text into evidence-backed flashcards, verify answers against exact quotes, and export study materials for review or manual Anki import.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied source material may be sensitive and is retained in local working files.

Mitigation: Only provide text you allow your configured model to process, and protect the local source copies.

Risk: Generated answers may not be accurate, and an Anki import may not preview as intended.

Mitigation: Review answers against the quoted source and preview manual Anki imports with HTML disabled before confirming.

## Reference(s):

- [MochiLab](https://mochilab.bz)
- [Manual Anki text import](https://docs.ankiweb.net/manual/importing/text-files)
- [ClawHub release](https://clawhub.ai/hznetnewpower/skills/mochi-learning-cards)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown study cards and review checklist, plus UTF-8 tab-separated Anki import text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cards retain paragraph IDs and exact source quotes; exports are generated locally for manual review and import.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
