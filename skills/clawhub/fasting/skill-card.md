## Description: <br>
Tracks intermittent fasting and extended fasts by logging start and break times, computing elapsed hours, identifying fasting stages and eating windows, and guiding common fasting scenarios with safety-aware checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to log fasting boundaries, check fasting status, plan common fasting protocols, and receive cautious guidance on symptoms, electrolytes, refeeding, religious observance, training, glucose, ketones, and safety red flags. It is not for prescribing fasting to treat diagnosed conditions or overriding clinician guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may store sensitive health, weight, medication, symptom, and religious-observance context in local fasting logs and memory. <br>
Mitigation: Keep records local under ~/Clawic/data/fasting/, log only explicit user signals, and avoid collecting preference or health details unless the user provides them during the fasting workflow. <br>
Risk: Fasting, extended fasting, medication, diabetes, pregnancy, electrolyte, and refeeding guidance can be mistaken for medical advice. <br>
Mitigation: Use the skill as a logger and safety-aware guide only; suspend protocol advice for red flags, avoid medication changes, and route clinician-dependent cases to a qualified professional. <br>
Risk: Extended fasts, dry fasts, low glucose, stacked symptoms, or breaking a long fast can create acute electrolyte, hypoglycemia, dehydration, or refeeding risks. <br>
Mitigation: Apply the artifact's safety gates: screen contraindications first, require electrolyte checks for 24h+ water fasts, stop encouraging unsupervised fasts past 72h, and scale refeeding guidance to fast duration. <br>
Risk: Fasting logs and streak framing can reinforce disordered-eating patterns or pressure users to continue longer than intended. <br>
Mitigation: Never push beyond the user's target, log early breaks neutrally, and stop tracking or return fasting metrics when disordered-eating red flags appear. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/fasting) <br>
- [Clawic Fasting Tracker homepage](https://clawic.com/skills/fasting) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown text with local log and configuration updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores user preferences, fasting logs, and memory under ~/Clawic/data/fasting/ when the agent applies the skill.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
