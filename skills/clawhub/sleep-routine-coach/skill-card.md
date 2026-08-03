## Description: <br>
Provides privacy-first, non-diagnostic sleep habit coaching with short setup, consent-gated wind-down reminders, gradual sleep-time adjustment, local record controls, and descriptive weekly summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[raindongdry](https://clawhub.ai/user/raindongdry) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to set up gentle sleep-routine reminders, record goodnight and morning reports, adjust sleep timing gradually, and review descriptive trends without diagnostic or treatment claims. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The delete-all command can recursively delete the configured sleep-routine data directory. <br>
Mitigation: Review before installing, use a dedicated sleep-routine data directory only, and do not point SLEEP_ROUTINE_DATA_DIR or --data-dir at a home, project, sync, or shared directory. <br>
Risk: The skill handles sensitive self-reported sleep habits and reminder preferences. <br>
Mitigation: Persist data only after explicit local-storage consent, keep records in the user-approved local directory, and use the built-in view, export, correction, deletion, and stop-collection controls. <br>
Risk: Health-adjacent sleep guidance could be mistaken for diagnosis or treatment. <br>
Mitigation: Keep guidance non-diagnostic, present trends as descriptive, avoid medication or treatment instructions, and refer users to healthcare professionals for persistent or concerning symptoms. <br>
Risk: Proactive reminders or scheduler jobs could be created without sufficient user intent. <br>
Mitigation: Require separate confirmation of exact reminder times, channel, destination, allowed hours, and quiet behavior before submitting scheduler requests. <br>


## Reference(s): <br>
- [Skill homepage](https://github.com/RAINDONGDRY/sleep-routine-coach) <br>
- [ClawHub skill page](https://clawhub.ai/raindongdry/skills/sleep-routine-coach) <br>
- [Interaction protocol](artifact/references/interaction-protocol.md) <br>
- [Data schema and deterministic rules](artifact/references/data-schema.md) <br>
- [Safety boundaries](artifact/references/safety-boundaries.md) <br>
- [Evidence sources](artifact/references/evidence-sources.md) <br>
- [NHLBI, NIH - Healthy Sleep Habits](https://www.nhlbi.nih.gov/health/sleep-deprivation/healthy-sleep-habits) <br>
- [AASM/Sleep Research Society - Recommended Amount of Sleep for a Healthy Adult](https://aasm.org/resources/pdf/pressroom/adult-sleep-duration-consensus.pdf) <br>
- [NHLBI, NIH - Sleep/Wake Cycle](https://www.nhlbi.nih.gov/health/sleep/sleep-wake-cycle) <br>
- [Oxford Health NHS - Sleep difficulties/insomnia](https://oxfordhealth.nhs.uk/oxon-adult-adhd/resources/sleep-difficulties-insomnia/) <br>
- [NHS Every Mind Matters - How to fall asleep faster and sleep better](https://www.nhs.uk/every-mind-matters/mental-wellbeing-tips/how-to-fall-asleep-faster-and-sleep-better/) <br>
- [NHLBI, NIH - Circadian Rhythm Disorders: Treatment](https://www.nhlbi.nih.gov/health/circadian-rhythm-disorders/treatment) <br>
- [NIDDK, NIH - Symptoms & Causes of Bladder Control Problems](https://www.niddk.nih.gov/health-information/urologic-diseases/bladder-control-problems/symptoms-causes) <br>
- [NHLBI, NIH - Sleep Apnea Symptoms](https://www.nhlbi.nih.gov/health/sleep-apnea/symptoms) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Conversational guidance with JSON-producing Python script commands and scheduler request data when explicitly authorized] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local files for profile, sleep records, reminders, and sleep-shift state; proactive scheduling is consent-gated.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
