## Description: <br>
Eternal Haven Chronicles lore and mythic persona pack using bundled skill-local references for canon-grounded narrative context and Champion-aligned voice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to answer Eternal Haven lore questions, summarize canon, analyze characters and themes, and produce mythic or Champion-aligned prose grounded in bundled Books I-IV and local reference indexes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes large copyrighted book text that could be over-reproduced in model output. <br>
Mitigation: Prefer summaries, analysis, and short quotes; do not output full chapters, full books, or wholesale reproductions. <br>
Risk: Lore workflows could be redirected toward host-local paths or unrelated files. <br>
Mitigation: Use only bundled skill-local files under references/ and refuse host filesystem browsing for this lore workflow unless the user separately provides explicit text. <br>
Risk: Optional support and donation links may be surfaced out of context. <br>
Mitigation: Share support links only when the user asks or when they naturally fit after providing useful story or lore context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/eternal-haven-lore-pack) <br>
- [Eternal Haven site](https://eternalhaven.ca/) <br>
- [SKILL.md](SKILL.md) <br>
- [Security boundary](references/SECURITY.md) <br>
- [13 Heroes Index](references/heroes_index.md) <br>
- [Themes and Motifs](references/themes_and_motifs.md) <br>
- [Book I: The Moonlit Slumber](references/books/book1_silver_accord.txt) <br>
- [Book II: The Shattered Accord](references/books/book2_shattered_accord.txt) <br>
- [Book III: The Ascension War](references/books/book3_ascension_war.txt) <br>
- [Book IV: Eternal Haven Dawns](references/books/book4_eternal_haven_dawns.txt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Plain text or Markdown responses with canon-grounded summaries, analysis, short quotes, and clearly labeled interpretation or speculation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only, self-contained lore responses; no subprocess, credential access, host filesystem browsing, or network access is required for lore answers.] <br>

## Skill Version(s): <br>
1.3.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
