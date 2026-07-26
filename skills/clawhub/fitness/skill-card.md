## Description: <br>
Plans and progresses workout programs for strength, muscle building, cardio, endurance, and general conditioning with quantified rules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use Fitness to create and adjust workout plans, choose sets, reps, loads, and heart-rate zones, adapt training around layoffs, injuries, travel, or limited equipment, and interpret training logs or wearable readiness data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fitness logs, body metrics, age, injury notes, and wearable-derived readings may be stored as plain local markdown. <br>
Mitigation: Review whether local plain-text storage is acceptable, avoid recording unnecessary sensitive details, and protect or remove ~/Clawic/data/fitness/ files according to the user's privacy needs. <br>
Risk: Workout guidance can be unsafe when the user reports medical red flags, significant pain, or conditions requiring clinician clearance. <br>
Mitigation: Apply the skill's red-flag checks before prescriptions, stop training for listed warning signs, and route urgent or unresolved symptoms to emergency care or a clinician. <br>


## Reference(s): <br>
- [ClawHub Fitness Skill](https://clawhub.ai/ivangdavila/skills/fitness) <br>
- [Clawic Fitness Skill](https://clawic.com/skills/fitness) <br>
- [Setup - Fitness](artifact/setup.md) <br>
- [Program Design - Splits, Templates, Substitutions](artifact/program-design.md) <br>
- [Progression - Models and Plateau Playbooks](artifact/progression.md) <br>
- [Cardio - Zones, Intervals, Concurrent Training](artifact/cardio.md) <br>
- [Recovery - Deloads, Readiness, Overtraining](artifact/recovery.md) <br>
- [Tracking - Logs, Wearables, Trend Reading](artifact/tracking.md) <br>
- [Memory Template - Fitness](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown prose with structured exercise prescriptions and local markdown or configuration updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and update local fitness config, memory, and log markdown under ~/Clawic/data/fitness/ when the user provides relevant information.] <br>

## Skill Version(s): <br>
1.0.4 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
