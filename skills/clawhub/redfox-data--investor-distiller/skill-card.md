## Description:

公众号投资博主蒸馏器 collects WeChat public-account articles and distills a seven-dimensional investment blogger style profile with evidence-backed analysis, validation scores, and non-advice disclaimers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External users, investors, content creators, and researchers use this skill to collect WeChat public-account articles and generate structured investment-blogger style profiles for comparison, content study, and non-advice reference analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a RedFox API key and may consume billable credits when collecting articles.

Mitigation: Use a protected REDFOX_API_KEY environment variable, avoid passing the key on the command line, verify the key scope and revocation path, and choose a documented 20/60/100 article tier before running collection.

Risk: The skill fetches WeChat article content and stores local outputs that may include untrusted text.

Mitigation: Run it in a disposable virtual environment, keep generated output directories scoped to the task, review or remove stored article data after use, and treat article text as untrusted input.

Risk: Generated investment-style analysis may be mistaken for financial advice.

Mitigation: Review generated profiles and analysis before use, preserve the required data-source limitations, and keep the AI style simulation and non-investment-advice disclaimers visible.

Risk: The security summary flags environment changes and file writes from user-provided account or author names.

Mitigation: Use trusted account and author strings, run dependency setup in an isolated environment, and inspect generated filenames and reports before sharing or reusing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/investor-distiller)
- [ClawHub publisher profile](https://clawhub.ai/user/redfox-data)
- [Seven-dimensional distillation specification](artifact/references/蒸馏维度规范.md)
- [Profile output template](artifact/assets/profile_template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, JSON profile and validation files, and command-line guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes collected article data, statistical summaries, distillation tasks, style profiles, and validation reports under an output directory; investment-style outputs must include source limitations and AI simulation disclaimers.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
