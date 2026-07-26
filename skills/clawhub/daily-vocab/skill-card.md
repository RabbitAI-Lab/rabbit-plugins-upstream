## Description: <br>
Daily Vocab generates one advanced English vocabulary learning card per day with IPA pronunciation, etymology, examples, and quiz mode. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiajiaoy](https://clawhub.ai/user/jiajiaoy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, students, and language learners use this skill to practice advanced English vocabulary for GRE, SAT, IELTS, academic writing, and professional communication. Developers or OpenClaw users can also enable optional scheduled morning and evening vocabulary prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional push setup can create recurring OpenClaw cron jobs that send daily vocabulary prompts to a messaging channel. <br>
Mitigation: Enable push only when recurring messages are desired, and use the documented off command or cron list to manage or remove scheduled prompts. <br>


## Reference(s): <br>
- [Daily Vocab ClawHub Skill Page](https://clawhub.ai/jiajiaoy/skills/daily-vocab) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance, generated HTML, and OpenClaw cron command payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a daily-vocab.html learning card and can optionally configure recurring morning and evening push prompts.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
