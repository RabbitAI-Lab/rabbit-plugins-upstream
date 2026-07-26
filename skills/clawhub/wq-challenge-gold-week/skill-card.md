## Description: <br>
Helps agents guide WorldQuant BRAIN Challenge participants through account setup, field and operator discovery, alpha factor construction, gate checks, daily submission selection, score tracking, and iterative research practice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dfkai](https://clawhub.ai/user/dfkai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to run an AI-assisted WorldQuant BRAIN Challenge workflow, including building candidate alpha factors, screening them against Sharpe, Fitness, and self-correlation gates, and deciding which candidates to submit. It is also useful for Chinese-language requests about WorldQuant BRAIN factor mining, Challenge GOLD progress, and AI-assisted quantitative research routines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uses a user's WorldQuant BRAIN account credentials. <br>
Mitigation: Keep BRAIN_EMAIL and BRAIN_PASSWORD in the shell environment only, never hard-code them, and avoid sharing them in chats, issues, or committed files. <br>
Risk: The local workspace can contain alpha identifiers, candidate expressions, PnL cache data, and submission history. <br>
Mitigation: Keep wq_workspace private and out of Git, and delete local caches when they are no longer needed. <br>
Risk: Submitting an alpha is an account action that may affect challenge standing. <br>
Mitigation: Review each alpha before confirming submission; the included submission workflow requires interactive human confirmation. <br>
Risk: The scripts communicate with WorldQuant BRAIN APIs using the user's account. <br>
Mitigation: Install only for this intended use and restrict network access to WorldQuant BRAIN where possible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dfkai/skills/wq-challenge-gold-week) <br>
- [WorldQuant BRAIN platform](https://platform.worldquantbrain.com/) <br>
- [WorldQuant BRAIN API](https://api.worldquantbrain.com) <br>
- [Rules and scoring reference](artifact/references/01-rules-and-scoring.md) <br>
- [Data and operator probing reference](artifact/references/02-arsenal-probing.md) <br>
- [Factor construction reference](artifact/references/03-factor-construction.md) <br>
- [Submission harvest reference](artifact/references/04-submission-harvest.md) <br>
- [AI research loop reference](artifact/references/05-research-loop.md) <br>
- [Five-day plan reference](artifact/references/06-five-day-plan.md) <br>
- [QuantML wq-alpha-research inspiration](https://github.com/QuantML-Research/wq-alpha-research) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, Python code workflows, and local JSON/JSONL workspace files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local wq_workspace artifacts such as arsenal_usa.json, recipes.json, tried.txt, pool.jsonl, pnl_cache files, and submit_log.jsonl when the bundled scripts are run.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
